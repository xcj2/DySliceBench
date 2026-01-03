
###template###
import sys
def input(): return sys.stdin.readline().rstrip()
import heapq
INF = float("inf")
def mi(): return map(int, input().split())
def ii(): return int(input())
###template###

def custom_round(number, ndigits=0):
  if type(number) == int: #整数ならそのまま返す
    return number
  d_point = len(str(number).split('.')[1]) #小数点以下が何桁あるか定義
  if ndigits >= d_point:#求める小数点以下の値が引数より大きい場合はそのまま返す
    return number
  c = (10 ** d_point) * 2
    #小数点以下の桁数分元の数に0を足して整数にして2倍するための値(0.01ならcは200)
  return round((number * c + 1) / c, ndigits)
    #元の数に0を足して整数にして2倍して1を足して2で割る。元の数が0.01なら0.015にしてroundを行う

Ai = list(mi())

for a in Ai:
  if a % 2 == 0:
    print(0)
    exit()

print(min([Ai[0]*Ai[1], Ai[1]*Ai[2], Ai[0]*Ai[2]])) 