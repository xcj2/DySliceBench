import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array
from typing import List

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value


def partition(cards: List[Card], p: int, r: int) -> int:
    x = cards[r].value
    i = p - 1
    for j in range(p, r):
        if cards[j].value <= x:
            i += 1
            cards[i], cards[j] = cards[j], cards[i]
    cards[i + 1], cards[r] = cards[r], cards[i + 1]
    return i + 1


def quick_sort(cards: List[Card], p: int, r: int):
    if p < r:
        q = partition(cards, p, r)
        quick_sort(cards, p, q - 1)
        quick_sort(cards, q + 1, r)


def merge(cards: List[Card], left: int, mid: int, right: int):
    n1 = mid - left
    n2 = right - mid
    L, R = [Card('Z', 0)] * (n1 + 1), [Card('Z', 0)] * (n2 + 1)
    for i in range(n1):
        L[i] = cards[left + i]
    for i in range(n2):
        R[i] = cards[mid + i]

    L[n1] = Card('Z', float('INF'))
    R[n2] = Card('Z', float('INF'))

    i, j = 0, 0
    for k in range(left, right):
        if L[i].value <= R[j].value:
            cards[k] = L[i]
            i += 1
        else:
            cards[k] = R[j]
            j += 1


def merge_sort(cards: List[Card], left: int, right: int):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(cards, left, mid)
        merge_sort(cards, mid, right)
        merge(cards, left, mid, right)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A, B = [], []
    for n in range(N):
        suit, value = sl()
        A.append(Card(suit, int(value)))
        B.append(Card(suit, int(value)))

    # ソート
    quick_sort(A, 0, N - 1)
    merge_sort(B, 0, N)

    # 回答
    for a, b in zip(A, B):
        if a.suit != b.suit or a.value != b.value:
            print('Not stable')
            break
    else:
        print('Stable')
    for a in A:
        print(a.suit, a.value)


if __name__ == '__main__':
    main()

