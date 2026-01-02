import sys
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    # まずは最大公約数を求める
    G = gcd(A, B)

    # 最大公約数を素因数分解して素因数の数を求める
    result = factorizer(G)
    print(result)


# ユークリッド互除法
def gcd(a, b):
    # print("a:{0},b:{1}".format(a, b))
    if b == 0:
        return a
    return gcd(b, a % b)


def factorizer(n):
    """
    素因数分解するということは、
    2 ~ Nまでの数で割り続けるということ　試し割り
    割れなくなったら次の数で割る。
    素数を除いて、素因数の最大値は√nなので、それを超えたらやめる
    """
    res = {1: 1}  # １は必ずある
    calcEnd = n ** 0.5

    for i in range(2, int(calcEnd) + 2, 1):
        while n % i == 0:
            if res.get(i) is None:
                res[i] = 1
            else:
                res[i] += 1
            n /= i
            # print("n:{0}".format(n))

    # GCDが素数だった時の処理
    if n > 1:
        res[int(n)] = 1

    # print("res is {}".format(res))
    return len(res)


if __name__ == '__main__':
    main()
