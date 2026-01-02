from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M = ZZ()
    edge = [ZZ() for _ in range(M)]
    E = defaultdict(list)
    for a, b in edge:
        E[a].append(b)
        E[b].append(a)

    color = [0] * (N+1)

    def is_bi(v, c):
        color[v] = c
        for to in E[v]:
            if color[to] == c: return False
            if color[to] == 0 and not is_bi(to, -c): return False
        return True

    if is_bi(1, 1):
        x = color.count(1)
        output = x * (N - x) - M
    else: output = N * (N - 1) // 2 - M
    print(output)

    return

if __name__ == '__main__':
    main()
