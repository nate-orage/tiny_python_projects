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

    # print('narwhal')
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
