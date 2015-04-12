#!/usr/bin/py


def lonely_integer(b):
    for i, val in enumerate(b):
        if val not in b[:i] and val not in b[i+1:]:
            return val

if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().strip().split(" ")))
    print(lonely_integer(b))
