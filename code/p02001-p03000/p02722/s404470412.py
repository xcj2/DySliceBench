def divisor(N:int):
    res = set()
    i = 1
    while i * i <= N:
        if N % i == 0:
            res.add(i)
            if i != N // i:
                res.add(N // i)
        i += 1
    return res

def check(N:int, K:int):
    while N % K == 0:
        N //= K
    return True if N % K == 1 else False

def main():
    N = int(input())

    ans = set()
    for K in divisor(N):
        if K == 1: continue
        if check(N, K):
            ans.add(K)

    ans |= divisor(N - 1)

    ans.remove(1)

    print(len(ans))

if __name__ == "__main__":
    main()