# -*- coding: utf-8 -*-
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
write = sys.stdout.write
def ii(): return int(readline())
def mi(): return map(int, readline().rstrip().split())
def li(): return list(readline().rstrip())
def lmi(): return list(map(int, readline().rstrip().split()))
def end(*arg): print(*arg); sys.exit()
# template


def main():
    n = ii()
    a = lmi()
    i = 0
    tmp = 1
    while i < n:
        if a[i] == tmp:
            tmp += 1
            i += 1
        else:
            i += 1
    if(tmp == 1):
        print(-1)
    else:
        print(n - (tmp - 1))
    return


if __name__ == '__main__':
    main()
