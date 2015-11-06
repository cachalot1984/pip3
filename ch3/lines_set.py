#!/usr/bin/python
import sys

if len(sys.argv) < 3:
    print('usage: {0} file1 file2'.format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as fd1:
    lines_f1 = set([line for line in fd1])
    with open(sys.argv[2]) as fd2:
        lines_f2 = set([line for line in fd2])
        print('---------------')
        for line in (lines_f1 & lines_f2):
            print(line)
        print('---------------')
        for line in (lines_f1 | lines_f2):
            print(line)
        print('---------------')
        for line in (lines_f1 - lines_f2):
            print(line)
        
