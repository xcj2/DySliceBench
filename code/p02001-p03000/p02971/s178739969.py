from math import sqrt

def solve0(N, A):
    S = sorted(A)
    S0 = S[-1]
    S1 = S[-2]

    for a in A:
        if a == S0:
            print(S1)
        else:
            print(S0)

def solve(N, A):
    D = int(sqrt(N))
    M = []
    for i in range(0, N, D):
        M.append(max(A[i:i+D]))
    M.append(0)
    for i in range(0, N):
        d = i // D
        l = d*D
        m = 0
        for j in range(l, min(l+D, N)):
            if i != j and A[j] > m:
                m = A[j]
        m0 = m
        if d == 0:
            m = max(m, max(M[d+1:]))
        elif d >= len(M) - 1:
            m = max(m, max(M[:d]))
            pass
        else:
            #print(d, len(M))
            #print("M[:d]", M[:d])
            #print("M[d+1:]", M[d+1:])
            m = max(m, max(M[:d]), max(M[d+1:]))
        print(m)
        #print("d=%d,"%d, m, max(A[:i]+A[i+1:]))
        #assert m == max(A[:i]+A[i+1:])


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    solve0(N, A)

#l = list(range(1, 200))
#solve(len(l), l)
main()
