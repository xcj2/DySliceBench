import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()


def II(): return int(input())


def MI(): return map(int,input().split())


def MF(): return map(float,input().split())


def LI(): return list(map(int,input().split()))


def LF(): return list(map(float,input().split()))


def TI(): return tuple(map(int,input().split()))

# rstrip().decode('utf-8')

#####segfunc#####
def segfunc(x, y):
    return x*y
#################

#####ide_ele#####
ide_ele = 1
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def main():
	n=II()
	s=input().rstrip().decode()
	S=[]
	for i in s:
		S.append(ord(i)-ord("a"))
	
	seg=[SegTree([1]*n,segfunc,ide_ele) for _ in range(26)]
	
	#print(S)
	#print(seg)
	for i in range(n):
		seg[S[i]].update(i,0)
	
	q=II()
	for _ in range(q):
		a,b,c=input().split()
		if int(a)==1:
			b=int(b)-1
			seg[S[b]].update(b,1)
			t=ord(c)-ord("a")
			seg[t].update(b,0)
			S[b]=t
		
		else:
			#print(S)
			b=int(b)-1
			c=int(c)
			cnt=0
			for se in seg:
				if se.query(b,c)==0:
					cnt+=1
			print(cnt)
			
	
	

if __name__=="__main__":
	main()
