N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input().replace("s","R").replace("p","S").replace("r","P")

ans=0

def win(type):
  if type=="R":
    return R
  elif type=="S":
    return S
  elif type=="P":
    return P
  return 0

yaku=set(["R","S","P"])
def rest(a,b):
  re=yaku-set([a,b])
  for c in re:
    return c

def restRand(a):
  re=yaku-set([a])
  for c in re:
    return c

me=[""]*len(T)
for i in range(len(T)):
  if i-K<0:
    ans+=win(T[i])
    me[i]=T[i]
  else:
    if me[i-K]==T[i]:
      # 勝つ手は出せない
      # 残り二つのうち、K回あとに勝負がある場合、K回あとに勝てる手以外を出す
      if i+K<len(T):
        me[i]=rest(T[i],T[i+K])
      else:
        me[i]=restRand(T[i])
    else:
      # 勝つ手を出せる
      ans+=win(T[i])
      me[i]=T[i]

print(ans)
