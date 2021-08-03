#!/home/nate/python/python_env/bin/python3
"""
Author : nate <nate@localhost>
Date   : 2021-07-31
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text",
        metavar="str",
        type=str,
        help="Each number in the text will be encoded using this algorithm.",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    text = args.text # This creates a variable by extracting the values used by the argument
    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
    }

    new_text = ""
    for char in text:
        new_text += jumper.get(char, char)
    print(new_text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
