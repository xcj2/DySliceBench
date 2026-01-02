# -*- coding: utf-8 -*-
import sys

import fractions
import copy
import bisect
import math
import numpy as np
import itertools
from itertools import combinations_with_replacement
#import math#数学的計算はこれでいける。普通に0.5乗しても計算可能
#w=input()
from operator import itemgetter
from sys import stdin
#input = sys.stdin.readline#こっちの方が入力が早いが使える時に使っていこう
from operator import mul
from functools import reduce
from collections import Counter
#from collections import deque

#input = stdin.readline


j=0
k=0
n=3
r=1
a=[0]
#n=int(input())
#r=int(input())
#print(M)
#A=int(input())
#B=int(input())
#print(N)
"1行1つの整数を入力を取得し、整数と取得する"


#number_list=list(map(int, input().split(" ")))#数字の時
#print(number_list)
"12 21 332 とか入力する時に使う"
"1行に複数の整数の入力を取得し、整数として扱う"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#メモ
for i in number_list:#こっちの方がrage使うより早いらしい
    print(number_list[i-1])#

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
x=[]
y=[]
for i in range(N):
    x1, y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)
print(x)
print(y)
"複数行に2数値を入力する形式 x座標とy座標を入力するイメージ"
'''

'''
mixlist=[]
for i in range(N):
    a,b=input().split()
    mixlist.append((int(a),b))
print(mixlist)
"複数行にintとstrを複合して入力するやつ，今回はリスト一つで処理している"
'''

'''
#array=[input().split()for i in range(N)]
#print(type(array[0][0]))
#print(array)
"正方行列にstr型の値を入力"
'''

#brray=[list(map(int, input().split(" ")))for i in range(N)]
#print(type(brray[0][0]))
#print(brray)
'''
入力
1 2
4 5
7 8
出力結果
[[1, 2], [4, 5], [7, 8]]
'''
"列数に関して自由度の高いint型の値を入力するタイプの行列"
#以下に別解を記載
#N, M = [int(i) for i in input().split()]
'''
table = [[int(i) for i in input().split()] for m in range(m)]

print(type(N))
print(N)
print(type(M))
print(M)

print(type(table))
print(table)
'''




#s=input()
#a=[int(i) for i in s]
#print(a[0])
#print([a])
#単数値．桁ごとに分割したい．入力と出力は以下の通り
#イメージとして1桁ごとにリストに値を入れているかんじ
#intを取ると文字列分解に使える
'''
入力
1234
出力
1
[[1, 2, 3, 4]]
'''




'''
word_list= input().split(" ")
print(word_list[0])
"連続文字列の入力"
"qw er ty とかの入力に使う"
"入力すると空白で区切ったところでlistの番号が与えられる"
'''



'''
A, B, C=stdin.readline().rstrip().split()#str style 何個でもいけることが多い
print(A)
"リストではなく独立したstr型を入れるなら以下のやり方でOK"
'''


#a= stdin.readline().rstrip()
#print(a.upper())
"aという変数に入っているものを大文字にして出力"


#a,b=map(int, input().split())  #int style 複数数値入力　「A B」みたいなスペース空いた入力のとき

#なんかうまく入力されるけど
#a=[[int(i) for i in 1.strip()]for 1 in sys.stdin]
#a = [[int(c) for c in l.strip()] for l in sys.stdin]]
#print(a)
#複数行の数値を入力して正方行列を作成


##############################################################################################
##############################################################################################
#under this line explains example calculation



'''
コンビネーションの組み合わせの中身を出力する形式
for i in itertools.combinations(brray, 2)
combinationsをpermutationsにすれば順列になる
今回なら(abc133B)
入力
1 2
5 5
-2 8
出力
[[1, 2], [5, 5], [-2, 8]]
もちろん一次元リストでも使えるし
何よりiもリストのように使えるので便利
'''

#nCr combination
'''
def cmb(n,r):
    #When n < r , this function isn't valid
    r= min(n-r,r)
    #print(n,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n-r, -1))
    #flochart mul(n,n-1)=x
    #next     mul(x,n-2)........(n-r+1,n-r)
    #mul read a,b and returns a*b

    under = reduce(mul, range(1, r+1))
    #print(over, under)
    #reduce is applied mul(1,2)=2
    #next   mul(2,3)=6
    #next   mul(6,4)=4.........last(r!,r+1)=r+1!

    return over // under
    #// is integer divide
    #calc example 5C2
    #over=5*4*3
    #under=3*2*1
