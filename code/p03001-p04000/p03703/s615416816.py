from itertools import accumulate

def main():
    N, K, *A = map(int, open(0).read().split())

    B = [0] + list(accumulate(a - K for a in A))

    memo = {n: i for i, n in enumerate(sorted(set(B)), 1)}

    N += 1
    tree = [0] * (N + 1)

    def bit_sum(i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def bit_add(i, x):
        while i <= N:
            tree[i] += x
            i += i & -i

    ans = 0
    for b in map(memo.get, B):
        ans += bit_sum(b)
        bit_add(b, 1)

    print(ans)

if __name__ == '__main__':
    main()
