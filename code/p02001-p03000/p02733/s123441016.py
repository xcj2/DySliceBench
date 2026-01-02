import math
import time
from collections import deque
from collections import defaultdict
from copy import deepcopy
import heapq

mod = 10 ** 9 + 7
t = time.time()



def iip():
    ret = [int(i) for i in input().split()]
    if len(ret) == 1:
        return ret[0]
    return ret


def conbination(n, r, mod):
    if n < r:
        return 0

    if r == 0 or n == 0:
        return 1

    ret = 1
    for i in range(n-r+1, n+1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r+1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    #print(f"conbination {n}, {r} = {ret}")
    return ret

def inv(n, mod):
    return power(n, mod-2)

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p//2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod

def main():
    H, W, K = iip()

    chocos = []
    for i in range(H):
        chocos.append(input())


    result = 9999
    for i in range(2**(H-1)):
        hbin = bin(i)[2:].zfill(H-1)

        lines = []
        cur = []
        for i in range(H):
            cur.append(i)
            if i <= H-2 and hbin[i] == "1":
                lines.append(cur)
                cur = []
        lines.append(cur)
        cnum = cracknum(lines, W, K, chocos) + hbin.count("1")
        result = min(result, cnum)

    print(result)

def cracknum(lines, W, K, chocos):
    volumes = [0 for i in lines]
    result = 0
    for x in range(W):
        crack = False
        for line, y_list in enumerate(lines):
            for y in y_list:
                if chocos[y][x] == "1":
                    volumes[line] += 1
                    #print(y, x)
                    #print(volumes)
                    if volumes[line] > K:
                        crack = True
                        #print("crack")
                        break
            if crack:
                break

        if crack:
            result += 1
            volumes = [0 for i in lines]
            for line, y_list in enumerate(lines):
                for y in y_list:
                    if chocos[y][x] == "1":
                        volumes[line] += 1
                        if volumes[line] > K:
                            return 9999
    #print(result)
    return result





main()