#!/usr/bin/env python3
import time
import argparse
import sys
from image2ascii import Image2Ascii as A2I
try:
    import pyperclip
except Exception:
    pass
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
    '-c',
    '--clipboard',
    action='store_true', 
    # nargs='+',
    help="Copy from clipboard")
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

def help():
    parser.print_help()
    exit()


def validate():
    if(len(sys.argv) <= 1):
        help()


def img_to_display():
    if args.image:
        return 'img'
    elif args.ascii:
        return 'ascii'
    elif args.clipboard:
        return 'clip'


class Animate:
    def __init__(self, speed=0.01):
        self.speed = speed

    def animate(self, art):
        for _ in art:
            print(_, end='', flush=True)
            time.sleep(self.speed)

if __name__ == '__main__':
    validate()
    a = Animate(args.speed)
    if img_to_display() == 'img':
        asc = A2I(args.image[0] , args.width).convert()
        a.animate(asc)
    elif img_to_display() == 'ascii':
        with open(args.ascii[0], 'r') as f:
            a.animate(f.read())
    elif img_to_display() == 'clip':
        d = None
        try:
            d = pyperclip.paste() 
        except Exception:
            d = """
            Did you just edit the code or you forgot 
            to install pyperclip module?
            """
        a.animate(d)
    else:
        help()
