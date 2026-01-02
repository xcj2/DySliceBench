import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

def solve():
    n = II()
    S = list(map(int, list(input())))

    ans = 0
    for v in range(0, 1000):
        V = list(str(v))
        if len(V) == 2:
            V.insert(0, '0')
        elif len(V) == 1:
            V.insert(0, '0')
            V.insert(0, '0')
        elif len(V) == 0:
            V.insert(0, '0')
            V.insert(0, '0')
            V.insert(0, '0')
        # print(V)

        # end = [0] * 3
        cnt = 0
        for s in S:
            # print(V[cnt], str(s))
            if V[cnt] == str(s):
                cnt += 1
                if cnt == 3:
                    # print(V)
                    break
        # print(cnt)
        # input()
        if cnt == 3:
           ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
