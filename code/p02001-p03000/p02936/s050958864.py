import sys
from collections import defaultdict
def wi(): return list(map(int, sys.stdin.readline().split()))
def i(): return int(sys.stdin.readline())
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def mip(n): return [wip() for _ in range(n)]

def main():
    n, q = wi()
    ab = mip(n - 1)
    px = mip(q)
    for i in range(q):
        px[i][1] += 1


    cost = [0] * n
    for i in range(q):
        cost[px[i][0]] += px[i][1]

    son = [[] for _ in range(n)]
    for i in range(n - 1):
        son[ab[i][0]].append(ab[i][1])
        son[ab[i][1]].append(ab[i][0])

    flagli = [0] * n
    flagli[0] = 1
    queue = []
    queue.append(0)
    while queue != []:
        po = queue.pop()
        for kk in son[po]:
            if flagli[kk] == 0:
                flagli[kk] = 1
                queue.append(kk)
                cost[kk] += cost[po]

    for i in range(n):
        print(cost[i],"" , end="")

if __name__ == '__main__':
    main()