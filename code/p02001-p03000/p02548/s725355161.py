#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def get_factor(N):
    N1 = N + 2
    A = [2, 0] * (N1//2)

    for i in range(3, N1, 2):
        if A[i]:
            continue
        for j in range(i, N1, 2*i):
            A[j] = i

    def factor(n):
        i = 0
        ans = []

        while n & 1 == 0:
            i += 1
            n >>= 1
        if i:
            ans.append((2, i))

        while n > 1:
            a = A[n]
            i = 1
            while True:
                n //= a
                b = A[n]
                if a != b:
                    ans.append((a, i))
                    b = a
                    break
                i += 1

        return ans


    return factor

def resolve():
    N = int(sys.stdin.readline())

    f = get_factor(N)

    ans = 0
    for i in range(1, N):
        num = 1
        #print(i, f(i))
        for a, b in f(i):
            num *= b + 1
        ans += num
    print(ans)
if __name__ == "__main__":
    resolve()
