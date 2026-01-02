def fib(n):
    if n == 0: 
        return 0

    if n == 1: 
        return 1

    def matmul(M1, M2):
        a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
        a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
        a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
        a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
        return [[a11, a12], [a21, a22]]

    def matPower(mat, p):
        if p == 1: 
            return mat

        m2 = matPower(mat, p//2)
        if p % 2 == 0:
            return matmul(m2, m2)
        else: 
            return matmul(matmul(m2, m2),mat)

    Q = [[1,1],[1,0]]

    q_final = matPower(Q, n-1)
    return q_final[0][0]

N, M = map(int, input().split())
if(M==0):
    print(fib(N+1)%1000000007)
else:
    V = []
    for x in range(M):
        V.append(int(input()))

    result = 1

    for i in range(1, M):
        if(V[i]-V[i-1]==1):
            result = 0

    result *= fib(V[0])

    for x in range(1, M):
        result *= fib(V[x]-V[x-1]-1)

    if(V[M-1]!=N):
        result *= fib(N-V[M-1])

    print(result%1000000007)