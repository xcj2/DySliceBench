import sys

sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    N, K = LI()
    T = []
    D = []
    TD = []
    [TD.append(LI()) for i in range(N)]
    TD = sorted(TD, key=lambda l:l[1], reverse=True)
    # 種類のカウントをもつ
    type_count_dict = {}
    base_point = 0
    type_bonus = 0
    remaining_items = []
    for idx, i in enumerate(TD):
        if not type_count_dict.get(i[0]):
            type_count_dict[i[0]] = 0
        if idx < K:
            if type_count_dict[i[0]] == 0:
                type_bonus += 1
            type_count_dict[i[0]] += 1
            base_point += i[1]
        else:
            if type_count_dict[i[0]] == 0:
                remaining_items.append(i[1])
                type_count_dict[i[0]] += 1

    S = TD[:K]
    result = base_point + type_bonus**2
    
    ridx = 0
    for idx, s in enumerate(S[::-1]):
        if len(remaining_items) < ridx + 1:
            break
        if len(remaining_items) == 0:
            break
        if type_count_dict[s[0]] >= 2:
            type_count_dict[s[0]] -= 1
            base_point += remaining_items[ridx] - s[1]
            type_bonus += 1
            ridx += 1
            result = max(type_bonus**2 + base_point, result)
    print(result)


if __name__ == '__main__':
    main()