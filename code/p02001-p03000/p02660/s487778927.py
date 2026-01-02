import sys
from math import floor
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
    N = int(input())
    if N== 1:
        print(0)
        return
    
    arr = factorization(N)
    ans = 0
    for p, i in arr:
        num = 0
        while num * (num + 1) // 2 <= i: num += 1
        ans += num - 1
    print(ans)

    

if __name__ == "__main__":
    main()
