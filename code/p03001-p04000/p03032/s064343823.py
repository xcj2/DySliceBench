def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

# 以上マージソート

N, K = map(int, input().split())
que = list(map(int, input().split()))

qa = [0]
takea = [[]]
now = 0

for i in range(N):
    now += que[i]
    qa.append(now)
    takea.append(que[0:i+1])

qb = [0]
takeb = [[]]
now = 0

for i in reversed(range(N)):
    now += que[i]
    qb.append(now)

    takeb.append(que[i:])

max = 0

# 取る個数：i
for i in range(1, N+1):
    #左から取る個数：j
    for j in range(i+1):
#        print("Left : ", j, "   Right : ", i-j)
        qtotal = qa[j]+qb[i-j]
        taketotal = takea[j]+takeb[i-j]
        taketotal = merge_sort(taketotal)
        discardable = K-i
        for k in taketotal:
            if (discardable==0):
                break;

            if (0<=k):
                break;
            else:
                qtotal-=k
                discardable-=1
        if(max<qtotal):
            max = qtotal
    if(i==K):
        break;

print(max)

# temp
'''
A = int(input())
'''
# 2つ
'''
A, B = map(int, input().split())
'''
# N個+横1列
'''
N = input()
A = list(map(int, input().split()));
'''
#-1が来るまでinput
'''
a = []
while True:
    n = input()
    if n == -1:
        break
    a.append(n)
'''
#EOFまでinput
'''
import sys

a = []
for line in sys.stdin:
    a.append(int(line))
'''

# 横N 縦M
'''
N, M = map(int, raw_input().split())
a = []
for i in range(M):
    a.append(map(int, raw_input().split()))
'''

# union-find木
'''
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
'''

# merge sort
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

'''
