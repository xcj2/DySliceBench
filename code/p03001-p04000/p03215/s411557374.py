#第5回 ドワンゴからの挑戦状 予選-B Sum AND Subarrays
"""
数列Aが与えられる。
整数kが与えられる。
数列Aの空でない部分列からk個取る。
各部分列の合計を"美しさ"と言う。
この時、k個すべての"美しさ"のbit andを取った時、最大値がいくつになるか
求めよ。
n <= 1000, k <= n*(n+1)//2

解法：
まず直感的に、すべての要素の合計sum(lst1)を使うとして良い。
また、回答は必ずこれ未満の値となる。
更に、andを用いることから、上位桁のbit積を優先して良い。

となると、結局大きい値が上位桁のbitも多いことから、
和が大きい順にk個取った時の論理積ということになる。

N<1000という制約から、n*(n+1)//2が愚直に間に合うので、これを
実装すれば良い。

WA:
下位桁を優先したほうが良い場合が存在する。
解説：
下位桁を優先する、のではなく、上位桁を満たすようなk個を用意できなかった場合、
次に下位の桁を探すという解き方をする必要がある。つまり、上位桁を優先にするのは
変わらず、その桁のbitが1であるようなものをどんどん絞っていく形になる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,k = map(int,readline().split())
lst1 = list(map(int,readline().split()))

def cumsum(lst): #元のリストを保持
    res = lst[:]
    for i in range(1,len(res)):
        res[i] += res[i-1]
    return res
def cumsumdif(l,r,lst): #求めたい差のインデックスを入れる
    if l == 0:
        return lst[r]
    else:
        return lst[r] - lst[l-1]
lst2 = cumsum(lst1)

lst3 = []

for i in range(n):
    for j in range(i,n):
        lst3.append(cumsumdif(i,j,lst2))

lst3.sort(reverse=True)

for i in range(40,-1,-1): #まず最上位桁について決定
    ct = 0
    res = []
    for j in lst3:
        if j>>i&1:
            ct += 1
            res.append(j)
    if ct >= k:
        m = i
        ans = pow(2,m)
        break

for i in range(m-1,-1,-1): #次に、上位桁からその桁においてandが1になるようなものを優先して絞っていく
    ct = 0
    resres = []
    for j in res:
        if j>>i&1:
            ct += 1
            resres.append(j)
    if ct >= k:
        ans += pow(2,i)
        res = resres

print(ans)
