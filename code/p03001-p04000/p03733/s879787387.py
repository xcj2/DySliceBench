# coding: utf-8
import array, bisect, collections, heapq, itertools, math, random, re, string, sys, time
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
 
 
def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}
 
 
def solve(N, T, t):
    ans = 0
    t_dif = [t[i + 1] - t[i] for i in range(N - 1)]
    
    for i in t_dif:
        if i >= T:
            ans += T
        else:
            ans += i
    
    ans += T
    
    return ans

 
def main():
    N, T = ILI()
    t = ILI()
    print(solve(N, T, t))
 
 
if __name__ == "__main__":
    main()
