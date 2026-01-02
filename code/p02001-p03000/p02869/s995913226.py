import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N,K = map(int,read().split())

def solve_even(N,K):
    L = N//2
    x = np.arange(K,K+N)
    y = np.concatenate([np.arange(K+L+N,K+L+N+L),np.arange(K+N,K+L+N)])
    add = N-(K+L)
    z = x + y + add
    z[L:] += 1
    answer = np.vstack([x,y,z]).T
    print('\n'.join(' '.join(row) for row in answer.astype(str)))

def solve_odd(N,K):
    L = N//2
    x = np.arange(K,K+N)
    y = np.concatenate([np.arange(K+L+N,K+L+N+L+1),np.arange(K+N,K+L+N)])
    add = N-(K+L)
    z = x + y + add
    answer = np.vstack([x,y,z]).T
    print('\n'.join(' '.join(row) for row in answer.astype(str)))

def solve(N,K):
    if K+K > N+1:
        print(-1)
        return
    if N&1:
        solve_odd(N,K)
    else:
        solve_even(N,K)

solve(N,K)