#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Read a file')
parser.add_argument('filename', help='the file to process')
parser.add_argument('--limit', '-l', type=int, help='the number of line to process')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args)