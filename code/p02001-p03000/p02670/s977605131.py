#!/usr/bin/env python3
import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    n = INT()
    P = LI()
    cost = [[min(i, n-i-1, j, n-j-1) for j in range(n)] for i in range(n)]
    issit = [[True for _ in range(n)] for _ in range(n)]
    ans = 0

    for p in P:
        i,j = divmod(p-1,n)
        issit[i][j] = False
        ans += cost[i][j]

        q = [(i, j, cost[i][j])]
        while q:
            n_i, n_j, cur_cost = q.pop()

            if n_i > 0 and cost[n_i-1][n_j] > cur_cost:
                cost[n_i-1][n_j] = cur_cost
                q.append((n_i-1,n_j,cur_cost+issit[n_i-1][n_j]))

            if n_i < n-1 and cost[n_i+1][n_j] > cur_cost:
                cost[n_i+1][n_j] = cur_cost
                q.append((n_i+1,n_j,cur_cost+issit[n_i+1][n_j]))

            if n_j > 0 and cost[n_i][n_j-1] > cur_cost:
                cost[n_i][n_j-1] = cur_cost
                q.append((n_i,n_j-1,cur_cost+issit[n_i][n_j-1]))
 
            if n_j < n-1 and cost[n_i][n_j+1] > cur_cost:
                cost[n_i][n_j+1] = cur_cost
                q.append((n_i,n_j+1,cur_cost+issit[n_i][n_j+1]))
    print(ans)

if __name__ == '__main__':
    main()