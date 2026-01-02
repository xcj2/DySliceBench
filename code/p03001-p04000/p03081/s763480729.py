def bisect(f, ok, err):
    while abs(ok - err) > 1:
        m = (ok + err) // 2
        if f(m):
            ok = m
        else:
            err = m
    return ok

def c2i(c): return ord(c)-ord("A")
def mapst(s,t): return c2i(s),-1 if t=="L" else 1
def main():
    N,Q=map(int, input().split())
    S=list(map(c2i, input()))
    TD=[mapst(*input().split())for _ in range(Q)]
    def f(m):
        for t,d in TD:
            m+=(S[m]==t)*d
            if m<0 or m>=N: return False
        return True
    l=bisect(f, N, -1)
    def f(m):
        for t,d in TD:
            m+=(S[m]==t)*d
            if m<0 or m>=N: return False
        return True
    r=bisect(f, -1, N)
    print(r-l+1 if l<=r else 0)

if __name__ == "__main__":
    main()