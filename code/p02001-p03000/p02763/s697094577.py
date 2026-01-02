import sys
input = sys.stdin.readline

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
            t = self.ide_ele
            while L < R:
                if R & 1:
                    R -= 1
                    t = self.segf(self.data[R],t)
                if L & 1:
                    s = self.segf(s,self.data[L])
                    L += 1
                L >>= 1
                R >>= 1
            return self.segf(s,t)

        # セグ木上で二分探索，[l,r)の範囲でcheck関数を満たす最小の値をとるところのindexを返す．
        # reverse=Trueなら最大値かな
        # ない時の返り値がNoneなことに注意
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
    

    N=I()
    S=input()
    Q=I()
    
    A=[]
    for i in range(N):
        ii=ord(S[i])
        aaa=set([ii])
        A.append(aaa)
    
    seg=Segtree(A,set([]),segf=lambda a,b:a|b)
    
    for _ in range(Q):
        q=input().split()
        if q[0]=="1":
            i=int(q[1])-1
            c=q[2]
            seg.update(i,set([ord(c)]))
        else:
            l=int(q[1])
            r=int(q[2])
            ans=seg.query(l-1,r)
            print(len(ans))
    

main()
