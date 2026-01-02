import bisect

# https://docs.python.org/ja/3/library/bisect.html

DBG = False

def find_lt(a, x):
    i = bisect.bisect_left(a, x)
    if i:
        return i-1, a[i-1]
    else:
        return 0, a[0]

def readlist(n):
    return list(map(int, (input() for _ in range(n))))

def main():
    A, B, Q = map(int, input().split(' '))
    S = readlist(A)
    T = readlist(B)
    X = readlist(Q)
    if DBG: print(S)
    if DBG: print(T)
    def get_right(lst, left, x):
        if lst[left] > x:
            # x is smaller than lst[0]
            return left, lst[left]
        right = left + 1
        if right < len(lst):
            return right, lst[right]
        else:
            # x is bigger than lst[-1]
            return left, lst[left]
    def print_status(sl_i, sl_v, sr_i, sr_v, tl_i, tl_v, tr_i, tr_v):
        def tostr(i, v):
            return str(i) + " (" + str(v) + ")"
        print("S: " + tostr(sl_i, sl_v), tostr(sr_i, sr_v),
                " T: " + tostr(tl_i, tl_v), tostr(tr_i, tr_v))
    def solve(x):
        if DBG: print("Q:", x)
        sl_i, sl_v = find_lt(S, x)
        sr_i, sr_v = get_right(S, sl_i, x)
        tl_i, tl_v = find_lt(T, x)
        tr_i, tr_v = get_right(T, tl_i, x)
        if DBG: print_status(sl_i, sl_v, sr_i, sr_v, tl_i, tl_v, tr_i, tr_v)
        def distance(p0, p1):
            # first, go to p0 from x.
            d = abs(p0 - x)
            # second, goto p1 from p0.
            d = d + abs(p1 - p0)
            if DBG: print(p0, p1, "->", d)
            return d
        # choose l->l l->r r->l r->r
        #        l<-l l<-r r<-l r<-r
        dists = []
        dists.append(distance(sl_v, tl_v))
        dists.append(distance(tl_v, sl_v))
        dists.append(distance(sl_v, tr_v))
        dists.append(distance(tl_v, sr_v))
        dists.append(distance(sr_v, tl_v))
        dists.append(distance(tr_v, sl_v))
        dists.append(distance(sr_v, tr_v))
        dists.append(distance(tr_v, sr_v))
        if DBG: print(dists)
        return min(dists)
    for x in X:
        print(solve(x))

main()
