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

    abc = [chr(i) for i in range(97, 123)]
    # print(abc)

    for s in S:
        if s in abc:
            abc[ord(s) - 97] = 0



    if len(S) == 26:
        # abc = [chr(i) for i in range(97, 123)]
        # print(S)
        SR = S[::-1]
        # print(SR)
        idx = (INF, INF)
        for i in range(26):
            for j in range(i+1, 26):
                if SR[i] > SR[j]:
                    # print(i, j)
                    # print(S[:-j])
                    if j < idx[1]:
                        idx = (i, j)
                    break
        # print(idx)
        i, j = idx
        if i == INF:
            print(-1)
        else:
            ans = S[:-j-1]
            ans.append(SR[i])
            printlist(ans, '')

    else:
        for t in abc:
            if t != 0:
                S.append(t)
                printlist(S, k='')
                return

if __name__ == '__main__':
    solve()
