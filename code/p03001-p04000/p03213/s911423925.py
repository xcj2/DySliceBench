#ABC114-D 756
"""
約数の個数の求め方は、素因数分解した時の各要素の(乗数+1)をかけ合わせると求まる。
入力例2の32400を素因数分解してみると、
2^4*3^4*5^2となり、それぞれの乗数+1をかけ合わせると
(4+1)*(4+1)*(2+1) = 75となる。

また、75自体を素因数分解すると、
3^1*5^2となり、これが最小の約数であるので、
3*5*5
15*5
3*25
75
の4通りが素因数分解した時の乗数+1の候補として考えられる。

よって、約数が75個存在する数とは、基数をp,q,rとして,
p^(3-1)*q^(5-1)*r^(5-1)
p^(15-1)*q^(5-1)
p^(3-1)*q^(25-1)
p^(75-1)
のいずれかとして得られる数である。

なお、p^2*q^4*r^4の場合は4を2回使うため、combinationを使って数える必要があるのに注意。
"""
import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
dic1 = defaultdict(int)

"""素因数分解"""
def factrize(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            #もし素因数を重複させたくないならここを加えてfct.append(b)を消す
            """
            if not b in fct:
                fct.append(b)
            """
            fct.append(b)
        b = b+1
    if n > 1:
        fct.append(n)
    return fct #リストが帰る

#二項係数(modなし) O(k)
def large_conbination(n,k): #no mod. return nCk.
    res1 = 1
    for i in range(n,n-k,-1):
        res1*=i
    res2 = 1
    for i in range(1,k+1):
        res2*= i
    return res1//res2

for i in range(2,n+1): #n!を素因数分解する時、各要素ごとに素因数分解しても結果は変わらない
    for j in factrize(i):
        dic1[j] += 1

def num(m):
    return len(list(filter(lambda x:x>=m-1,dic1.values())))

#解法の条件を満たす通り数の順に再現
print(
    large_conbination(num(5),2)*(num(3)-2) +
    num(15)*(num(5)-1) + 
    num(25)*(num(3)-1) +
    num(75)
)