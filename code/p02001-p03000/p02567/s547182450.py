
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    class Segtree:
        def __init__(self, A, ide_ele, initialize = True, segf = max):
            self.N = len(A)
            self.N0 = 2**(self.N-1).bit_length()
            self.ide_ele = ide_ele
            self.segf = segf
            if initialize:
                self.data = [ide_ele]*self.N0 + A + [ide_ele]*(self.N0 - self.N)
                for i in range(self.N0-1, 0, -1):
                    self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
            else:
                self.data = [ide_ele]*(2*self.N0)
            
        def update(self, k, x):
            k += self.N0
            self.data[k] = x
            while k > 0 :
                k = k >> 1
                self.data[k] = self.segf(self.data[2*k], self.data[2*k+1])
        
        def query(self, l, r):
            L, R = l+self.N0, r+self.N0
            s = self.ide_ele
            while L < R:
                if R & 1:
                    R -= 1
                    s = self.segf(s, self.data[R])
                if L & 1:
                    s = self.segf(s, self.data[L])
                    L += 1
                L >>= 1
                R >>= 1
            return s
        
        def binsearch(self, l, r, check, reverse = False):
            L, R = l+self.N0, r+self.N0
            SL, SR = [], []
            while L < R:
                if R & 1:
                    R -= 1
                    SR.append(R)
                if L & 1:
                    SL.append(L)
                    L += 1
                L >>= 1
                R >>= 1
            
            if reverse:
                pre = self.ide_ele
                for idx in (SR + SL[::-1]):
                    if check(self.segf(self.data[idx], pre)):
                        break
                    else:
                        pre = self.segf(self.data[idx], pre)
                else:
                    return None
                while idx < self.N0:
                    if check(self.segf(self.data[2*idx+1], pre)):
                        idx = 2*idx + 1
                    else:
                        pre = self.segf(self.data[2*idx+1], pre)
                        idx = 2*idx
                return idx - self.N0
            else:
                pre = self.ide_ele
                for idx in (SL + SR[::-1]):
                    if not check(self.segf(pre, self.data[idx])):
                        pre = self.segf(pre, self.data[idx])
                    else:
                        break
                else:
                    return None
                while idx < self.N0:
                    if check(self.segf(pre, self.data[2*idx])):
                        idx = 2*idx
                    else:
                        pre = self.segf(pre, self.data[2*idx])
                        idx = 2*idx + 1
                return idx - self.N0
    N,Q=MI()
    A=LI()
    seg=Segtree(A,0,segf=max)
    N0=seg.N0
    for _ in range(Q):
        t,x,v=MI()
        if t==1:
            x-=1
            seg.update(x,v)
        elif t==2:
            l=x-1
            r=v
            print(seg.query(l,r))
        else:
            l=x-1
            r=N
            ans=seg.binsearch(l,r,lambda x: x>=v)
            if ans==None:
                ans=N
            
                
            print(ans+1)
    
    

 
 


        
    





main()
