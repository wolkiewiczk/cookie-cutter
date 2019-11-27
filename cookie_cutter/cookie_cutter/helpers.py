import random

from PIL import Image, ImageDraw


class CookieMold:

    def __init__(self, image, rows=3, columns=3):
        self.image = Image.open(image)
        self.piece_width = self.image.width // columns
        self.piece_height = self.image.height // rows
        self.pieces = self.generate_pieces(rows, columns)
        print(self.pieces)

    def generate_pieces(self, rows=3, columns=3):

        width_joints = list(range(0, self.piece_width * columns, self.piece_width))
        height_joints = list(range(0, self.piece_height * rows, self.piece_height))

        return [(wj, hj) for wj in width_joints for hj in height_joints]

    def cut(self, ray):
        piece_coords = random.choice(self.pieces)
        ray = min([2 * ray, self.piece_height, self.piece_width]) // 2
        x = random.randrange(piece_coords[0] + ray, piece_coords[0] + self.piece_width - ray + 1)
        y = random.randrange(piece_coords[1] + ray, piece_coords[1] + self.piece_height - ray + 1)
        cookie = self.image.crop((x - ray, y - ray, x + ray, y + ray))

        alpha = Image.new('L', (cookie.width, cookie.height), 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([(0, 0), alpha.size], 0, 360, fill=255)
        cookie.putalpha(alpha)
        return cookie, x, y
