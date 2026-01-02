import sys
import math
from collections import defaultdict, deque
from copy import deepcopy
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
def end_of_loop():raise StopIteration
    
    
def main():
    N = I()
    A = [0]*N
    B = [0]*N
    if N == 0:
        sys.exit()
    for i in range(N):
        a, b = MI()
        A[i] = a
        B[i] = b

    D = Init(N, N, 0)
    #tableの初期化
    for num1 in range(N-1):
        num2 = num1+1
        a,b,c = A[num1], B[num1], B[num2]
        D[num1][num2] = a*b*c
        D[num2][num1] = a*b*c

    for length in range(2, N):
        for num1 in range(N-length):
            num2 = num1+length
            #num1からnum2-1までの組み合わせで最小値を求める
            a = A[num1]
            c = B[num2]
            result = float('inf')
            for num3 in range(num1, num2):
                result = min(result, a*B[num3]*c + D[num1][num3] + D[num3+1][num2])
            D[num1][num2] = result
            D[num2][num1] = result
    print(D[0][N-1])
            
if __name__ == "__main__":
    main()
