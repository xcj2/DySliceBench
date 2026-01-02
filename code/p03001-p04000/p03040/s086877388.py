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
    from heapq import heappush, heappushpop, heappop
    Q = I()
    # highはそのままheapq
    high = []
    # lowは一番デカイのを取り出せるように符号逆転して、heapq
    low = []

    _, a, b = MI()
    heappush(low, -a)

    debug = [a]

    # debug用
    def solve(n):
        ans = 0
        for a in debug:
            ans += abs(a - n)

        return B + ans

    B = b
    ans = 0
    cnt = 1
    for _ in range(Q - 1):
        inp = input()
        if inp[0] == "1":
            _, a, b = map(int, inp.split())
            B += b
            debug.append(a)
            cnt += 1

            # 偶数なら答えを更新してから、heapqを更新
            if cnt % 2 == 0:
                ans += abs(-low[0]-a)
                even = True
            else:
                even = False

            # lowに入れるかhighに入れるか
            if a > -low[0]:
                heappush(high, a)
            else:
                heappush(low, -a)

            # 中央値がわかるように平衡化
            if len(low) < len(high):
                heappush(low, -heappop(high))
            elif len(low) > len(high) + 1:
                heappush(high, -heappop(low))

            # 奇数ならheapqを更新してから答えを更新
            if not even:
                ans += abs(-low[0] - a)

        else:
            print(-low[0], ans + B)
            #print(-low[0], solve(-low[0]))
        #print(sorted(debug), low, high, ans)
    # print(sorted(debug))


if __name__ == '__main__':
    main()
