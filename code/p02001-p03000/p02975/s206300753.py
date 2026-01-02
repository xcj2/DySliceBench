from sys import exit
import sys
def input():
    return sys.stdin.readline()[:-1]
N = int(input())
A = list(map(int, input().split()))

def noexit():
    print('No')
    exit()

def yesexit():
    print('Yes')
    exit()

setA = set(A)
if 0 in setA:
    if len(setA) == 1: yesexit()
    elif len(setA) == 2 and N%3 == 0:
        A.sort()
        listA = list(setA)
        listA.remove(0)
        neww_list = [0] * (N//3) + [listA[0]] * ((N//3)*2)
        neww_list.sort()
        if A == neww_list:
            yesexit()
        else:
            noexit()
    else: noexit()

if N%3 != 0: noexit()
if len(setA) != 3: noexit()

listA = list(setA)
if listA[0]^listA[1] == listA[2]:
    new_list = [listA[0]]*(N//3) + [listA[1]]*(N//3) + [listA[2]]*(N//3)
    A.sort()
    new_list.sort()
    if A == new_list:
        yesexit()
    else:
        noexit()
else: noexit()