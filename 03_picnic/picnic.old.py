#!/usr/bin/env python3
"""
Author : nate <nate@localhost>
Date   : 2021-07-24
Purpose: Picnic
"""

import argparse
from typing import ItemsView


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='item',
                        type=str,
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                       # metavar='',
                        action='store_true',
                        #default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args.items)
    # print(args.sorted)
    # items = []
    # items.append(args)

   
    print('You are bringing ', items,  '.')
    
    
    
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
if __name__ == '__main__':
    main()
