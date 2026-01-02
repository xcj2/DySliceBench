#import sys
#sys.setrecursionlimit(500000)　マージテクをちゃんとしていればこんなものはいらないはず……

class UF:
    #経路圧縮＋マージテクのunion find木
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * (n+1) #1-indexedにするために１個足している
        self.rnks = [0] * (n+1)

    def find(self,n):
        if self.parents[n] < 0:
            return n
        else:
            self.parents[n] = self.find(self.parents[n])
            return self.parents[n]

    def union(self,a,b):
        a_par = self.find(a)
        b_par = self.find(b)

        if a_par == b_par:
            return
        if self.rnks[a_par] < self.rnks[b_par]: #ランクの高い方の根に低い方の根をつける　逆にしないように……！
            a_par,b_par = b_par,a_par
        if self.rnks[a_par] == self.rnks[b_par]:
            self.rnks[a_par] += 1
        self.parents[a_par] += self.parents[b_par]
        self.parents[b_par] = a_par

    def length(self,n):
        par = self.find(n)
        return abs(self.parents[par])

    def is_same(self,a,b):
        return self.find(a) == self.find(b)



def main():
    n,m,k = map(int,input().split())
    uf = UF(n)
    block_lst = [0 for _ in range(n+1)]
    friend_lst = [0 for _ in range(n+1)]
    #友達リスト部分
    for i in range(m):
        a,b = map(int,input().split())
        friend_lst[a] += 1
        friend_lst[b] += 1
        uf.union(a,b)
    #print(friend_lst)

    #ブロックリスト部分
    for i in range(k):
        c,d = map(int,input().split())
        if uf.is_same(c,d):#c,dが同じ友達候補グループにない限り、解答には影響しない！
            block_lst[c] += 1
            block_lst[d] += 1
    #print(block_lst)
    #メイン処理
    answer = []

    for i in range(1,n+1):
        f_o_f = uf.length(i)
        answer.append(f_o_f - friend_lst[i] - block_lst[i] - 1)


    print(" ".join(map(str,answer)))






if __name__ == '__main__':
    main()
