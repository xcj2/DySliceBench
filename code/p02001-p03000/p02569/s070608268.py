
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    #######################
    class LazySegmentTree:
        
      __slots__ = ["n", "data", "lazy", "me", "oe", "fmm", "fmo", "foo"]

      def __init__(self, monoid_data, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator, func_operator_operator):
          self.me = monoid_identity
          self.oe = operator_identity
          self.fmm = func_monoid_monoid
          self.fmo = func_monoid_operator
          self.foo = func_operator_operator

          self.n = len(monoid_data)
          self.data = monoid_data * 2
          for i in range(self.n-1, 0, -1):
              self.data[i] = self.fmm(self.data[2*i], self.data[2*i+1])
          self.lazy = [self.oe] * (self.n * 2)
          

      def update(self, index, value):
          index += self.n

          # propagation
          for shift in range(index.bit_length()-1, 0, -1):
              i = index >> shift
              self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
              self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
              self.data[i] = self.fmo(self.data[i], self.lazy[i])
              self.lazy[i] = self.oe

          # update
          self.data[index] = value
          self.lazy[index] = self.oe

          # recalculation
          i = index
          while i > 1:
              i //= 2
              self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
              self.lazy[i] = self.oe


      def range_update(self, l, r, operator):
          l += self.n
          r += self.n
          
          # preparing indices
          indices = []
          l0 = (l // (l & -l))     // 2
          r0 = (r // (r & -r) - 1) // 2
          while r0 > l0:
              indices.append(r0)
              r0 //= 2
          while l0 > r0:
              indices.append(l0)
              l0 //= 2
          while l0 and l0 != r0:
              indices.append(r0)
              r0 //= 2
              if l0 == r0:
                  break
              indices.append(l0)
              l0 //= 2
          while r0:
              indices.append(r0)
              r0 //= 2

          # propagation
          for i in reversed(indices):
              self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
              self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
              self.data[i] = self.fmo(self.data[i], self.lazy[i])
              self.lazy[i] = self.oe

          # effect
          while l < r:
              if l % 2:
                  self.lazy[l] = self.foo(self.lazy[l], operator)
                  l += 1
              if r % 2:
                  r -= 1
                  self.lazy[r] = self.foo(self.lazy[r], operator)
              l //= 2
              r //= 2

          # recalculation
          for i in indices:
              self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
              self.lazy[i] = self.oe
              
          
      def query(self, l, r):
          l += self.n
          r += self.n

          # preparing indices
          indices = []
          l0 = (l // (l & -l))     // 2
          r0 = (r // (r & -r) - 1) // 2
          while r0 > l0:
              indices.append(r0)
              r0 //= 2
          while l0 > r0:
              indices.append(l0)
              l0 //= 2
          while l0 and l0 != r0:
              indices.append(r0)
              r0 //= 2
              if l0 == r0:
                  break
              indices.append(l0)
              l0 //= 2
          while r0:
              indices.append(r0)
              r0 //= 2
          
          # propagation
          for i in reversed(indices):
              self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
              self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
              self.data[i] = self.fmo(self.data[i], self.lazy[i])
              self.lazy[i] = self.oe

          # fold
          left_folded = self.me
          right_folded = self.me
          while l < r:
              if l % 2:
                  left_folded = self.fmm(left_folded, self.fmo(self.data[l], self.lazy[l]))
                  l += 1
              if r % 2:
                  r -= 1
                  right_folded = self.fmm(self.fmo(self.data[r], self.lazy[r]), right_folded)
              l //= 2
              r //= 2
          return self.fmm(left_folded, right_folded)
        
      ########################
      
    N,Q=LI()
    A=LI()
    B=[]
    for i in range(N):
      #0の個数，1の個数,反転数
      if A[i]:
        temp=(0,1,0)
      else:
        temp=(1,0,0)
      B.append(temp)
      
    def foo(x,y):
          return x^y
        
    def fmm(x,y):
          z1=x[0]+y[0]
          z2=x[1]+y[1]
          z3=x[2]+y[2]+x[1]*y[0]
          return (z1,z2,z3)
        
    def fmo(x,y):
          if y:
              z1=x[1]
              z2=x[0]
              z3=x[0]*x[1]-x[2]
              return (z1,z2,z3)
          else:
                return x
          
      
    seg=LazySegmentTree(B,(0,0,0),0,fmm,fmo,foo)
    ans=[]
    for _ in range(Q):
        t,l,r=MI()
        if t==1:
              seg.range_update(l-1,r,1)
        else:
              temp=seg.query(l-1,r)
              ans.append(temp[-1])
           
    for v in ans:
          print(v)
    




main()
