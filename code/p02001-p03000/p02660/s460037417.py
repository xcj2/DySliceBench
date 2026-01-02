
import math
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


# 素数pと正の整数eを用いて、z=P**eと表せる
# N%z==0
# z=まだ選んでない素数だけ選ぶ
# N = N/zに置き換える


# n = 24
# 24を素因数分解する
# z=2, 2*1
# n = 24/2

# n = 12
# z=2, 3*1
# n = 24/2


N = int(input())
#cnt = 0
z = []

def solve(N, cnt):
  #print("N:", N)
  f = factorization(N)
  #print(f)

  
  # 素因数分解の要素数分ループ
  for i in range(len(f)):
    # Pが素数かチェック
    p = f[i][0]
    #print("p:", f[i][0])
    if is_prime(p):
      # 指数の数だけループ
      for e in range(1, f[i][1]+1):
        # 未採用のzを見つける. 割り切れる数を見つける
        if (p**e in z) == False and N % (p**e) ==0:
          # 使用済みリストに追加
          z.append(p**e)
          #print("z:", p**e, "p**e:", p,e)
          cnt +=1
          #print("cnt", cnt)
          cnt = solve(N//p**e, cnt)
          return cnt
  return cnt


cnt = solve(N, 0)
print(cnt)

  
