"""foobar v0.1.0

just foo

Usage:
    foobar [options] <argument>
    foobar -h | --help
    foobar -V | --version

Options:
    -h --help                 show help and exit
    -V --version              show version and exit
"""
from docopt import docopt


def main(argv=None):
    args = docopt(__doc__, argv=argv, version='0.1.0')
    print(args)

if __name__ == "__main__":
    main()
