#: Author - Soumya Saurav
import sys,io,os,time
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect,math,heapq
alphabet = "abcdefghijklmnopqrstuvwxyz"

input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)


########################################
n , m = map(int , input().split())
g = defaultdict(list)
uf = UnionFind(n)
for i in range(m):
	u,v = map(int , input().split())
	u-=1
	v-=1
	uf.union(u,v)
check = set()
for i in range(n):
	check.add(uf.find(i))
print(len(check) - 1)







'''
# Wrap solution for more recursion depth
#submit as python3
import collections,sys,threading
sys.setrecursionlimit(10**9)
threading.stack_size(10**8)



threading.Thread(target=solve).start()
'''
