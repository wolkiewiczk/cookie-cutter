import random
from math import radians, tan

from PIL import Image, ImageDraw


class CookieMold:

    def __init__(self, image, rows=3, columns=3):
        self.image = Image.open(image)
        self.piece_width = self.image.width // columns
        self.piece_height = self.image.height // rows
        self.pieces = self.generate_pieces(rows, columns)

    def generate_pieces(self, rows=3, columns=3):

        width_joints = list(range(0, self.piece_width * columns, self.piece_width))
        height_joints = list(range(0, self.piece_height * rows, self.piece_height))

        return [(wj, hj) for wj in width_joints for hj in height_joints]

    def calculate_ray(self, screen_width_mm, screen_width_px, distance, angle):
        tangent = tan(radians(angle))
        ray_mm = distance * tangent
        return round(ray_mm * screen_width_px / screen_width_mm)

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
