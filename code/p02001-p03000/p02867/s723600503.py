#!/usr/bin/env python
# coding: utf-8

from collections import Counter
def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    la = rli()
    lb = rli()
    lab = []
    for i in range(n):
        lab.append([la[i], lb[i]])

    la.sort()
    lb.sort()
    for i in range(n):
        if la[i] > lb[i]:
            print("No")
            return

    # aでsort
    lab.sort()
    # print(lab)
    for i in range(n):
        lab[i].append(i)
    # bでsort
    lab.sort(key=lambda x: x[1])
    # print(lab)
    length = 1
    fr = 0
    to = lab[0][2]
    while to != 0:
        fr = to
        to = lab[fr][2]
        length += 1
    # cycleが二つ以上ある場合
    if length < n:
        print("Yes")
        return

    # 隣どうしをswapしてcycle二つにできる場合
    for i in range(n-1):
        if lb[i] >= la[i+1]:
            print("Yes")
            return
    
    # どうしようもない場合
    print("No")


if __name__ == '__main__':
    main()
