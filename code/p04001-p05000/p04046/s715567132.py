

class Cmber:
    def __init__(self,gensize,mod=10**9+7):
        self.mod = mod
        self.g1=[1,1]
        self.g2 = [1, 1] #逆元テーブル
        self.inverse = [0, 1] #逆元テーブル計算用テーブル
        self.getgen(gensize)
    def getgen(self,N):
        for i in range( 2, N + 1 ):
            self.g1.append( ( self.g1[-1] * i ) % self.mod )
            self.inverse.append( ( -self.inverse[self.mod % i] * (self.mod//i) ) % self.mod )
            self.g2.append( (self.g2[-1] * self.inverse[-1]) % self.mod )

    def cmb(self,n, r):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod

    def cmb_very_high_n(self,n, r):
        if ( r<0 or r>n ):
            return 0
        g1=1
        r = min(r, n-r)
        for i in range(n-r+1,n+1):
            g1*=i
            g1%=self.mod
        return g1 * self.g2[r] % self.mod


def resolve():
    H,W,A,B= map(int,input().split())
    cmb= Cmber(H+W+1)
    sm =0
    for i in range(H-A):
        bef = cmb.cmb(B+i-1,i)
        r=W-B-1
        u=H-i-1
        aft = cmb.cmb(r+u,u)
        sm += (aft*bef) % 1000000007
        sm %= 1000000007
#        print(i,r,u,bef,aft)
    print(sm)

if __name__ == "__main__":
    resolve()