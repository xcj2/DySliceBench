def main():
  n=int(input())
  s=list(input())
  q_=int(input())
  q=[input().split() for _ in range(q_)]
  class BIT:
    def __init__(self, n):
      self.n = n
      self.data = [0]*(n+1)
      self.el = [0]*(n+1)
    def sum(self, i):
      s = 0
      while i > 0:
        s += self.data[i]
        i -= i & -i
      return s
    def add(self, i, x):
      # assert i > 0
      self.el[i] += x
      while i <= self.n:
        self.data[i] += x
        i += i & -i
    def get(self, i, j=None):
      if j is None:
        return self.el[i]
      return self.sum(j) - self.sum(i)

  a2n = lambda c: ord(c) - ord('a')
  d=[BIT(n) for _ in range(26)]
  di=[0]*26
  for i in range(1,n+1):
    d[a2n(s[i-1])].add(i,1)
  for qi in q:
    if qi[0]=='1':
      i=int(qi[1])
      c=a2n(qi[2])
      si=a2n(s[i-1])
      d[c].add(i,1)
      d[si].add(i,-1)
      s[i-1]=qi[2]
    else:
      ans=0
      l,r=int(qi[1]),int(qi[2])
      for i in range(26):
        ls=d[i].sum(l-1)
        rs=d[i].sum(r)
        ans+=1 if rs-ls>0 else 0
      print(ans)
if __name__=='__main__':
  #import datetime
  #print(datetime.datetime.now())
  main()
  #print(datetime.datetime.now())
