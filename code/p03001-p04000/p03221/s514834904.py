import sys
import collections
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M = ZZ()
    a = collections.defaultdict(list)
    id = [''] * (M+1)
    for i in range(M):
        p, y = ZZ()
        a[p].append([y, i+1])
    for key in a.keys():
        a[key].sort()
        for j, al in enumerate(a[key], 1):
            y, i = al
            id[i] = '{:0=6}'.format(key) + '{:0=6}'.format(j)
    for i in range(1, M+1): print(id[i])

    return

if __name__ == '__main__':
    main()
