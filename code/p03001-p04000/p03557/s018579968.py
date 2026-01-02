#関数リスト
import sys
import bisect
input = sys.stdin.readline
def RD(): return input().rstrip()
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]

def main():
    N = I()
    A = LI()
    A.sort()
    B = LI()
    B.sort()
    B_len = len(B)
    C = LI()
    C.sort()
    C_len = len(C)
    result = 0
    A_init = A[0]
    index = 0
    next_i = index
    
    for i in B:
        tempA = bisect.bisect_left(A,i) 
        tempC = C_len - bisect.bisect_right(C,i)
        result += tempA*tempC
    print(result)

if __name__ == "__main__":
    main()
