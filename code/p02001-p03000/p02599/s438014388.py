# Coding is about expressing your feeling and there is always a better way to express your feeling _feelme
import sys,math
#sys.stdin,sys.stdout=open('input.txt','r'),open('output.txt','w')
from sys import stdin,stdout;mod=int(1e9 + 7);from statistics import mode
from collections import *;from math import ceil,floor,inf,factorial,gcd,log2,sqrt
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
# print('{:.3f}'.format(1),round(1.123456789,4))
# np.set_printoptions(sign=' ',legacy='1.13') # legacy add space at sign position
# sys.setrecursionlimit(500000)


# code here ----->
MAX = 500001

# structure to store queries
class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

# updating the bit array
def update(idx, val, bit, n):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

# querying the bit array
def query(idx, bit, n):
    summ = 0
    while idx:
        summ += bit[idx]
        idx -= idx & -idx
    return summ

def answeringQueries(arr, n, queries, q):

    bit = [0] * (n + 1)

    last_visit = [-1] * MAX

    ans = [0] * q

    query_counter = 0
    for i in range(n):
        if last_visit[arr[i]] != -1:
            update(last_visit[arr[i]] + 1, -1, bit, n)
        last_visit[arr[i]] = i
        update(i + 1, 1, bit, n)

        while query_counter < q and queries[query_counter].r == i:
            ans[queries[query_counter].idx] =  query(queries[query_counter].r + 1, bit, n) -  query(queries[query_counter].l, bit, n)
            query_counter += 1
    for i in range(q):
        print(ans[i])

if __name__ == "__main__":
    n,q=iia()
    a=iia()
    queries=[]
    for i in range(q):
        aa,bb=iia()
        aa-=1
        bb-=1
        queries.append(Query(aa,bb,i))
    queries.sort(key = lambda x: x.r)
    answeringQueries(a, n, queries, q)
