import argparse
import pickle
import sys

from PIL import Image
import numpy as np


def shred(img, rows, cols, shuffle=True):
    x = np.linspace(0, img.shape[1], rows + 1).astype(int)
    y = np.linspace(0, img.shape[0], cols + 1).astype(int)
    shredded = [
        (img[y[j]:y[j + 1], x[i]:x[i + 1]], (j, i))
        for i in range(rows)
        for j in range(cols)
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
        '--cols',
        '-c',
        default=50,
        type=int,
        help='Number of pieces of paper in the cols direction. Defaults to 50.'
    )
    parser.add_argument(
        '--rows',
        '-r',
        default=4,
        type=int,
        help='Number of pieces of paper in the rows direction. Defaults to 4.'
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
    images, indices = shred(img, args.rows, args.cols, shuffle=True)
    with open(args.output, 'wb') as o_:
        pickle.dump({
                'rows': args.rows,
                'cols': args.cols,
                'size': args.rows*args.cols,
                'images': images,
                'indices': indices
            },
            o_
        )


if __name__ == '__main__':
    main()