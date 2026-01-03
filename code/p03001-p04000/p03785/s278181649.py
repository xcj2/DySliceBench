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
    n, c, k = MI()

    T = [-1] * n
    for i in range(n):
        T[i] = II()
    T = sorted(T)

    bus_cnt = 1
    person_cnt = 0
    th = T[0] + k
    for i in T:
        # print(i, th, bus_cnt, person_cnt)
        if i <= th:
            if person_cnt + 1 > c:
                bus_cnt += 1
                th = i + k
                person_cnt = 1
            else:
                person_cnt += 1
        else:
            bus_cnt += 1
            person_cnt = 1
            th = i + k
    print(bus_cnt)

if __name__ == '__main__':
    solve()
