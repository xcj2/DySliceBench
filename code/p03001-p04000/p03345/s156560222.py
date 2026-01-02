def matmul(p, q):
    r = len(p)
    c = len(q[0])
    ret = []
    for i in range(r):
        row = []
        for j in range(c):
            v = 0
            for k in range(len(q)):
                v += p[i][k] * q[k][j]
            row.append(v)
        ret.append(row)
    return ret

def matpow(p, n):
    if n == 1:
        return p
    rsq = matpow(p, n // 2)
    rr = matmul(rsq, rsq)
    if n % 2 == 0:
        return rr
    else:
        return matmul(rr, p)


def main():
    a, b, c, k = map(int, input().split())
    ans = (a - b) * (1 if (k % 2 == 0) else -1)
    if abs(ans) <= 10 ** 18:
        print(ans)
    else:
        print("Unfair")


if __name__ == '__main__':
    main()
