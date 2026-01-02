import math;

def swap(a,b):
    return (b,a)

def gcd(a,b):
    if (a<b):
        a,b = swap(a,b)
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def main():
    n,m = map(int,input().split())
    X = [x for x in map(int,input().split())]
    if n>=m:
        print(0)
        return
    X.sort()
    X_dif = []
    for i in range(1,m):
        X_dif.append([abs(X[i]-X[i-1]),i])
    ans = 0
    X_dif.sort()
    X_dif.reverse()
    index = [0]
    for i in range(n-1):
        index.append(X_dif[i][1])
    for i in range(1,n):
        ans += X[index[i]-1] - X[index[i-1]]
    ans += X[-1]-X[index[-1]]
    print(ans)
    return

if __name__ == '__main__':
    main()