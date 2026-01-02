# simpleバージョン
class BinaryIndexedTree:
    def __init__(self,size):
        self.N = size
        self.bit = [0]*(size+1)
    def add(self,x,w): # 0-indexed
        x += 1
        while x <= self.N:
            self.bit[x] += w
            x += (x & -x)
    def _sum(self,x): # 1-indexed
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= (x & -x)
        return ret
    def sum(self,l,r): # [l,r)
        return self._sum(r) - self._sum(l)
    def __str__(self): # for debug
        arr = [self.sum(i,i+1) for i in range(self.N)]
        return str(arr)


class BIT:
    """ 区間加算BIT(区間加算・区間合計取得) """
 
    def __init__(self, N):
        # 添字0が使えないので、内部的には全て1-indexedとして扱う
        N += 1
        self.N = N
        self.data0 = [0] * N
        self.data1 = [0] * N
 
    def _add(self, data, k, x):
        k += 1
        while k < self.N:
            data[k] += x
            k += k & -k
 
    def _get(self, data, k):
        k += 1
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s
 
    def add(self, l, r, x):
        """ 区間[l,r)に値xを追加 """
 
        self._add(self.data0, l, -x*(l-1))
        self._add(self.data0, r, x*(r-1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)
 
    def query(self, l, r):
        """ 区間[l,r)の和を取得 """
 
        return self._get(self.data1, r-1) * (r-1) + self._get(self.data0, r-1) \
             - self._get(self.data1, l-1) * (l-1) - self._get(self.data0, l-1)

def ctoi(c):
    return ord(c) - ord('a')

def main():
    N = int(input())
    S = input()
    Q = int(input())
    query = [input().split() for i in range(Q)]
    bits = [BIT(N) for i in range(26)]
    s = []
    for i, c in enumerate(S):
        bits[ctoi(c)].add(i,i+1,1)
        s.append(c)

    for a, b, c in query:
        if a == '1':
            i = int(b) - 1
            bits[ctoi(s[i])].add(i,i+1,-1)
            bits[ctoi(c)].add(i,i+1,1)
            s[i] = c
        else:
            l = int(b) - 1
            r = int(c)
            a = 0
            for i in range(26):
                if bits[i].query(l,r):
                    a += 1
            print(a)




if __name__ == "__main__":
    main()