K=int(input())
S=input()

len_S=len(S)

#逆元を用いたコンビネーション
mod = 10**9+7
def mul_mod(a,b):
  return (a*b) % mod

def fact_inv(a):
  ans = 1
  for i in range(1,a+1):
    ans = (pow(i,mod-2,mod) * ans) % mod
  return ans

fact_list = [1]
for i in range(1,len_S+K):
  fact_list.append(mul_mod(fact_list[-1],i))

fact_list_inv = [1]
for i in range(1,len_S+K):
  fact_list_inv .append((pow(i,mod-2,mod) * fact_list_inv[-1]) % mod)
def comb_inv_mod(a,b):
  tmp = (fact_list[a]*fact_list_inv[b]) % mod
  return (tmp*fact_list_inv[a-b]) % mod

ans = 0
for i in range(len_S-1,len_S+K): #Snの位置
  #print(i)
  #ans += comb_inv(len_S+K-(len_S+K-i-1)-1,N-1)*pow(25,(K-(len_S+K-i-1)),mod)*pow(26,len_S+K-i-1,mod)
  A = comb_inv_mod(i,len_S-1)*pow(25,i-len_S+1,mod) % mod 
  A = A*pow(26,len_S+K-i-1,mod) % mod
  ans += A
  #print(ans)
  ans = ans % mod
print(ans)