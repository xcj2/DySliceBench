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

N = int(input())

lst = []
l_append = lst.append
for i in range(N):
    x, y = map(int, input().split())
    l_append([x, y, i])
# print (lst)
edge = []
e_append = edge.append
lst.sort(key = lambda x: x[0])
for i in range(1, N):
    e_append([lst[i-1][2], lst[i][2], min(abs(lst[i-1][0]-lst[i][0]), abs(lst[i-1][1]-lst[i][1]))])
# print (edge)
lst.sort(key = lambda x: x[1])
for i in range(1, N):
    e_append([lst[i-1][2], lst[i][2], min(abs(lst[i-1][0]-lst[i][0]), abs(lst[i-1][1]-lst[i][1]))])
# print (edge)
edge.sort(key = lambda x: x[2])

uni = UnionFind(N)
ans = 0
for i in edge:
    if not uni.same(i[0], i[1]): #違うグループのとき
        uni.connect(i[0], i[1])
        ans += i[2]
print (ans)