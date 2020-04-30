#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 Arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    i = 0
    for arg in sys.argv:
        if i != 0:
            print("{}: {}".format(i, arg))
        i += 1
