class Doubling():
    def __init__(self,N,log_k,perm):
        """
        与えられた順列のダブリング配列を作成する.

        Parameters
        ----------
            N :  int
                順列の数
            log_k : int
                最大移動回数の対数(切り上げ)
            perm : [int]
                1-indexed の順列が格納されたリスト
        """
        self.N = N
        self.log_k = log_k
        self.doubling = [[0]*(self.N+1) for _ in range(log_k)]

        for i in range(1,self.N+1):
            self.doubling[0][i] = perm[i]

        for j in range(1,self.log_k):
            for i in range(1,self.N+1):
                prev = self.doubling[j-1][i]
                self.doubling[j][i] = self.doubling[j-1][prev]
        
    def query(self,pos,k):
        """
        位置iからk回移動したときの移動先を計算する.

        Parameters
        ----------
            pos : int
                移動元の位置
            k : int
                移動回数(1<=k<=2^(log_k+1)-1)

        Returns
        ----------
            dest : int
                移動先の位置
        """
        for i in range(self.log_k):
            if k & (1<<i) == 0:continue
            pos = self.doubling[i][pos]
        dest = pos
        
        return dest

def main():
    n,k = tuple([int(t)for t in input().split()])

    a = [int(t) for t in input().split()]

    a.insert(0,0)
    log_k = k.bit_length()+1

    doubling = Doubling(n,log_k,a)
    print(doubling.query(1,k))

    
if __name__ == "__main__":
    main()