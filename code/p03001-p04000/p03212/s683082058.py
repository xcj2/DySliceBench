import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

ans = 0
c = ['3', '5', '7']
N = 0

def check(l):
    return len(set(l)) == 4

def nummaker(k, n):
    global ans
    if k == 0:
        q = int(''.join(n))
        if q > N:
            print(ans)
            sys.exit(0)
        if check(n):
            ans += 1
        return
    for i in c:
        m = n[:]
        m.append(i)
        nummaker(k-1, m)

def rec(x):
    # print(x)
    ans = 0
    c = int(x)
    if c > N:
        return 0
    if check(x):
        ans += 1
    # if ans == 1:
    #     print(x)
    for s in '357':
        ans += rec(x + s)
    return ans

def main():
    global N
    N = int(input().strip())
    print(rec('0'))
    # for i in range(1, 11):
        # nummaker(i, [])

if __name__ == '__main__':
    main()
