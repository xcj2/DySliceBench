import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    def sum_of_floor(N,M,A,B):
        """
        return sum_{i=0}^{N-1} (A*i+B)//M
        """
        S = 0
        while N:
            q,A = divmod(A,M)
            S += N * (N-1) // 2 * q
            q,B = divmod(B,M)
            S += N * q
            if not A:
                return S
            y = (A * N + B) // M
            x = M * y - B
            S += (N - (x+A-1)//A) * y
            N,M,A,B = y,A,M,(-x)%A
        return S
    
    T=I()
    for _ in range(T):
        n,m,a,b=MI()
        print(sum_of_floor(n,m,a,b))



main()
