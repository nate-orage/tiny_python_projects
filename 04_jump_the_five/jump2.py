#!/usr/bin/env python3
"""
Author : nate <nate@localhost>
Date   : 2021-08-03
Purpose: Numbers to Words
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Numbers to Words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "numbers", metavar="str", type=str, help="A positional argument"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    text = args.numbers
    words = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }

    spelling = ""
    for num in text:
        spelling += words.get(num, num)

    print(spelling)

    # str_arg = args.arg
    # int_arg = args.int
    # file_arg = args.file
    # flag_arg = args.on
    # pos_arg = args.positional

    # print(f'str_arg = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
