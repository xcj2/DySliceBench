import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def keta(n):
    return len(str(n))

def make(n, l, r):
    ans = 0
    sn = str(n)
    for i in range(5):
        if keta(n) > 2+i:
            ans += 10 ** i
        elif keta(n) == 2 + i:
            if sn[0] > str(l):
                ans += 10 ** i
            elif sn[0] == str(l):
                if sn[-1] < r:
                    ans += int(sn[1:-1])
                else:
                    if sn[1:-1] == '':
                        ans += 1
                    else:
                        ans += int(sn[1:-1]) + 1
            else:
                pass
        else:
            pass
    if l == r:
        ans += 1
    return ans

def main():
    n = int(input().strip())
    ans = 0
    for i in range(1, n+1):
        p = make(n, str(i)[-1], str(i)[0])
        if i % 10 == 0:
            continue
        # if i < 10:
        #     p += 1
        # print("i ,p: ", i, p)
        ans += p
    print(ans)
if __name__ == '__main__':
    main()
