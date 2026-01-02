n = int(input())
##実装ミスをあとでミスっていたことが分かるよう修正した結果a,b逆。
##要注意
b = list(map(int, input().split( )))
a = list(map(int,input().split( )))

#これでx考慮しなくてよくなる
a2 = [a[i]^a[i-1] for i in range(n)]
b2 = [b[i]^b[i-1] for i in range(n)]
b2 = b2+b2
#print(a2)
#print(b2)

#ローリングハッシュ
#https://tjkendev.github.io/procon-library/python/string/rolling_hash.html

base = 37; mod = 10**9 + 9
pw = None
def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    v = 0
    for i in range(l):
        h[i+1] = v = (v * base + s[i]) % mod
    return h
# RH前に、必要な長さの最大値分のpow-tableを計算しておく
def setup_pw(l):
    global pw
    pw = [1]*(l + 1)
    v = 1
    for i in range(l):
        pw[i+1] = v = v * base % mod
def get(h, l, r):#lは含まない
    return (h[r] - h[l] * pw[r-l]) % mod

setup_pw(n*2)
bh = rolling_hash(b2)
ah = rolling_hash(a2)
ans = []

get_a = get(ah,0,n)
for k in range(n):
    if get(bh,k,k+n) == get_a:
        ans.append(k)
for k in ans:
    x = b[k]^a[0]
    print(k,x)
