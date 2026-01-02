def solve(N, Hs):
    def split(s, e):
        d = []
        for i in range(s, e):
            if Hs[i] != 0 and len(d) % 2 == 0:
                d.append(i)
            elif Hs[i] == 0 and len(d) % 2 == 1:
                d.append(i)
        if len(d) % 2 == 1:
            d.append(e)

        return [(d[2 * i], d[2 * i + 1]) for i in range(len(d) // 2)]

    def f(s, e):

        ans = 0
        if s >= len(Hs) or s > e:
            return 0
        if s == e:
            return Hs[s]
        m = min(Hs[s:e])
        c = Hs[s:e].count(0)
        if len(Hs[s:e]) == c:
            return 0
        if m == 0:
            l = split(s, e)
            for ss, ee in l:
                ans += f(ss, ee)
        else:
            ans += m
            for i in range(s, e):
                Hs[i] -= m
            ans += f(s, e)
        return ans

    return f(0, N)

if __name__ == "__main__":
    N = int(input())
    Hs = list(map(int, input().split(" ")))
    print(solve(N, Hs))
