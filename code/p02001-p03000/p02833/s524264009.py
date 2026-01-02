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
    if n % 2 == 1:
        print(0)
    else:
        ans = 0
        for i in range(1, 60):
            ans += (n // (2 * pow(5, i)))
        print(ans)

    return


if __name__ == '__main__':
    main()
