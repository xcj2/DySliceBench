import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


K = I()

ans = []
def fn(n):
    ns = str(n)
    tail = int(ns[-1])
    if tail > 0:
        yield int(ns + str(tail - 1))
    yield int(ns + ns[-1])
    if tail < 9:
        yield int(ns + str(tail + 1))


for i1 in range(1, 10):
    ans.append(i1)
    for i2 in fn(i1):
        ans.append(i2)
        for i3 in fn(i2):
            ans.append(i3)
            for i4 in fn(i3):
                ans.append(i4)
                for i5 in fn(i4):
                    ans.append(i5)
                    for i6 in fn(i5):
                        ans.append(i6)
                        for i7 in fn(i6):
                            ans.append(i7)
                            for i8 in fn(i7):
                                ans.append(i8)
                                for i9 in fn(i8):
                                    ans.append(i9)
                                    for i10 in fn(i9):
                                        ans.append(i10)


ans.sort()
print(ans[K - 1])
