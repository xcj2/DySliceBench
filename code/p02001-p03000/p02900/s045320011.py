# 入力を2つの数値として扱う
a, b = map(int, input().split())

# 最大公約数を求める関数(ユークリッド互除法)
def gcd(i, j):
    while j != 0:
        i, j = j, i % j
    return i

# 公約数のリストを返す関数(最大公約数の約数)
def divisor(n):
    i = 1
    ret = []
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            ret.append(n//i)
        i += 1
    ret = list(set(ret))
    ret.sort()
    return ret

# 互いに素(最大公約数が1)の場合Trueを返す関数
def coprime(i, j):
    return gcd(i, j) == 1

# 最大公約数を求める
g = gcd(a, b)

# 公約数のリストを求める
dl = divisor(g)

# 公約数を調べる
cnt = 1
# 1より大きい約数について
while cnt < len(dl):
    lc = 1
    # 次の約数と比較
    while cnt + lc < len(dl):
        # for debug:print(str(dl[cnt]) + ',' + str(dl[cnt + lc]))
        # 素でない場合は削除
        if not coprime(dl[cnt], dl[cnt + lc]):
            dl.remove(dl[cnt + lc])
            lc -= 1
        lc += 1
    cnt += 1

# 答えの出力
print(len(dl))