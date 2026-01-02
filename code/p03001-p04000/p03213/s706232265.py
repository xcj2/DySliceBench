# 10 -> [2,3,5,7]
def make_prime_list(k):
    p = [True] * (k+1)
    p[0] = False
    p[1] = False
    for i in range(2, k+1):
        if p[i]:
            for j in range(i*2, k+1, i):
                p[j] = False
    return [i for i in range(k + 1) if p[i]]


# 6 -> [[2,1],[3,1],[6,1]]
def get_prime_fact_dict(num):
    ps = make_prime_list(num//2)
    i = num
    prime_and_count = []

    for p in ps:
        count = 0
        while i % p == 0:
            i //= p
            count += 1
        if count > 0:
            prime_and_count.append([p, count])

    prime_and_count.append([num, 1])

    return prime_and_count


def solve(n):
    div_fact_count = [0] * (n+1)

    for i in range(2, n+1):
        xss = get_prime_fact_dict(i)
        for k, v in xss:
            div_fact_count[k] += v

    a = len([i for i in div_fact_count if i >= 74])
    b = len([i for i in div_fact_count if i >= 24])
    c = len([i for i in div_fact_count if i >= 14])
    d = len([i for i in div_fact_count if i >= 4])
    e = len([i for i in div_fact_count if i >= 2])

    # p**74
    c1 = a
    # p**24 * q**3
    c2 = b*(e-1)
    # p**14 ** q**4
    c3 = c * (d-1)
    # p**4 * q**4 * r*2
    # p and q are calculated as duplicated.
    c4 = (d * (d-1) * (e-2))//2

    return c1+c2+c3+c4


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
