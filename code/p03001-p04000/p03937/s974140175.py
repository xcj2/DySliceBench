#!/usr/bin/env python3
import sys
import copy
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    H,W = MAP()
    S = [input() for _ in range(H)]
    answerLabel = [[S[i][j]=="#" for j in range(W)] for i in range(H)]

    def dfs(cur,isVisited):
        i,j = cur
        isVisited[i][j] = True
        v = copy.deepcopy(isVisited)
        v2 = copy.deepcopy(isVisited)
        
        if i == H-1 and j == W-1:
            if isVisited == answerLabel:
                print("Possible")
                sys.exit()
            return
        if i+1<H:
            dfs((i+1,j),v)
        
        if j+1<W:
            dfs((i,j+1),v2)
    
    dfs((0,0),[[False]*W for _ in range(H)])

    print("Impossible")
    return

if __name__ == '__main__':
    main()
