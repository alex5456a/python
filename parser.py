#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Read a file')
parser.add_argument('filename', help='the file to process')
parser.add_argument('--limit', '-l', type=int, help='the number of line to process')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileExistsError as err:
    print(f"error: {err}")
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::1])
            