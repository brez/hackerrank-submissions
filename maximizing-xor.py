#!/usr/bin/python3


def max_xor(l, r):
    h = []
    for i in range(l, r+1):
        for j in range(i, r+1):
            h.append(i ^ j)
    return max(h)

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(max_xor(l, r))
