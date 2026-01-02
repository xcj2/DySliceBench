#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(X: int):
    def eratos(n :int):
        isPrimeList = [True] * (n+1)
        isPrimeList[0] = isPrimeList[1] = False
        
        for i in range(2, int(n**0.5+1)):
            if(isPrimeList[i]):
                j = i+i
                while(j <= n):
                    isPrimeList[j] = False
                    j = j+i
                    
        return isPrimeList

    t = eratos(10**6)
    # print(t[:10])
    l = [i for i,v in enumerate(t) if t[i] == True] 
    
    for i in l:
        if i >= X:
            print(i)
            exit()
            
    

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
