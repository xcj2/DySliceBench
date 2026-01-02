from collections import deque
from copy import copy,deepcopy
from itertools import permutations,combinations
from pprint import pprint

def myinput():
    return map(int,input().split())

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)

k = int(input())

def bfs(k):
    ls = []
    q = deque()
    for i in range(1,10):
        q.append(str(i))
    while q:
        tmp = q.popleft()
        ls.append(tmp)
        if len(ls)==k:
            break
        n = int(tmp[-1])
        if n==0:
            tmp_new = tmp + "0"
            q.append(tmp_new)
            tmp_new = tmp + "1"
            q.append(tmp_new)
        elif 0<n<9:
            tmp_new = tmp + str(n-1)
            q.append(tmp_new)
            tmp_new = tmp + str(n)
            q.append(tmp_new)
            tmp_new = tmp + str(n+1)
            q.append(tmp_new)
        elif n==9:
            tmp_new = tmp + "8"
            q.append(tmp_new)
            tmp_new = tmp + "9"
            q.append(tmp_new)
        else:
            print("Error")
    return ls

ls = bfs(k)
# print(ls)
print(ls[k-1])