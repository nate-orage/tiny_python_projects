#!/usr/bin/env python3
"""
Author : nate <nate@localhost>
Date   : 2021-08-10
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text Here')

    parser.add_argument('-o',
                        '--outfile',
                        help='This will output to a text file.',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
    if os.path.isfile(args.text): # If the argument given is a text file, the program will open it to read.
        args.text = open(args.text).read().rstrip().upper()
    
    return args
# --------------------------------------------------
def main():
    args = get_args()
    '''One Solution'''
    # if args.outfile:
    #     print(args.text.upper(),file=open(args.outfile, 'wt'))
    # else:
    #     print(args.text.upper())
    '''Another Solution'''
    # out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    # print(args.text.upper(), file=out_fh)
    '''Another Solution'''
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()

      


# --------------------------------------------------
if __name__ == '__main__':
    main()
