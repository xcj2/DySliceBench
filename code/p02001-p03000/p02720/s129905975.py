def ith(N,i):
    # print(N, i, (N % (10 ** (i+1))) // 10 ** i)
    return (N % (10 ** (i+1))) // 10 ** i
def next(N):
    if N < 10:
        return N+1
    if ith(N,0) == 9:
        up = next(N//10)
        # print(up)
        if ith(up,0) == 0:
            return up * 10 + ith(up,0)
        else:
            return up * 10 + ith(up,0) - 1
    if ith(N,0) == ith(N,1) + 1:
        up = next(N//10)
        if ith(up,0) == 0:
            return up * 10 + ith(up,0)
        else:
            return up * 10 + ith(up,0) - 1
    return N + 1


def main():
    K = int(input())
    ans = 1
    for i in range(K-1):
        ans = next(ans)
    print(ans)
main()