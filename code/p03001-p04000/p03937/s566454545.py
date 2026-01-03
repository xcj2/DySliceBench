# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    h, w = MI()
    cnt = 0
    for i in range(h):
        l = list(input())
        for j in range(w):
            if l[j] == '#':
                cnt = cnt + 1
    if h + w - 1 == cnt:
        print('Possible')
    else:
        print('Impossible')

if __name__ == '__main__':
    solve()
