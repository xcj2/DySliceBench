import sys
sys.setrecursionlimit(100000)

def ins(): return input().split()
def ii(): return int(input())
def iil(): return list(map(int, ins()))
def lin(): return list(input())
def iin(): return map(int, ins())

import copy
n = ii()
dic = {1: ['a']}
dic.update({i+2:[] for i in range(9)})
def getnext(dic):
    tmp = {i+1:[] for i in range(10)}
    for i, v in dic.items():
        for j in v:
            for k in range(i+1):
                if i == k:
                    tmp[i+1].append(j+chr(k+0x61))
                else:
                    tmp[i].append(j+chr(k+0x61))
    return tmp
for i in range(n-1):
    dic = getnext(dic)
tmp = []
for i in range(10):
    tmp += dic[i+1]
tmp.sort()
for i in tmp:
    print(i)