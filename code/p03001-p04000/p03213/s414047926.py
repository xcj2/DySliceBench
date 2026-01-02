def factorize_factorial(n):
    # 階乗の素因数分解
    e = [0] * 101
    for k in range(2, n + 1):
        divisor = 2
        cnt = 0
        while k % divisor == 0:
            k //= divisor
            cnt += 1
        if cnt > 0:
            e[divisor] += cnt

        divisor = 3
        while k > 1:
            cnt = 0
            while k % divisor == 0:
                k //= divisor
                cnt += 1
            if cnt > 0:
                e[divisor] += cnt
            divisor += 2
    return e


def count(k, e):
    # 素因数分解テーブルからべき数k以上の要素数を求める
    return len(tuple(filter(lambda x: x >= k, e)))


def main():
    n = int(input())
    e = factorize_factorial(n)

    ans = 0
    ans += count(75 - 1, e)
    ans += count(25 - 1, e) * (count(3 - 1, e) - 1)
    ans += count(15 - 1, e) * (count(5 - 1, e) - 1)
    ans += count(5 - 1, e) * (count(5 - 1, e) - 1) * (count(3 - 1, e) - 2) // 2

    print(ans)


if __name__ == '__main__':
    main()
