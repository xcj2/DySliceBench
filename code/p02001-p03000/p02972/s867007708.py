import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

import collections

def solve():
    N = int(input())
    a_list = list(map(int, input().split()))

    y_dict = collections.defaultdict(list)

    # 約数dictの自分の倍数のところに自分を入れる
    for i in range(1, N//2+2):
        cnt = 2
        while True:
            baisu = i * cnt
            y_dict[baisu].append(i)
            cnt += 1
            if baisu > N:
                break

    dprint(y_dict)
    bits = collections.defaultdict(int)
    ans = []
    # 逆順で見ていき、約数listに入っているもののbitを反転させる
    for i in range(N, 0, -1):

        a = a_list[i-1]
        dprint(a, bits[i])
        if a == bits[i]:
            continue
        for y in y_dict[i]:
            bits[y] = (bits[y] + 1) % 2
        ans.append(i)


    print(len(ans))
    print(' '.join([str(num) for num in reversed(ans)]))

solve()