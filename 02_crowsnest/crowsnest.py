#!/home/nate/python/python_env/bin/python3
"""
Author : Nate
Date   : today
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crows Nest", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("word", metavar="word", help="A single word")
    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    word = args.word
    char = word[0]
    article = ""

    if word[0] in "aeiou":
        article = "an"
    elif word[0] in "AEIOU":
        article = "An"
    elif word[0] not in "AEIOUaeiou" and word[0] == word[0].upper():
        article = "A"
    else:
        article = "a"
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")

if __name__ == "__main__":
    main()
