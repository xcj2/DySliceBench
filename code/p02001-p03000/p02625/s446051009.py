MOD=10**9+7
N,M=map(int,input().split())

def invmod(a):
  return pow(a,MOD-2,MOD)

fact_list=[1]
fact_inv_list=[1]
for i in range(1,M+1):
  fact_mod=(fact_list[-1]*i)%MOD
  fact_list.append(fact_mod)
  fact_inv_list.append(invmod(fact_mod))
def comb_mod_table(n,r):
  if 0<=r<=n:
    return fact_list[n]*fact_inv_list[r]*fact_inv_list[n-r]
  else:
    return 0
def perm_mod_table(n,r):
  if 0<=r<=n:
    return fact_list[n]*fact_inv_list[n-r]
  else:
    return 0
  
answer=0
for i in range(N+1):  
  term=comb_mod_table(N,i)*pow(-1,i)*perm_mod_table(M,i)*perm_mod_table(M-i,N-i)*perm_mod_table(M-i,N-i)
  answer=(answer+term)%MOD
  
print(answer)