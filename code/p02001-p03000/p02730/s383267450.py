"""
NTC here
"""
import sys
inp = sys.stdin.readline


def input(): return inp().strip()


flush = sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**25)


def iin(): return int(input())


def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input


def main():
    def fn(s):
        l = len(s)
        l, r = 0, l-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    s = input()
    n = len(s)
    print("Yes" if fn(s) and fn(s[:n//2]) else "No")

main()
# threading.Thread(target=main).start()
