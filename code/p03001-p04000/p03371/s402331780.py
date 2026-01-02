#関数リスト
import sys
input = sys.stdin.readline


def RD(): return input().rstrip()
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))

def main():
    A, B, C, X, Y = MI()
    result = float('inf')
    result = min(result,int(A*X+B*Y))
    temp = min(X,Y)
    result = min(result,int(C*temp*2+(X-temp)*A+(Y-temp)*B))
    result = min(result, int(max(X, Y)*C*2))
    print(result)
    
    
if __name__ == "__main__":
    main()