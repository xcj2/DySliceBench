#!/usr/bin/env python3
import sys
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    S = input()
    answer = len(S)-1

    def is_even(s):
        if len(s)&1:
            return False
        
        half_length = len(s)//2
        if s[:half_length] == s[half_length:]:
            return True
        else:
            return False
    
    while True:
        S = S[:-1]
        if is_even(S):
            print(len(S))
            return
        
        answer -= 1
    return

if __name__ == '__main__':
    main()
