#キューを使います
from collections import deque

#関数f:入力xの1の位がyだとした時、「xの末尾に(y-1)を付加したもの」を出力
def f(x):
  s=str(x) #文字列にする
  y=int(s[-1]) #末尾を取り出し数字に戻したものをyとする
  return int(s+str(y-1)) #yから1引いて、元の文字列の末尾に追加

#関数g:入力xの1の位がyだとした時、「xの末尾にyを付加したもの」を出力
def g(x):
  s=str(x) #文字列にする
  y=int(s[-1]) #末尾を取り出し数字に戻したものをyとする
  return int(s+str(y)) #yを元の文字列の末尾に追加

#関数h:入力xの1の位がyだとした時、「xの末尾にy+1を付加したもの」を出力
def h(x):
  s=str(x) #文字列にする
  y=int(s[-1]) #末尾を取り出し数字に戻したものをyとする
  return int(s+str(y+1)) #y+1を元の文字列の末尾に追加

#入力受け取り
K=int(input())

#キューの準備
q=deque()

#キューには1から9の整数を先に入れておく
for i in range(1, 10):
  q.append(i)
  
#キューから数字を取り出し、末尾に数字を付けることで作れるルンルン数をキューに追加する
#この操作をK-1回行う
for i in range(K-1):
  num=q.popleft() #キューから数字を取り出す
  if num%10!=0: #末尾が0の時は、末尾から-1した数字を付加してもルンルン数とならないため除外
    q.append(f(num))
    
  q.append(g(num))
  
  if num%10!=9: #末尾が9の時は、末尾に+1した数字を付加してもルンルン数とならないため除外
    q.append(h(num))
    
print(q.popleft()) #K回目に出てくるルンルン数を出力