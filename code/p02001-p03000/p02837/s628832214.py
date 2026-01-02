#!python3

def resolve():
    N = int(input().rstrip())
    A = []

    ok = dict()
    ng = dict()
    for i in range(N):
        a = []
        for j in range(int(input().rstrip())):
            x, y = map(int, input().rstrip().split())
            a.append((x, y))

        A.append(a)

    def cbit(n):
        i = 0
        while n:
            if n & 1:
                i += 1
            n >>= 1
        return i

    def check(i, t):
        for x, y in t:
            ii = i & (1 << (x-1))
            if y == 1:
                if ii == 0: return False
            else:
                if ii != 0: return False
        return True

    n = -1
    for i in range(2**N-1, -1, -1):
        n0 = cbit(i)
        if n0 <= n: continue

        for j in range(N):
            k = 1 << j
            if not i & k:
                continue
            if not check(i, A[j]):
                break
        else:
            n = n0
    print(n)


if __name__ == "__main__":
    resolve()
