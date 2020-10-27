#!/usr/bin/env python3
import time
import argparse
import sys
from PIL import Image

parser = argparse.ArgumentParser(
    usage='%(prog)s <[-i] [--image]> [Location] || <[-a] [--ascii]> [Location]',
    description='''simple python program
            that output ascii art with animation.
        ''')

parser.add_argument(
    '-i',
    '--image',
    nargs='+',
    default=False,
    help="Location of image")
parser.add_argument(
    '-a',
    '--ascii',
    nargs='+',
    default=False,
    help="Location of text file containing ascii art")
parser.add_argument(
    '-w',
    '--width',
    type=int,
    default=100,
    nargs='?',
    help="Width of ascii art")
parser.add_argument(
    '-s',
    '--speed',
    type=float,
    default=0.1,
    nargs='?',
    help="Speed of animation")

args = parser.parse_args()


def validate():
    if(len(sys.argv) <= 1):
        parser.print_help()
        exit()


def img_to_display():
    if args.image:
        return 'img'
    elif args.ascii:
        return 'ascii'


class Animate:
    def __init__(self, speed=0.01):
        self.speed = speed

    @staticmethod
    def __resize(image, new_width):
        width, height = image.size
        aspect_ratio = float(height) / float(width)
        new_height = aspect_ratio * new_width * 0.55
        image = image.resize((new_width, int(new_height)))

        return image

    @staticmethod
    def __grayscale(image):
        return image.convert('L')

    @staticmethod
    def __modify(image, buckets=25):
        initial_pixels = image.getdata()
        chars = list("@#S%?*+;:,.")
        new_pixels = [chars[pixel // buckets] for pixel in initial_pixels]
        return ''.join(new_pixels)

    @staticmethod
    def __process(image, new_width):
        image = Animate.__resize(image, new_width)
        image = Animate.__grayscale(image)
        pixels = Animate.__modify(image)

        len_pixels = len(pixels)

        new_image = [pixels[index: index + new_width]
                     for index in range(0, len_pixels, new_width)]
        return '\n'.join(new_image)

    @staticmethod
    def image_ascii(path):
        image = None
        try:
            image = Image.open(path)
        except Exception:
            print('Unable to find image in {} \n'.format(path))
            exit()

        return Animate.__process(image, args.width)

    def animate(self, art):
        for _ in art:
            print(_, end='', flush=True)
            time.sleep(self.speed)


if __name__ == '__main__':
    validate()
    a = Animate(args.speed)
    if img_to_display() == 'img':
        a.animate(Animate.image_ascii(args.image[0]))
    else:
        with open(args.ascii[0], 'r') as f:
            a.animate(f.read())
