import sys

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MATINT(h): return [list(map(int, input().split())) for _ in range(h)]
def MATSTR(h): return [input() for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
inf = float('inf')
mod = 10 ** 9 + 7

def main():
    S = input() + 'R'
    R = 0
    L = 0
    Ri = 0
    Li = 0
    flag = 0
    ans = [0] * (len(S)-1)
    for i in range(len(S)-1):
        if S[i] == 'R':
            R += 1
        elif S[i] == 'L':
            if flag == 0:
                Ri = i - 1
                Li = i
                flag = 1
            L += 1
            if S[i + 1] == 'R':
                tmp = R + L
                if tmp % 2 == 0:
                    ans[Ri] = tmp // 2
                    ans[Li] = tmp // 2
                else:
                    if R > L:
                        if R % 2 == 0:
                            ans[Ri] = tmp // 2
                            ans[Li] = ceil(tmp, 2)
                        else:
                            ans[Ri] = ceil(tmp, 2)
                            ans[Li] = tmp // 2
                    else:
                        if L % 2 == 0:
                            ans[Ri] = ceil(tmp, 2)
                            ans[Li] = tmp // 2
                        else:
                            ans[Ri] = tmp // 2
                            ans[Li] = ceil(tmp, 2)
                flag = 0
                L = 0
                R = 0
    print(*ans)

if __name__ == '__main__':
    main()
