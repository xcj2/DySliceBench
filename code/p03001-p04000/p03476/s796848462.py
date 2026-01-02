def main():
    q = int(input())
    p_s = primes()
    is_like_2017 = is_like_2017_function(p_s)

    counter = 0

    memo = [0] * (10**5+1)

    for i in range(0, 10**5+1):
        if is_like_2017(i):
            counter += 1
        memo[i] = counter

    for _ in range(q):
        l, r = map(int, input().split(' '))
        print(memo[r] - memo[l-1])


def is_like_2017_function(primes):
    def _f(num):
        if primes[num] and primes[(num+1)//2]:
            return True
        else:
            False
    return _f


def primes():
    MAX = 10**5+1
    result = [True] * MAX
    result[0] = False
    loop_max = int(MAX**0.5) + 1
    for i in range(loop_max):
        if result[i]:
            for j in range((i+1)*2 - 1, MAX, (i+1)):
                if (j+1) % (i+1) == 0:
                    result[j] = False
    return [False] + result


if __name__ == '__main__':
    main()
