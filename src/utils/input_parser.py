import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file",
        type=str,
        help="Provide the path to the text file.",
    )

    return parser.parse_args()
