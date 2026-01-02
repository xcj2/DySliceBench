#!python3

import sys

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N, Q = iim()
    val = 2**31-1

    A, S, i = [], [],  N
    while i > 1:
        i += i & 1
        A.append([val] * i)
        i >>= 1
    A.append([val])
    la = len(A)

    def update(i, x):
        i0 = i
        x0 = A[0][i]
        diff = x0 - x
        if diff == 0:
            return
        A[0][i] = x
        if diff > 0:
            for j in range(1, la):
                i, i0 = i >> 1, i
                y = A[j][i]
                if x >= y:
                    break
                A[j][i] = x
            return

        for j in range(0, la-1):
            y = A[j][i^1]
            if x >= y:
                x = y
            i >>= 1
            if A[j+1][i] == x:
                break
            A[j+1][i] = x


    def find(s, t):
        i, ans = 0, val
        while t - s > 1:
            if s & 1:
                ans = min(ans, A[i][s])
                s += 1
            if t & 1 == 0:
                ans = min(ans, A[i][t])
                t -= 1
            s, t , i= s // 2, t // 2, i + 1
            #print(s, t)

        return min(A[i][s], A[i][t], ans)


    for com, *arg in (map(int, line.split()) for line in sys.stdin):
        if com == 0:
            update(*arg)
        else:
            #for i,a in enumerate(A):
            #    print("*", " "*i*2,  *a)
            #print(*arg)
            res = find(*arg)
            print(res)

if __name__ == "__main__":
    resolve()

