# D - 2017-like Number
# https://atcoder.jp/contests/abc084/tasks/abc084_d

counts = []
counts.append(0)
counts.append(0)
counts.append(0)

prime = []

is_prime = []
is_prime.append(False)
is_prime.append(False)

def sieve(r):
    for i in range(2, r + 1):
        is_prime.append(True)

    for i in range(2, r + 1):
        if is_prime[i]:
            prime.append(i)

            j = 2 * i
            while j <= r:
                is_prime[j] = False
                j = j + i

def calc_like_number_count(r):
    for i in range(3, r + 1):
        if i % 2 == 1 and is_prime[i] and is_prime[(i + 1) // 2]:
            counts.append(1)
        else:
            counts.append(0)
    
    for i in range(3, r + 1):
        counts[i] = counts[i] + counts[i - 1]


def main():
    Q = int(input())
    querys = []
    max_r = 0
    for i in range(Q):
        l, r = map(int, input().split())
        querys.append((l, r))
        if max_r < r:
            max_r = r

    sieve(max_r)
    calc_like_number_count(max_r)

    for l, r in querys:
        print(counts[r] - counts[l - 1])
    
main()