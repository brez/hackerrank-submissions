#!/usr/bin/python3


def utopia(n, j=0, s=1):
    if (j == n):
        return s
    if(j % 2 == 0):
        return utopia(n, (j+1), (s+s))
    else:
        return utopia(n, (j+1), (s+1))

for i in range(int(input())):
    n = int(input())
    print(utopia(n))
