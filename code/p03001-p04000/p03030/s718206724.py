import sys
input = sys.stdin.readline
inf = float('inf')
mod = 10**9+7


def INT_(n): return int(n)-1


def MI(): return map(int, input().split())


def MF(): return map(float, input().split())


def MI_(): return map(INT_, input().split())


def LI(): return list(MI())


def LI_(): return [int(x) - 1 for x in input().split()]


def LF(): return list(MF())


def LIN(n: int): return [input() for _ in range(n)]


def LLIN(n: int): return [LI() for _ in range(n)]


def LLIN_(n: int): return [LI_() for _ in range(n)]


def LLI(): return [list(map(int, l.split())) for l in input()]


def I(): return int(input())


def F(): return float(input())


def ST(): return input().replace('\n', '')


def main():
    N = I()
    #city = []
    city = set()
    sp = []
    for i in range(N):
        i += 1
        s, p = input().split()
        p = int(p)
        sp.append([s, p, i])
        city.add(s)
    city = list(city)
    city.sort()
    ans = [[] for i in range(len(city))]
    sp.sort(reverse=True, key=lambda x: x[1])
    for s, p, i in sp:
        for j, c in enumerate(city):
            if s == c:
                ans[j].append(i)

    for a in ans:
        print(*a, sep="\n")


if __name__ == '__main__':
    main()
