#!/home/nate/python/python_env/bin/python3
"""
Author : nate <nate@localhost>
Date   : 2021-07-30
Purpose: Picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='item',
                        type=str,
                        nargs='+',
                        help='Items we are bringing')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items.',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    items = args.items
    num_items = len(items)
    bringing = ''

    if args.sorted:
        items.sort()

    if num_items == 1:
        bringing = items[0]
    elif num_items == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')



    # print('You are bringing', args, '.')
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
