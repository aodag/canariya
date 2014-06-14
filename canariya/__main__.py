import argparse
from .commands.runtest import RunTestCommand


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module")
    args = parser.parse_args()
    print(args)
    command = RunTestCommand()
    command(args)


if __name__ == '__main__':
    main()