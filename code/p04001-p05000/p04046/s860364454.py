from functools import reduce
import math

memo = []
memo_inv = []
MOD = 10**9+7
    
def get_factorial(i):
    return memo[i]

def get_factorial_inv(i):
    return memo_inv[i]

def nCr(n, r):
    return get_factorial(n) * get_factorial_inv(n-r) * get_factorial_inv(r)

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    
    slist = input().rstrip().split(' ')
    H = int(slist[0])
    W = int(slist[1])
    A = int(slist[2])
    B = int(slist[3])
    global memo
    memo = [1]*(H+W+1)
    f= 1
    for i in range(1,H+W+1):
        f *=i
        f %=MOD
        memo[i] = f
        
    global memo_inv
    memo_inv = [1]*(H+W+1)
    memo_inv[H+W] = pow(memo[H+W],MOD-2,MOD)
    f_inv = memo_inv[H+W]
    for i in range(H+W-1,0,-1):
        f_inv *= i +1
        f_inv %= MOD
        memo_inv[i] = f_inv
        
    ans = 0
    for i in range(B,W):
        ans += nCr(i+H-A-1,i) * nCr(W-i-1+A-1,A-1)
    print(ans % MOD)
    
if __name__ == '__main__':
    main()
