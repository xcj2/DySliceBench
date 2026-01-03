import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import copy
from collections import deque

class SegTree():
    def __init__(self, n):
        self.value = [0 for i in range(n*2)]

MOD = 10 ** 9 + 7

def getinvmod(n):
    return [pow(i, MOD-2, MOD) for i in range(n+1)]

def judge(monsters, n_attack, a, b):
    attack = 0
    for monster in monsters:
        # monster -= n_attack * b
        if monster > 0:
            attack += math.ceil(max(0, (monster - b*n_attack)/(a-b)))

    return attack <= n_attack


def main():
    n, a, b = getList()
    monsters = []
    for i in range(n):
        monsters.append(getN())

    mn = 0
    mx = 10 ** 15
    while(mx - mn > 1):
        mid = (mn + mx) // 2
        if judge(monsters, mid, a, b):
            mx = mid
        else:
            mn = mid
        # print(monsters)

    if judge(monsters, mn, a, b):
        print(mn)
    else:
        print(mx)



if __name__ == "__main__":
    main()