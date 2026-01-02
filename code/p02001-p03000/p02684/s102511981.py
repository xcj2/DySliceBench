from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
#from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
#------------------------------------------------------------------
import sys
sys.setrecursionlimit(10**6)
from types import GeneratorType
#use:- put @bootstrap overrecursive function
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack:
            return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack:
                        break
                    call = stack[-1].send(call)
            return call
    return wrapped_function


n,k = mapi()
a = [0]+list(mapi())
gr = defaultdict(int)
for i in range(1,n+1):
    gr[i]=a[i]

vis ={}
path = []
p = 1

@bootstrap
def dfs(s):
    global p
    if s in vis:
        p = s
        yield 0
    path.append(s)
    vis[s] = 1
    res =0
    res+= yield dfs(gr[s])
    yield res
dfs(1)
i = 0
ln = 0
path2 = path[:]
while i<len(path):
    if p==path[i]:
        path2 = path2[i:]
        break
    i+=1
#print(path)
if k<len(path)-len(path2):
    print(path[k])
else:
    k -= len(path)-len(path2)
    print(path2[k%len(path2)])
#print(dfs(1,k))
