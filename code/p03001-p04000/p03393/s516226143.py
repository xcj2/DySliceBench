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
    S = list(input())


    if len(S) == 26:
        # abc = [chr(i) for i in range(97, 123)]
        # print(S)
        for i in range(25, -1, -1):
            for j in range(25, i, -1):
                # print(i, j, S[i], S[j])
                if S[i] < S[j]:
                    ans = S[:i] + [S[j]]
                    printlist(ans, '')
                    return

        print(-1)

    else:
        abc = [chr(i) for i in range(97, 123)]

        for s in S:
            if s in abc:
                abc[ord(s) - 97] = 0

        for t in abc:
            if t != 0:
                S.append(t)
                printlist(S, k='')
                return


if __name__ == '__main__':
    solve()
