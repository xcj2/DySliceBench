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
    N = ii()
    S, T = input().rstrip().split()
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)
    return


if __name__ == '__main__':
    main()
