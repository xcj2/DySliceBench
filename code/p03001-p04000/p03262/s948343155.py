def gcd(a, b):
    if a > b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


def allgcd(d):
    if len(d) == 1:
        return d
    ret_gcd = d[0]
    for i in d:
        ret_gcd = gcd(ret_gcd, i)
    return ret_gcd


def maxNumVisitCity(N, X, x):
    if len(x) == 1:
        return abs(x[0] - X)

    d = []
    for i in x:
        d.append(abs(i - X))
    return allgcd(d)


def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    print(maxNumVisitCity(N, X, x))


if __name__ == '__main__':
    main()
