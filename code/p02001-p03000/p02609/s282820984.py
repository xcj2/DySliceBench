def solve():
    N = int(input())
    X = input()
    X_10 = int(X,2)

    r = X.count("1")
    r0 = r-1
    r1 = r+1
    ans = []
    
    s0 = X_10 % r0 if r != 1 else None
    s1 = X_10 % r1 

    for i in range(N):
        if X[i] == '0':
            ans.append(f((s1 + pow(2,N-1-i,r1)) % r1))
        else:
            if r0 == 0:
                ans.append(0)
            else:
                ans.append(f((s0 - pow(2,N-1-i,r0)) % r0))
    
    print(*ans, sep='\n')

def f(N):
    cnt = 1
    while N != 0:
        N = N % popcount(N)
        cnt += 1
    
    return cnt

def popcount(N):
    b = bin(N)
    cnt = 0
    for i in range(2,len(b)):
        if b[i] == '1':
            cnt += 1

    return cnt

if __name__ == '__main__':
    solve()