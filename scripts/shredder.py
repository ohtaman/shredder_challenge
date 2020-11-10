import argparse
import pickle
import sys

from PIL import Image
import numpy as np


def shred(img, vertical_bins, horizontal_bins, shuffle=True):
    cols = np.linspace(0, img.shape[1], vertical_bins + 1).astype(int)
    rows = np.linspace(0, img.shape[0], horizontal_bins + 1).astype(int)
    shredded = [
        (img[rows[j]:rows[j + 1], cols[i]:cols[i + 1]], (j, i))
        for i in range(vertical_bins)
        for j in range(horizontal_bins)
    ]
    if shuffle:
        np.random.shuffle(shredded)
    return list(zip(*shredded))


def parse_args(argv):
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser('shredder')
    parser.add_argument(
        '--vertical',
        default=50,
        type=int,
        help='Number of pieces of paper in the vertical direction. Defaults to 50.'
    )
    parser.add_argument(
        '--horizontal',
        default=4,
        type=int,
        help='Number of pieces of paper in the horizontal direction. Defaults to 4.'
    )
    parser.add_argument(
        'image',
        help='Path to the image to shred.'
    )
    parser.add_argument(
        'output',
        help='Path to the output pickle file.'
    )

    return parser.parse_args(argv)


def main(argv=sys.argv):
    args = parse_args(argv[1:])

    img = np.array(Image.open(args.image))
    shredded = shred(img, args.vertical, args.horizontal, shuffle=True)
    with open(args.output, 'wb') as o_:
        pickle.dump(shredded, o_)


if __name__ == '__main__':
    main()