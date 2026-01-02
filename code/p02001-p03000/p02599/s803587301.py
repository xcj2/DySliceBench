import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    bit = [0] * (N+1)

    def add(x, a):
        while x <= N:
            bit[x] += a
            x += x & -x

    def sum(x):
        ret = 0
        while x != 0:
            ret += bit[x]
            x -= x & -x
        return ret

    c = list(map(int, input().split()))
    lr = [None] * Q
    for i in range(Q):
        l, r = map(int, input().split())
        lr[i] = (i, l, r)
    lr.sort(key=lambda x: x[2])
    ans = [None] * Q
    last_idx = [-1] * (N+1)
    j = 0
    for i, l, r in lr:
        while j < r:
            if last_idx[c[j]] == -1:
                last_idx[c[j]] = j
            else:
                add(last_idx[c[j]]+1, -1)
                last_idx[c[j]] = j
            add(j+1, 1)
            j += 1
        ans[i] = sum(r) - sum(l-1)
    for a in ans:
        print(a)
            
if __name__ == "__main__":
    main()