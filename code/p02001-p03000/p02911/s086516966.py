# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
# 入力を整数に変換して受け取る
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, input().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n, k, q = MI()
    A = [II() for _ in range(q)]

    ini = k-q
    point = [ini for _ in range(n)]
    for a in A.copy():
        point[int1(a)] += 1

    for p in point:
        print('Yes' if p > 0 else 'No')


if __name__ == '__main__':
    solve()
