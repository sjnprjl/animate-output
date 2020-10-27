#!/usr/bin/env python3
import time
import argparse
import sys
from PIL import Image

parser = argparse.ArgumentParser(usage='%(prog)s <[-i] [--image]> [Location] || <[-a] [--ascii]> [Location]',
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


validate()


def img_to_display():
    if args.image:
        return 'img'
    elif args.ascii:
        return 'ascii'

# display help message if no argument is passed


class Animate:
    def __init__(self, speed=0.01):
        self.speed = speed

    @staticmethod
    def image_ascii(img):
        img = Image.open(img)
        width, height = img.size
        a_r = height / width
        n_w = args.width
        n_h = a_r * n_w * 0.55
        img = img.resize((n_w, int(n_h)))

        img = img.convert('L')
        pixels = img.getdata()

        chars = [";", "x", "{", "&", "@", "$", "%", "*", "!", ":", "."]
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        new_pixels_count = len(new_pixels)
        ascii_img = [new_pixels[index:index + n_w]
                     for index in range(0, new_pixels_count, n_w)]
        ascii_img = "\n".join(ascii_img)

        return ascii_img

    def animate(self, art):
        for _ in art:
            print(_, end='', flush=True)
            time.sleep(self.speed)


if __name__ == '__main__':
    a = Animate(args.speed)

    if img_to_display() == 'img':
        a.animate(Animate.image_ascii(args.image[0]))
    else:
        with open(args.ascii[0], 'r') as f:
            a.animate(f.read())
