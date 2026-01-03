def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))
# import sys
# input = sys.stdin.readline

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

N=one_int()

dicts={}
for i in range(2,N+1):
    lists = factorization(i)
    for item in lists:
        if item[0] != 1:
            if item[0] in dicts:
                dicts[item[0]] += item[1]
            else:
                dicts[item[0]] = item[1]

div=10**9 + 7
ans=1

for k,v in dicts.items():
    ans *= (v+1)%div

print(ans%div)