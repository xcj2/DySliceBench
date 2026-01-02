# -*- coding: utf-8 -*-
import sys
from itertools import permutations
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    mx=[1,1,-1,-1]
    my=[1,-1,1,-1]
    def check(tmp_board):
        for y,x in enumerate(tmp_board):
            d=[1,1]
            for j in range(7):
                for k in range(4):
                    c=[y+d[0]*my[k],x+d[1]*mx[k]]
                    if 0<=c[0]<=7 and 0<=c[1]<=7 and tmp_board[c[0]]==c[1]:
                        return False
                d[0]+=1
                d[1]+=1
        return True
    
    
    k=int(input())
    c=[['.']*8 for _ in range(8)]
    for i in range(k):
        R,C=map(int,input().split())
        c[R][C]='Q'
    yoko=list(range(8))
    tate=list(range(8))
    board=[-1]*8
    try:
        for y,l in enumerate(c):
            for x,s in enumerate(l):
                if s=='Q':
                    tate.remove(y)
                    yoko.remove(x)
                    board[y]=x
        for p in permutations(yoko):
            tmp_board=board[:]
            for i,x in enumerate(tate):
                tmp_board[x]=p[i]
            if check(tmp_board):
                for x in tmp_board:
                    ans=['.']*8
                    ans[x]='Q'
                    print(''.join(ans))
                break
        else:
            raise Exception
    except:
        print('No Answer')

if __name__ == '__main__':
    main()

