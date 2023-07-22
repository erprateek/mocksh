import os
import sys
import argparse
from generic_utils import get_ftype

def main():
    parser.ArgumentParser()
    parser.add_argument('-s','--specification_file')

    args = parser.parse_args()

    ftype = get_ftype(args.specification_file)
    

if __name__ == '__main__':
    main()
