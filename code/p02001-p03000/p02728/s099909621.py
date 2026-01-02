def main():
    import sys
    from collections import deque

    input = sys.stdin.readline
    sys.setrecursionlimit(1000000)

    n = int(input())
    f = 0

    E = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
        if len(E[a-1]) > n // 10 or len(E[b-1]) > n // 10:
            f = 1

    mod = 10 ** 9 + 7
    N = n + 1

    #逆元テーブル
    inv_t = [0]+[1]
    for i in range(2, N):
        inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

    #階乗計算
    kai = [1, 1]
    rev_kai = [1, inv_t[1]]
    for i in range(2, N):
        kai.append(kai[-1] * i % mod)
        rev_kai.append(rev_kai[-1] * inv_t[i] % mod)

    # コンビネーション計算
    def cmb(n, r):
        if n == 0 or r == 0:
            return 1
        else:
            return kai[n] * rev_kai[r] * rev_kai[n-r] % mod

    down = [{} for i in range(n+1)]
    up = [0 for i in range(n+1)]
    down_sum = [0 for i in range(n)]
    down_mul = [{} for i in range(n)]

    def dfs_down(cur, pre):
        if E[cur] == [pre]:
            down[pre][cur] = [1, 1]
        ns = []
        cnt = 1
        ns_append = ns.append
        for e in E[cur]:
            if e != pre:
                if e not in down[cur]:
                    dfs_down(e, cur)
                ni, cnti = down[cur][e]
                ns_append(ni)
                cnt = cnt * cnti % mod
        s = sum(ns)
        S = s
        for ni in ns:
            cnt = cnt * cmb(s, ni) % mod
            s -= ni
        down[pre][cur] = [S+1, cnt]
    
    def preprocess():
        for i in range(n):
            ns = []
            cnt = 1
            cnts = []
            l = [1]
            r = [1]
            cnts_append = cnts.append
            ns_append = ns.append
            l_append = l.append
            r_append = r.append
            downi = down[i]
            downmuli = down_mul[i]
            for e in downi:
                ni, cnti = downi[e]
                ns_append(ni)
                cnts_append(cnti)
            for j in range(len(cnts)):
                l_append(l[-1] * cnts[j] % mod)
                r_append(r[-1] * cnts[-j-1] % mod)
            for j, e in enumerate(downi):
                if len(r) >= 2:
                    downmuli[e] = l[j] * r[-j-2] % mod
                else:
                    downmuli[e] = 1

            s = sum(ns)
            S = s
            for ni in ns:
                cnt = cnt * cmb(s, ni) % mod
                s -= ni
            down_sum[i] = [S, cnt, l[-1]]
    
    def dfs_up_preprocess(cur, pre):
        stack = deque([[cur, pre]])
        while stack:
            cur, pre = stack.pop() 
            if cur != 0:
                ni = 0
                cnt = 1
                if up[pre]:
                    ni, cnt = up[pre]
                # 自分以外の子について計算
                # あらかじめ積をとっておけば、毎回for 文回さなくて良い
                n_cur, cnt_cur = down[pre][cur]
                n_sum, cnt_sum, _ = down_sum[pre]
                cnt = cnt * down_mul[pre][cur] % mod
                cnt = cnt * cnt_sum % mod
                cnt = cnt * kai[n_sum - n_cur] % mod
                cnt = cnt * kai[n_cur] % mod
                cnt = cnt * rev_kai[n_sum] % mod
                cnt = cnt * cmb(n_sum-n_cur+ni, ni) % mod
                s = n_sum-n_cur+ni

                up[cur] = [s+1, cnt]
            for e in E[cur]:
                if e != pre:
                    stack.append([e, cur])

    def dfs_up(cur, pre):
        stack = deque([[cur, pre]])
        while stack:
            cur, pre = stack.pop() 
            if cur != 0:
                ns = []
                cnt = 1
                ns_append = ns.append
                if up[pre]:
                    ni, cnti = up[pre]
                    ns_append(ni)
                    cnt = cnt * cnti % mod
                bros = down[pre]
                for bro in bros:
                    if bro != cur:
                        ni, cnti = bros[bro]
                        ns_append(ni)
                        cnt = cnt * cnti % mod
                s = sum(ns)
                S = s
                for ni in ns:
                    cnt = cnt * cmb(s, ni) % mod
                    s -= ni
                up[cur] = [S+1, cnt]
            for e in E[cur]:
                if e != pre:
                    stack.append([e, cur])


    if f:
        dfs_down(0, n)
        preprocess()
        dfs_up_preprocess(0, n)


        for i in range(n):
            ni = 0
            cnt = 1
            if up[i]:
                ni, cnt = up[i]
            n_sum, cnt_sum, cnt_all = down_sum[i]
            cnt = cnt * cnt_sum % mod
            cnt = cnt * cnt_all % mod
            cnt = cnt * cmb(n_sum + ni, ni) % mod
            print(cnt)
    else:
        
        dfs_down(0, n)
        dfs_up(0, n)


        for i in range(n):
            ns = []
            cnt = 1
            ns_append = ns.append
            if up[i]:
                ni, cnti = up[i]
                ns_append(ni)
                cnt = cnt * cnti % mod
            for bro in down[i]:
                ni, cnti = down[i][bro]
                ns_append(ni)
                cnt = cnt * cnti % mod
            s = sum(ns)
            for ni in ns:
                cnt = cnt * cmb(s, ni) % mod
                s -= ni
            print(cnt)


if __name__ == '__main__':
    main()
