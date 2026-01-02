# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    S = list(input())
    k = II()
    n = len(S)
    S2 = S[:]

    if len(set(S)) == 1:
        print(n * k // 2)
    else:
        cnt = 0
        for i in range(n-1):
            j = i + 1
            si, sj = S[i], S[j]
            if si == sj:
                S[j] = i
                cnt += 1
        if S[0] == S[-1]:
            moji = S[0]
            sl = 0
            for s in S2:
                if s == moji:
                    sl += 1
                else:
                    break
            sr = 0
            for s in S2[::-1]:
                if s == moji:
                    sr += 1
                else:
                    break

            print(cnt * k + ((sl+sr)//2 - sl//2 - sr//2) * (k - 1))
        else:
            print(cnt * k)


if __name__ == '__main__':
    solve()
