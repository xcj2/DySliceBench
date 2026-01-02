def main():
    N = list(map(int,input()))
    K = int(input())
    if len(N) < K :
        print(0)
    else:
        print(dfs(N, 0, K))
def test(N,K):
    return dfs(list(map(int,str(N))),0,K)

def comb(N, K):
    if N < K:
        return 0
    if K == 0:
        return 1
    elif K == 1:
        return N
    elif K == 2:
        return N * (N - 1) // 2
    elif K == 3:
        return N * (N - 1) * (N - 2) // 6


def dfs(N, pos, rest):
    if rest == 0:
        return 1
    if pos >= len(N):
        return 0
    ans = 0
    for i in range(10):
        if N[pos] > i:
            if i == 0:
                ans += comb(len(N) - pos - 1, rest) * (9**rest)
            else:
                ans += comb(len(N) - pos - 1, rest - 1) * (9 ** (rest-1))
        elif N[pos] == i :
            if i == 0 :
                ans += dfs(N, pos+1, rest)
            else :
                ans += dfs(N, pos+1, rest - 1)
        else:
            break
    return ans
if __name__ == "__main__":
    main()