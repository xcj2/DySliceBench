import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque
import pdb

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    s = S()
    t = S()
    cands = []
    ans = 'z' * 50
    for st_ix in range(len(s)):
        i = st_ix 
        cur_j = 0
        copy_s_list = list(s)
        is_cand = False 
        while cur_j < len(t) and st_ix + len(t) - 1< len(s):
            if s[i] == t[cur_j] or s[i] == '?':
                copy_s_list[i] = t[cur_j]
                cur_j += 1
                i += 1
                if cur_j == len(t):
                    is_cand = True
            else:
                break

        if is_cand: 
            for ix in range(len(copy_s_list)):
                if copy_s_list[ix] == '?':
                    copy_s_list[ix] = 'a'
            cands.append(''.join(copy_s_list))
    if cands == []:
        print("UNRESTORABLE")
    else:
        print(min(cands))

            
main()

