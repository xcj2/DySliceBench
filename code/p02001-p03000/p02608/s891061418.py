def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()

def solve(n):
    ret = {i:[] for i in range(n+1)}
    X=int(n**(1/2) +0.5)+1
    Y=int(n**(1/2) +0.5)+1 
    Z=int(n**(1/2) +0.5)+1
    for x in range(1,X):
        for y in range(1,Y):
            d = x**2+y**2+x*y
            for z in range(1,Z):
                if n < d+z**2 + y*z + z*x:
                    continue
                ret[d+z**2 + y*z + z*x].append((x,y,z))
    return ret

ret = solve(N)
for i in range(1,N+1):
    print(len(set(ret[i])))