import random

from PIL import Image, ImageDraw


class CookieMold:

    def __init__(self, image, rows=3, columns=3):
        self.image = Image.open(image)
        self.pieces = self.generate_pieces(rows, columns)

    def generate_pieces(self, rows=3, columns=3):
        piece_width = self.image.width // columns
        piece_height = self.image.height // rows

        width_joints = list(range(0, piece_width * columns, piece_width))
        height_joints = list(range(0, piece_height * rows, piece_height))

        return [(wj, hj, wj + piece_width, hj + piece_height) for wj in width_joints for hj in height_joints]

    def cut(self, ray):
        piece_coords = random.choice(self.pieces)
        piece = self.image.crop(piece_coords)
        ray = min([2 * ray, piece.height, piece.width]) // 2
        x = random.randrange(ray, piece.width - ray + 1)
        y = random.randrange(ray, piece.height - ray + 1)
        cookie = piece.crop((x - ray, y - ray, x + ray, y + ray))

        alpha = Image.new('L', (cookie.width, cookie.height), 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([(0, 0), alpha.size], 0, 360, fill=255)
        cookie.putalpha(alpha)
        return cookie
