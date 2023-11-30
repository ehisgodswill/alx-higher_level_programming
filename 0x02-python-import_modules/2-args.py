#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    lnt = len(sys.argv) - 1
    if lnt == 0:
        print("0 arguments.")
    elif lnt == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(lnt))
        for i in range(lnt):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
