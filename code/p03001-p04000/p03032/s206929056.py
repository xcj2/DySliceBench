#!/usr/bin/env python3.4

# abc128_d

def get_right(l, r):
    return l[-r:] if r!=0 else []

def main():
    # Input
    n, k = [int(s) for s in input().split()]
    vs = [int(s) for s in input().split()]
    # Get ans
    R = min(n, k)
    def gene_lr():
        for i in range(1, R+1):
            for j in range(i+1):
                yield(i-j, j)
    def gene_tv():
        for l, r in gene_lr():
            tv = 0
            pps = []
            for v in vs[:l] + vs[n-r:]:
                tv += v
                if v<0:
                    pps.append(v)
            s = k-(l+r)
            pps.sort()
            yield tv-sum(pps[:s])
    ans = max(gene_tv())
    # Output
    print(ans)

if __name__ == '__main__':
    main()

