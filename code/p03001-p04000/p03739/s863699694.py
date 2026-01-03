import math


"""
e.g. N=3 a=[-1 1 1]
 -1 2  1 :1
 -1 2 -2 :4

e.g. N=3 a=[0 0 -1]
 1  0 -1 :1
 1 -2 -1 :3
 1 -2  2 :6

 -1 0 -1 :1
 -1 2 -1 :3
 -1 2 -2 :4

e.g. N=3 a=[0 0 1]
 1  0 1 :1
 1 -2 1 :3
 1 -2 2 :4

 -1 0  1 :1
 -1 2  1 :3
 -1 2 -2 :6

e.g. N=4 a=[0 0 0 -1]
 1  0 0 -1 :1
 1 -2 0 -1 :3
 1 -2 2 -1 :5
 1 -2 2 -2 :6

 -1 0  0 -1 :1
 -1 2  0 -1 :3
 -1 2 -2 -1 :5
 -1 2 -2  2 :8

e.g. N=4 a=[0 0 0 1]
 1  0 0  1 :1
 1 -2 0  1 :3
 1 -2 2  1 :5
 1 -2 2 -2 :8

 -1 0  0 1 :1
 -1 2  0 1 :3
 -1 2 -2 1 :5
 -1 2 -2 2 :6
"""


def main2():
    """
    累積和は、偶奇,奇偶のどちらかの数列になるので２種類試す
    """
    n = int(input())
    A = list(map(int, input().split()))

    ans = float("inf")
    for sign in (1, -1):
        s, n_op = 0, 0
        for a in A:
            s += a
            # if sign == 1 and s <= 0:
            # elif sign == -1 and s >= 0:
            if s * sign <= 0:
                # 調整
                n_op += abs(s) + 1
                s = sign

            # 偶奇の入れ替え
            sign *= -1

        ans = min(ans, n_op)

    print(ans)


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    # 最初から0続きのとき、操作が少なくなるように同じ符号にする
    def sign(x):
        if x == 0:
            return 0
        return int(math.copysign(1, x))

    if a[0] == 0:
        for i in range(1, n):
            if a[i] != 0:
                sign_a = sign(a[i])
                if i % 2 == 0:
                    # odd: 1-indexed
                    a[0] = sign_a
                else:
                    a[0] = -sign_a

                ans += 1
                break
    s = a[0]

    for i in range(1, n):
        s1 = s + a[i]
        sign_s = sign(s)
        sign_s1 = sign(s1)

        if s1 == 0 or sign_s == sign_s1:
            # 逆方向に変更
            # new_s1 = -sign_s = s+a[i] + diff
            diff = -(sign_s + s + a[i])
            a[i] += diff
            ans += abs(diff)

        s += a[i]

        #print(i, a, sep="\t")
    print(ans)

if __name__ == '__main__':
    main2()
