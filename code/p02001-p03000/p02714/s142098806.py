

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
    from bisect import bisect_right as br
    def find(a, b, c):
        sc = set(c)
        smc = len(c)
        ans = 0
        for i in a:
            for j in b:
                if j>i:
                    x = smc - br(c, j)
                    ans += x - (1 if (j-i)*2+i in sc else 0)
        return ans


    n = iin()
    s = input()
    dc = {'R':[], 'G':[], 'B':[]}
    for i in range(n):
        dc[s[i]].append(i)
    a, b, c = dc['R'], dc['B'], dc['G']
    ans = find(a, b, c) + find(a, c, b) + find(b, a, c) + find(b, c, a) + find(c, a, b) + find(c, b, a)
    print(ans)

main()
# threading.Thread(target=main).start()
