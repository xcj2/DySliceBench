# Meet Arora

def fibonacci(n):
    f = [[1,1],[1,0]]
    if n==0:
        return 0
    f=power(n-1, f)
    return f[0][0]

def multiply(f, m):
    x = f[0][0]*m[0][0] + f[0][1]*m[1][0]
    y = f[0][0]*m[0][1] + f[0][1]*m[1][1]
    z = f[1][0]*m[0][0] + f[1][1]*m[1][0]
    w = f[1][0]*m[0][1] + f[1][1]*m[1][1]

    f[0][0] = x
    f[0][1] = y
    f[1][0] = z
    f[1][1] = w

    return f

def power(n, f):
    if n==0 or n==1:
        return f

    m = [[1,1], [1,0]]
    f=power(n//2, f)
    f=multiply(f,f)

    if n%2==1:
        f=multiply(f, m)

    return f

arr = [int(x) for x in input().split()]
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
k = int(arr[3])

if abs(a-b)>10**18:
    print("Unfair")
else:
    if k%2==0:
        print(a-b)
    else:
        print(b-a)




