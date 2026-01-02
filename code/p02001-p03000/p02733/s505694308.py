def main():
    import sys
    inf = 100100100
    ans = inf
    H, W, K = map(int, input().split())
    S = [0]*H
    for i in range(H):
        S[i] = [int(x) for x in sys.stdin.readline().strip()]
    for i in range(2**(H-1)):
        group = [0]
        g = 0
        for j in range(H-1):
            if (i >> j) & 1:
                g += 1
            group.append(g)
        g += 1
        c = [[0 for _ in range(W)] for __ in range(g)]
        for j in range(H):
            for k in range(W):
                c[group[j]][k] += S[j][k]
        num = g-1
        now = [0]*g
        def large(now):
            for n in now:
                if n > K:
                    return True
            else:
                return False
        def v_vec(twodlis, k):
            ans = []
            for lis in twodlis:
                ans.append(lis[k])
            return ans
        for k in range(W):
            for n in range(len(now)):
                now[n] = now[n] + v_vec(c,k)[n]
            if large(now):
                now = v_vec(c,k)
                num += 1
                if large(now):
                    num = inf
                    break

        ans = min(ans, num)
    print(ans)

if __name__ == "__main__":
    main()
