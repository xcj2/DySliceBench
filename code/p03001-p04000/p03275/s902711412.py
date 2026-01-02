import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
aiが数列mに何回出現するか，がわかれば良い？
左をa個，右をB個見たときに，M=a+B+1として，aiがM//2 +1番目なら良い．
→ai以上の要素が(M+1)//2個以上ある，かつ，此の性質を満たすものの中で最大の数である．
これ辛そう...

でも中央値を求めるのに二分探索は良いよな
結局，答えxの決めうち二分探索で，数列mの中でx以上の要素が何個あるかを知ることができれば解ける．
(x以上のものが(M+1)//2個以上ある中で最大のxを探したい)

つまり，a[l,r]のうち，中央値がx以上になるものはいくつありますか，をときたい
a[l,r]のうちx以上の要素を((r-l+1)+1)/2個以上含むものは何個あるか，がわかれば良いか
x以上ならば+1，そうでなければ-1として，区間の総和が0以上になる区間の個数を探す．
累積和で処理する，S_r-S_(l-1)が0以上ならばOK．このl,rの組を探すのはseg木でできるか，転倒数と同じ要領で．


"""
def main():
    class BIT:
        '''
        0-indexed
        '''
        def __init__(self, N):
            self.size = N
            self.tree = [0] * (N + 1)
            self.depth = N.bit_length()

        def _bitsum(self, i):
            ret = 0
            while i:
                ret += self.tree[i]
                i ^= i & -i
            return ret

        # [l,r)の和
        def sum(self, l, r=None):
            if r is None:
                return self._bitsum(l)
            else:
                return self._bitsum(r) - self._bitsum(l)

        # i番目にxを追加
        def add(self, i, x):
            i += 1
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
            return

        def lower_bound(self, x):
            sum_ = 0
            pos = 0
            v = 1 << self.depth
            for i in range(self.depth, -1, -1):
                k = pos + v
                if k <= self.size and sum_ + self.tree[k] < x:
                    sum_ += self.tree[k]
                    pos += v
                v >>= 1
            return pos + 1, sum_

    N=I()
    A=LI()
    
    
    def calc(x):
        # xを決めたときに，数列mの中でx以上の要素が何個あるか，を返す
        
        B=[0]*N
        for i in range(N):
            if A[i]>=x:
                B[i]=1
            else:
                B[i]=-1
                
        #累積和
        S=[0]*(N+1)
        for i in range(N):
            S[i+1]=S[i]+B[i]
            
        # S[i]にiの情報を持たせる
        inf=10**6
        for i in range(N+1):
            S[i]=S[i]*inf+i
        S.sort()

            
        # Sの値が小さい順に見ていく，そいつの番号を取り出し，そこよりも左側のbitの個数を答えに足していく&そこのbitを立てる
        bit=BIT(N+1)
        res=0
        for i in range(N+1):
            s=S[i]
            ii=s%inf
            temp=bit.sum(0,ii)
            res+=temp
            bit.add(ii,1)
        return res
    
    A2=sorted(A)
    M=(N*N)//2
    ok=0
    ng=N
    
    def ch(x):
        cnt=calc(x)
        # print(x,cnt)
        return cnt>=(M+1)//2

    while ng-ok>1:
        # print(ng,ok)
        med=(ok+ng)//2
        x=A2[med]
        if ch(x):
            ok=med
        else:
            ng=med
        
            
    print(A2[ok])
                
        
    

main()
