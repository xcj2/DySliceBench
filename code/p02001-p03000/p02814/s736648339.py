# 問題文：長さNの偶数からなる正の整数列A=a1,a2,...,aNと、整数Mが与えられます。
#        任意のk(1≤k≤N)に対して以下の条件を満たす正の整数XをAの「半公倍数」と定義します。
#        X=ak×(p+0.5)を満たす負でない整数pが存在する。
#        1以上M以下の整数のうちのAの半公倍数の個数を求めてください。
# 入力 : 以下の形式で標準入力から与えられる。
#       N M
#       a1 a2 ... aN
# 出力 : 1 以上 M 以下の整数のうちの A の半公倍数の個数を出力せよ。

# 半公倍数の個数を求める
def n_hankobaisu(M, min_hankobaisu):
    q = M // min_hankobaisu
    if q % 2 == 1:
        q += 1
    return int(q/2)

# nが何回2で割り切れるかを求める
def nankai_2de_warikireruka(n):
    i = 0

    # nは最大10^9 処理速度を上げるため、2^10で割る
    for i in range(0,99999999999):
        if n >= 1024 and n % 1024 == 0:
            n = n / 1024
            i += 10
        else:
            break

    for i in range(0,9999999999999999999):
        if n > 1:
            n, mod = divmod(n, 2)
            if mod == 1:
                break
                i += 1
        else:
            break

    return i

# 最小半公倍数を求める
def min_hankobaisu(A, M):
    result = 1
    for i in range(9999999999999):
        result = A[0] * (0.5 + i)

        if len(A) == 1:
            return result

        if result > M:
            print(0)
            exit(0)

        for j in range(1, len(A)):
            q, mod = divmod(result, A[j]/2)
            if q % 2 == 1 and mod == 0:
                # 数列要素すべての半公倍数であるので、最小半公倍数として返却する
                if j == len(A)-1:
                    return int(result)
                continue
            else:
                break # 半公倍数としてふさわしくないので、次の半公倍数候補を求める
    return int(result)

# 正の整数列Aの長さN, 半公倍数の上限M
N, M = map(int, input().split())

# 正の整数列A
A = list(set(list(map(int, input().split()))))
A.sort(reverse=True)
# hankobaisu_list = []

# 2で割り切れる回数が異なる→半公倍数はない
# → その場で終了
p = nankai_2de_warikireruka(A[0])

if N == 1:
    print(n_hankobaisu(M, min_hankobaisu(A, M)))
    exit(0)

for i in range(1, len(A)):
    pi = nankai_2de_warikireruka(A[i])
    if pi != p:
        print(0)
        exit(0)

# 半公倍数の最小値を求める

# 範囲内にいくつの半公倍数があるか求める
#print('最小半公倍数：{}'.format(min_hankobaisu))
#print(int(M/min_hankobaisu)//2 + 1)
print(n_hankobaisu(M, min_hankobaisu(A, M)))
