import math

def read():
    N, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    F = list(map(int, input().strip().split()))
    return N, K, A, F

def solve(N, K, A, F):
    A = list(sorted(A))
    F = list(reversed(sorted(F)))
    mul = [A[i] * F[i] for i in range(N)]
    smul = list(sorted(mul)) + [9999999999]
    
    def f(x):
        k = 0
        for i in range(N):
            if x < mul[i]:
                k += math.ceil((mul[i] - x) / F[i])
        return k
    
    lb = 0
    ub = 10 ** 12
    while lb < ub:
        x = lb + (ub - lb) // 2
        if f(x) > K:
            # K回の修行では足りない
            lb = x+1
        else:
            ub = x
    return lb

if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
