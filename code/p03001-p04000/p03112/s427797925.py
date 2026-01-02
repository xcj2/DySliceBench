import bisect

A, B, Q = map(int, input().split())
s = [None] * A
t = [None] * B
x = [None] * Q

for i in range(A):
    s[i] = int(input())
for i in range(B):
    t[i] = int(input())
for i in range(Q):
    x[i] = int(input())

s.sort()
t.sort()

def calc(s, t, x):
    len_s = len(s)
    len_t = len(t)

    def f_nishi_pos(l, x):
        p1 = bisect.bisect_left(l, x)
        #p2 = bisect.bisect_right(l, x)
        #if p2 == len(l):
        #    return p1-1
        #if l[p1] == l[p2]:
        #    return max(p2-1, 0)
        #else:
        #    return p1
        if p1 == len(l):
            return p1 - 1
        else:
            if l[p1] == x:
                return p1
            else:
                return p1 - 1

    def f_higashi_pos(l, x):
        #p1 = bisect.bisect_left(l, x)
        p2 = bisect.bisect_right(l, x)
        #if p1 == len(l):
        #    return p1-1
        #if l[p1] == l[p2]:
        #    return min(p1, len(l)-1)
        #else:
        #    return p1
        if p2 == len(l):
            return p2 - 1
        else:
            return p2

    # 神社 -> 寺
    ## 西の神社
    j_nishi_pos = f_nishi_pos(s, x)
    j_nishi = s[j_nishi_pos]
    ## 東の神社
    j_higashi_pos = f_higashi_pos(s, x)
    j_higashi = s[j_higashi_pos]

    ## 西の神社の西の寺
    j_nishi_t_nishi_pos = f_nishi_pos(t, j_nishi)
    j_nishi_t_nishi = t[j_nishi_t_nishi_pos]
    ## 西の神社の東の寺
    j_nishi_t_higashi_pos = f_higashi_pos(t, j_nishi)
    j_nishi_t_higashi = t[j_nishi_t_higashi_pos]
    ## 東の神社の西の寺
    j_higashi_t_nishi = t[f_nishi_pos(t, j_higashi)]
    ## 東の神社の東の寺
    j_higashi_t_higashi = t[f_higashi_pos(t, j_higashi)]


    # 寺 -> 神社
    t_nishi = t[f_nishi_pos(t, x)]
    t_higashi = t[f_higashi_pos(t, x)]
    
    ## 西の寺の西の神社
    t_nishi_j_nishi = s[f_nishi_pos(s, t_nishi)]
    ## 西の寺の東の神社
    t_nishi_j_higashi = s[f_higashi_pos(s, t_nishi)]
    ## 東の寺の東の神社
    t_higashi_j_nishi = s[f_nishi_pos(s, t_higashi)]
    ## 東の寺の東の神社
    t_higashi_j_higashi = s[f_higashi_pos(s, t_higashi)]


    return min(
        abs(x - j_nishi) + abs(j_nishi - j_nishi_t_nishi),
        abs(x - j_nishi) + abs(j_nishi - j_nishi_t_higashi),
        abs(x - j_higashi) + abs(j_higashi - j_higashi_t_nishi),
        abs(x - j_higashi) + abs(j_higashi - j_higashi_t_higashi),
        abs(x - t_nishi) + abs(t_nishi - t_nishi_j_nishi),
        abs(x - t_nishi) + abs(t_nishi - t_nishi_j_higashi),
        abs(x - t_higashi) + abs(t_higashi - t_higashi_j_nishi),
        abs(x - t_higashi) + abs(t_higashi - t_higashi_j_higashi)
    )

for xx in x:
    print(calc(s, t, xx))