#!/usr/bin/py

if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    s = list(input())
    j,c = (len(s)-1, 0)
    for i in range(int(j/2)+1):
      if(s[i] != s[j]):
        a,b = (ord(s[i]), ord(s[j]))
        if(a > b):
          c += a - b
        else:
          c += b - a
      j -= 1
    print(c)
