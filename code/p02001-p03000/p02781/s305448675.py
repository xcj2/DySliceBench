# -*- coding: utf-8 -*-

def main():
    n = input()
    k = int(input())

    print(tmp(n, k))

def tmp(x, k):
    # k が 桁数以上の場合、パターンなし
    if len(x) < k:
        return 0
    # k が 0 の場合、全て 0 の 1パターン
    if k <= 0:
        return 1
    if len(x) == k == 1:
        return int(x)
    else:
        int_x = list(map(int, list(x)))
        next_x = str(int(x[1:]))

        # 最大桁を k の 1つとする場合、最大値の場合と それ以外の場合で計算が異なる。
        a = tmp(next_x, k-1)
        # 最大値, 0 以外の場合は、以下の桁は全ての値を取り得る
        b = (int_x[0]-1) * pow(9, k-1) * combination(len(x)-1, k-1)
        # 最大桁を k の 1つとしない場合（最大桁を0とみなす）
        c = pow(9, k) * combination(len(x)-1, k)

        return a + b + c

def combination(n, k):
    m = 1
    l = 1
    for i in range(n, n-k, -1):
        m = m * i

    for j in range(k, 0, -1):
        l = l * j
    
    return int(m / l)

if __name__ == "__main__":
    main()
