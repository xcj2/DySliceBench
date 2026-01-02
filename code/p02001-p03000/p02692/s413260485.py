# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def greedy(first, second, ch1, ch2):
    global ans
    if (first < second):
        first += 1
        second -= 1
        ans.append(ch1)
    else:
        first -= 1
        second += 1
        ans.append(ch2)
    return first, second

n,a,b,c = MAP()

ans = []
flag = 0

queries = []

for _ in range(n):
    queries.append(input())

for _ in range(n):
    zz = queries[_]
    if(zz=='AB'):
        if(a==b==0):
            flag = 1
            break
        if(a==b==1):
            foo = 0
            for j in range(_+1, n):
                if(queries[j]=="AC"):
                    a+=1
                    b-=1
                    ans.append("A")
                    foo = 1
                    break
                elif(queries[j]=="BC"):
                    b+=1
                    a-=1
                    foo = 1
                    ans.append("B")
                    break
            if(foo==0):
                a+=1
                b-=1
                ans.append("A")
        else:
            a,b = greedy(a, b,"A","B")

    elif(zz=="AC"):
        if (a == c == 0):
            flag = 1
            break
        if (a == c == 1):
            foo = 0
            for j in range(_ + 1, n):
                if (queries[j] == "BC"):
                    a -= 1
                    c+= 1
                    ans.append("C")
                    foo = 1
                    break
                elif (queries[j] == "AB"):
                    c-= 1
                    a += 1
                    foo = 1
                    ans.append("A")
                    break
            if (foo == 0):
                a += 1
                c -= 1
                ans.append("A")
        else:
            a, c = greedy(a, c,"A","C")
    else:
        if (b == c == 0):
            flag = 1
            break
        if (b == c == 1):
            foo = 0
            for j in range(_ + 1, n):
                if (queries[j] == "AB"):
                    c -= 1
                    b+= 1
                    ans.append("B")
                    foo = 1
                    break
                elif (queries[j] == "AC"):
                    c+= 1
                    b-= 1
                    foo = 1
                    ans.append("C")
                    break
            if (foo == 0):
                b += 1
                c -= 1
                ans.append("B")
        else:
            b, c = greedy(b, c, "B", "C")


if(flag==1):
    print("No")
else:
    print("Yes")
    for el in ans:
        print(el)


'''
6 9 1
AC
BC
AB
BC
AC
BC
AB
AB
C
C
A
C
C
C
B
A


5 9 2
5 8 3
6 7 3
6 6 4
5 6 5
5 5 6
6 4 6





'''