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
    E = list(map(int, list(input())))
    # print(E)

    for i in range(1<<3):
        op = ['-'] * 3
        for j in range(3):
            if i >> j & 1:
                op[j] = '+'

        f = '{}{}{}{}{}{}{}'.format(E[0], op[0], E[1], op[1], E[2], op[2], E[3])
        e = eval(f)
        if e == 7:
            print(f + '=7')
            return



if __name__ == '__main__':
    solve()
