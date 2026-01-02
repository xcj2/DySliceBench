import sys
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

def check(mid, k, pairs):
    tmp = 0
    for pair in pairs:
        a,b = pair
        kari_a = mid // b
        tmp += max(a - kari_a, 0)

    if tmp <= k:
        return True
    else:
        return False


def solve():
    n, k = getList()
    cap = getList()
    foods = getList()
    cap.sort()
    foods.sort(reverse=True)
    h = []
    pairs = [(a, b) for a, b in zip(cap, foods)]
    ansmn = 0
    ansmx = 10**13
    # print(foods)
    # print(cap)
    # print([2046//p for p in foods])
    while(ansmx - ansmn > 1):
        mid = (ansmn + ansmx) // 2
        res = check(mid, k, pairs)
        if res:
            ansmx = mid
        else:
            ansmn = mid


    if check(ansmn, k, pairs):
        print(ansmn)
    else:
        print(ansmx)

def main():
    solve()


if __name__ == "__main__":
    main()


"""
10 10
95 38 9 26 36 10 69 25 44 83
6 42 33 74 75 31 73 20 70 93
"""