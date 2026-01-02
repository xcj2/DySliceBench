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
    a, b, c, x, y = MI()

    ans = 0
    if a + b <= 2 * c:
        mn = min(x, y)
        ans = a * mn + b * mn
        x -= mn
        y -= mn

        if x < y:
            x = y
            a = b

        if a > 2*c:
            ans += x * 2 * c
        else:
            ans += x * a

    else:
        mn = min(x, y)
        ans = mn * 2 * c
        x -= mn
        y -= mn

        if x < y:
            x = y
            a = b

        if a > 2 * c:
            ans += x * 2 * c
        else:
            ans += x * a

    print(ans)



if __name__ == '__main__':
    solve()
