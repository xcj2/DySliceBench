import functools

N,M = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*N

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def multiple(a, b):
    return a*b // euclid(a, b)

def lcm(nums):
        return functools.reduce(multiple, nums)

def count_two(n):
    c = 0
    while n%2 ==0:
        c += 1
        n //= 2
    return c

l = [0]*N
for i in range(N):
    l[i] = count_two(a[i])

if len(set(l)) != 1:
    print(0)
else:
    p_2 = l[0] #2で何回割れるか
    for i in range(N):
        b[i] = a[i] // (2**p_2)
    
    X = lcm(b)*(2**(p_2-1))
    nax = M // X

    print((nax+1)//2)