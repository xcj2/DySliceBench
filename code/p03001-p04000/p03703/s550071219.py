n,k = map(int,input().split())
a = [0] + [int(input())-k for _ in range(n)]

for i in range(n):
  a[i+1] += a[i]
  
def comp(lis):
  dic = {x:i+1 for i,x in enumerate(sorted(list(set(lis))))}
  return list(map(lambda x:dic[x],lis))

a = comp(a)
 
class BIT:
    def __init__(self,n):
        self.n = n
        self.size = 1<<((n-1).bit_length())
        self.bit = [0]*(self.size+1)

    def bitsum(self,idx):
        tmp = 0
        while idx:
            tmp += self.bit[idx]
            idx -= idx & -idx
        return tmp

    def bitadd(self,idx,x):
        while idx <= self.n:
            self.bit[idx] += x
            idx += idx & -idx
        return

bit = BIT(max(a))
ans = 0
for x in a:
    ans += bit.bitsum(x)
    bit.bitadd(x,1)
print(ans)
