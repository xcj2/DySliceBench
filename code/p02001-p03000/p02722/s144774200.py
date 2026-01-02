import sys
sys.setrecursionlimit(10**7)
n = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append((i, cnt))

    if temp!=1:
        arr.append((temp, 1))

    if arr==[]:
        arr.append((n, 1))

    return arr

def get_divisors(num):
    f_divs, l_divs = [], []
    for i in range(1, int(num**0.5)+1):
        if not num % i:
            f_divs.append(i)
            if i != num // i:
                l_divs.append(num // i)
    return f_divs + l_divs[::-1]

f = factorization(n)
num, cnt = zip(*f)
ans = len(get_divisors(n-1))-1

def dfs(idx, x):
    nx = x
    if idx >= len(num):
        if x == 1: return
        k = n
        while k % x == 0: k //= x
        if (k-1) % x == 0:
            global ans
            ans += 1
        return

    for i in range(cnt[idx]+1):
        dfs(idx+1, nx)
        nx *= num[idx]

dfs(0, 1)
print(ans)
