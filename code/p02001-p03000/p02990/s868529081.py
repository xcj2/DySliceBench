n, k = map(int,input().split())

# m,nに対してm^(-1) mod n を求める
def reciprocal(m, n):
# p < q ならpをqで割った余りを求める
    if (m > n):
        m = m % n
    a0 = n
    a1 = m
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while (a1 != 0):
        q = a0 // a1
        r = a0 % a1
        x2 = x0 - q * x1
        y2 = y0 - q * y1
        a0 = a1
        a1 = r
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
    if (a0 !=1):
        print("法除算に失敗しました")
    while (y0 < 0):
      y0 += n
    return(y0)

# 各iに対して、(k-1)!/{(k-i)!(i-1)!} * (n-k+1)!/{(n-k-i+1)!i!}を計算する
# 以前のiの答えをansに格納しておく
# i = 1の時は(n-k+1)となる
ans = (n-k+1) % (10**9+7)
# i * j mod (10**9+7)を計算する関数を作る
def modMulti(i,j):
  return(i*j % (10**9+7))
# i / j mod (10**9+7)を計算する関数を作る
# i< j なら(10**9+7 + i) / jとする必要がある
def modDiv(i,j):
  if i % j == 0:
    # ここを(i/j % (10**9+7))とすると何故かバグる
    return(i//j % (10**9+7))
  else:
    return(i * reciprocal(j, (10**9+7)) % (10**9+7))
print(ans)
if k > 1:
  for i in range(2, k+1):
    ans = modDiv(modMulti(modMulti(ans,k-i+1), n-k-i+2), modMulti(i-1,i))
    print(ans)