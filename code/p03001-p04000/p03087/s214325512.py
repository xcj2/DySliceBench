from sys import stdin
import math
import itertools
import re
import sys
sys.setrecursionlimit(10**8)
 
 
def makeIntMatrix(lines):
    intMatrix = []
    for a in makeStringMatrix(lines):
        intMatrix.append([int(b) for b in a])
    return intMatrix
 
 
def makeStringMatrix(lines):
    stringMatrix = [line.split() for line in lines]
    return stringMatrix
 
 
def makeInt(line):
    return int(line.rstrip())
 
 
def makeMultiInteger(line):
    return [int(x) for x in line.rstrip().split()]
 
dp = {}
T = {}
 
def solve(input_string):
    N, Q = map(int, input_string[0].split())
    S = input_string[1]
    intMatrix = makeIntMatrix(input_string[2:])
    #print(input_string[2:])
    t=[0]*(N+1)
    for i in range(N):
        t[i + 1] = t[i] + (1 if S[i : i + 2] == 'AC' else 0)
    #for i in range(Q):
    for line in intMatrix:
        l, r = line
        #print(l, r)
        #print(S[l:r+1])
        #cnt = len(re.findall(r'AC', S[l-1:r]))
        #totalCnt = cntAC(L, R, S)
        totalCnt = t[r-1] - t[l-1]
        print(totalCnt)
    return
 

"""
wrong answer
def cntAC(l, r, D, S, cnt):
    global dp
    global T
    if r-l == D+1:
        return cnt
    if str(l)+str(r) not in T:
        T[str(l)+str(r)] = S[l-1:r]
        t = T[str(l)+str(r)]
    if str(l)+str(r) not in dp:
        #print(t)
        dp[str(l)+str(r)] = len(t.split('AC'))-1
        cnt = dp[str(l)+str(r)]
        return cntAC(l-1, r, D, S, cnt)
    else:
        cnt = dp[str(l)+str(r)]
        return cntAC(l-1, r, D, S, cnt)
"""
 

"""
wrong answer
def cntAC(L, r, S):
    global dp
    global T
    for l in range(L, r)[::-1]:
        if str(l)+str(r) not in T:
            T[str(l)+str(r)] = S[l-1:r]
            t = T[str(l)+str(r)]
        else:
            t = T[str(l)+str(r)]
        if str(l)+str(r) not in dp:
            dp[str(l)+str(r)] = len(t.split('AC'))-1
            cnt = dp[str(l)+str(r)]
        else:
            cnt = dp[str(l)+str(r)]
    return cnt
"""
 
def cntAC(L, R, S):
    cnt = 0
    for l in range(L, R):
        t = S[l-1:l+1]
        cnt +=  1 if t == 'AC' else 0
    return cnt

def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    #print(answer)
 
 
if __name__ == '__main__':
    main()