a = cmb(n, r)
#print(a)
'''

'''
import itertools
from itertools import combinations_with_replacement

combinationについて
以下の違いを意識しよう
combinations() p, r 長さrのタプル列、ソートされた順で重複なし

combinations_with_replacement() p, r 長さrのタプル列、ソートされた順で重複あり


使用例 　　　　　　　　　　　                  出力　　
combinations('ABCD', 2)　　　　　　　　　　　　AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)　　 AA AB AC AD BB BC BD CC CD DD
'''



'''
#集計
#example
#a=[2,2,2,3,4,3,1,2,1,3,1,2,1,2,2,1,2,1]
#a=Counter(a)
for i in a.most_common(n):print(i)
#most_common()メソッドは、出現回数が多い要素順にCounterオブジェクトを並び替えます。
#引数にint型の数字nを設定した場合は、出現回数が高い上位ｎ個の要素を返します。
#何も設定しなければ、コンテナ型にあるすべての要素を出現回数の順番に並び替えたタプル型オブジェクトを返します。
#out put
#(2, 8)
 #(1, 6)
#(3, 3)
#(4, 1)
'''


#二部探索(binary search)
#A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
#print(A)
#index = bisect.bisect_left(A, 5) # 7 最も左(前)の挿入箇所が返ってきている
#A.insert(index, 5)
#print(index)
#print(A)
'''
bisect.bisect_left(a, x, lo=0, h=len(a))
引数
a: ソート済みリスト
x: 挿入したい値
lo: 探索範囲の下限
hi: 探索範囲の上限
(lo, hiはスライスと同様の指定方法)
bisect_leftはソートされたリストaに対して順序を保ったままxを挿入できる箇所を探索します。leftが示す通り、aにすでにxが存在している場合は、挿入箇所は既存のxよりも左側になります。また、lo, hiを指定することで探索範囲を絞り込むことも可能です。デフォルトはaの全体が探索対象です。
'''

'''
素数の判定
'''
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(np.sqrt(n)) + 1):
        #sqrt(n)+1以上は考えて約数はないので却下
        if n % k == 0:
            return False
            #割り切れたらFalse
    return True


'''
npのmaxとmaximumの違い
xs = np.array([1, -2, 3])
np.max(xs, 0)
この出力は3となります．[1, -2, 3]と0の4つの数字のうち，最も大きい値を出力します．

一方で，[max(1, 0), max(-2, 0), max(3, 0)]を出力したい時があります．
その時は，numpyのmaximum関数を用います．

xs = np.array([1, -2, 3])
np.maximum(xs, 0)  # [1, 0, 3]

'''

def factorial(x, mod=10**9+7):
    # x!
    # 階乗
    # ex) factorial(5) = 120
    tmp = 1
    for i in range(1, x+1):
        tmp = (tmp * i) % mod
    return tmp
    '''
    Basically, when you do a**d % n, you actually have to calculate a**d, which could be quite large.
    But there are ways of computing a**d % n without having to compute a**d itself, and that is what pow does.
    '''
"#a,bの最大公約数"
def gcd(a, b):
    while b:#0以外なら進んでいくが、0になった時にとまる余りが0より、最大公約数と言える
        #print(a,b)#2,3
        #やり方てきにユークリッドの互除法か
        a, b = b, a % b#aには2 bには2%3が入る
    return a

"#a,bの最小公倍数"
def lcm(a, b):
    return a * b // gcd (a, b)

"#nの約数を全て求める"
def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


########################################################################
########################################################################
#b2=a[:]  #1次元のときはコピーはこれで良い
#print(b2)

#a= [[0]*3 for i in range(5)] #2次元配列はこう準備、[[0]*3]*5だとだめ
#b3=copy.deepcopy(a)  #2次元配列はこうコピーする
#print(b3)

'''
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv...\xaf\xb0...
lowercase = 'abcdefghijklmnopqrstuvwxyz'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
whitespace = '\t\n\x0b\x0c\r '
'''
'''
引数endに任意の文字列を指定すると、その文字列が改行の代わりに最後に挿入される。例えば連続するprint()の出力を改行なしで単純に連結したい場合は空文字列''を指定すればよい。

