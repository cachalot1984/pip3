#!/usr/bin/python3

import sys, collections

Statistics = collections.namedtuple('Statistics', 'mean mode median std_dev')

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print()
        sys.exit(0)

main()
