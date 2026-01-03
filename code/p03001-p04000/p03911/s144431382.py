class UnionFind(object):
    def __init__(self, N):
        self.parent = [-1] * N #parent[i] は(i+1)番目の要素が含まれる要素数の(-1)倍
    #要素が負-->その数を親とするグループに属する要素の数×(-1)
    #要素が正-->親のindex

    #Aがどのグループに属しているかを調べる
    def root(self, A):
        if self.parent[A-1] < 0: #負の数-->その数は親
            return A
        self.parent[A-1] = self.root(self.parent[A-1]) #負では無い時、親の場所が入っているから、親が属しているグループを、自分自身に入れる(一度確認したところは直接親を見れるようにする)
        return self.parent[A-1] #親の位置を返す

    #Aが含まれているグループに属している数を返す
    def size(self, A):
        return -1 * self.parent[self.root(A)-1]

    #AとBをくっ付ける
    def connect(self, A, B):
        A = self.root(A) #Aを含むグループの親を返す
        B = self.root(B) #Bを含むグループの親を返す
        if A == B: #親が同じならなにもしない
            return False
        
        #大きい方(A)に小さい方(B)をつなぎたい
        if self.size(A) < self.size(B): #大小関係が逆の時は入れ替える
            A, B = B, A
        
        self.parent[A-1] += self.parent[B-1] #大きい方に小さい方を加える　（負の数＋負の数 = 新しいグループに含まれる数×(-1)）
        self.parent[B-1] = A #加えられた親の値を、加えた先の親の位置に書き変える
        return True
    
    def same(self, A, B):
        if self.root(A) == self.root(B):
            return True
        else:
            return False
            
# N, Q = map(int, input().split())
# uni = UnionFind(N)
# for _ in range(Q):
#     P, A, B = map(int, input().split())
#     if P == 1:
#         if uni.root(A) == uni.root(B): #親が同じかどうか
#             print ('Yes')
#         else:
#             print ('No')
#     else:
#         uni.connect(A, B)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L1 = []
L1_append = L1.append

uni = UnionFind(M + 1)
for _ in range(N):
    KL = list(map(int ,input().split()))
    tmp = KL[1]
    L1_append(tmp)
    for i in KL[2:]:
        uni.connect(tmp, i)

tmp = uni.root(L1[0])
for i in L1[1:]:
    if tmp != uni.root(i):
        print ('NO')
        exit()

print ('YES')    
    