print('abc', end='---')
print('xyz')
# abc---xyz

print('abc', end='')
print('xyz')
# abcxyz
source: print_basic.py
なお、デフォルトで改行されるのは引数endのデフォルト値が改行文字'\n'に設定されているから。
'''

def main():
    n=3
    steps=0
    state=0
    w=1
    j=0
    k=0
    #lenを変数に置くと事故るから注意
    n=int(input())
    #a,b=input().split(" ")#a,bがともに文字列のとき
    #a,b=map(int, input().split(" "))
    #mapでとってもstrで変換すればappend可能
    #s=input()
    kl=[0]*n
    for i in range(n):
        kl[i]=int(input())
    #a=[i for i in s]#int(i)にすれば数字も行ける
    #kl=list(map(int, input().split(" ")))#数字の時
    kl.sort()
    kl[-1]=kl[-1]/2
    print(int(sum(kl)))
    #print(a)
    #brray=[list(map(int, input().split(" ")))for i in range(n)]
    #print(brray)


    #for i in range(1,n+1,2):#これで1個飛ばしループになる
    # pass
     #print(i)

    l = ['aaa', 'bbb', 'ccc']
    x=l.index('aaa')#ある要素のインデックス番号を取得
    #s = ''.join(l)
    #s = " ".join(map(str,a))#スペースを空ける時はこう
    #print(s)
    # aaabbbccc

    #if state in known_states and not flag: # state => 2 steps => 5
        #こうやってある要素がリストの中にあるか探すのか
    #print(f'steps: {steps}, state: {state}')
    #こう書いてあるとデバックしやすい

    #dp= [[0]*3 for i in range(5)]#列　行
    #dp用の0の入ったやつ
    #dp= [[0]*(w+1) for i in range(n+1)]#0からwまでのw+1回計算するから
    #print(dp)＃初期条件が入る分計算回数+1列分必要(この場合は判断すべきものの数)
    DP = np.zeros(w+1, dtype=int)#これでも一次元リストが作れる
    exdp=np.zeros((3,4)) # ３×４の２次元配列を生成。2次元ならこう
    #dtypeは指定しないとfloatになる
    #for i in range(n):#ちょっとした入力に便利
    #    a, b = map(int, input().split())
        #dp[i][0] += [a]
        #これだとintとlistをつなぐことになって不適
    #    dp[i] += [a]
    #    dp[i] += [b]
        #これはうまくいく
        #やり方はいろいろあるということ
    #print(dp)


    #brray=[list(map(int, input().split(" ")))for i in range(N)
    #print(brray)



    '''
    入力
    1234
    出力
    [1, 2, 3, 4]
    '''
    pin_l=["x" for i in range(10)]#内包表記に慣れろ
    #print(pin_l)

    ls = ["a", "b", "c", "d", "e"]


    #print(ls[2:5])
    #スライスでの取得

    #print(ls[:-3])
    #一番左端から右から3番目より左まで取得

    #print(ls[:4:2])
    #スライスで1個飛ばしで取得
    #ないときは左端スタート
    #始点のインデックス番号 : 終点のインデックス番号 : スキップする数+1
    #print(ls[::2])
    '''
    lsというリストの場合に、1つ飛びの値を取得したい場合には
    ls[::2]
    のようにします。こうすると、
    ["a", "c", "d"]と出力される
    '''

if __name__ == "__main__":
    main()
