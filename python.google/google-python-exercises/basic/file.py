#!~/.linuxbrew/bin/python -tt

import sys

def Cat(filename):
    f = open(filename, 'rU')
    lines = f.read()
    print lines,
    f.close()


def main():
    Cat(sys.argv[1])
    print sys.argv[1]


if __name__ == '__main__':
    main()
