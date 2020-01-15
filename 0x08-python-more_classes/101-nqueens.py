#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argv = sys.argv

    if len(argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
