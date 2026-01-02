import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque
from collections import defaultdict
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
    ans = 0
    s_dict = defaultdict(list)
    for ix, c in enumerate(s):
        s_dict[c].append(ix)
    cur_ix = -1 
    for counter, c in enumerate(t):
        if s_dict.get(c) == None:
            print(-1)
            return
        char_ix_list = s_dict.get(c)
        # cur_ixより大きい値を見つける
        pos = bisect.bisect_right(char_ix_list, cur_ix)
        # cur_ixより大きい値がないとき、リセット
        if pos >= len(char_ix_list):
            ans += len(s)
            cur_ix = char_ix_list[0]
        # cur_ixより大きい値が見つかった時、cur_ixを更新
        else:
            cur_ix = s_dict.get(c)[pos]
        # if last, add cur_ix to answer
        if counter == len(t)-1:
            ans += (cur_ix + 1)
    print(ans)
main()
