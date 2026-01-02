#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import itertools


def main():
    S=input()
    
    def calc(L):
        temp=int(S[0])
        for i in range(3):
            a=1
            if L[i]==0:
                a=-1
            temp+=int(S[i+1])*a
        return temp
    
    ans=S[0]
    for ite in itertools.product([0,1], repeat=3):
        if calc(ite)==7:
            for i in range(3):
                if ite[i]==1:
                    ans+="+"
                else:
                    ans+="-"
                ans+=S[i+1]
            break
    print(ans+"=7")
    
            
        
    

main()
