

"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()
flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**26)

def iin(): return int(input())


def lin(): return list(map(int, input().split()))

# out = []
# range = xrange
# input = raw_input

def main():
    from math import gcd
    n = iin()
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                ans += gcd(gcd(i, j), k)
    print(ans)

main()
# threading.Thread(target=main).start()
