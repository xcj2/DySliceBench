class SegmentTree():
    """一点更新、区間取得クエリをそれぞれO(logN)で答えるデータ構造を構築する
    update: i番目をvalに変更する
    get_min: 区間[begin, end)の最小値を求める
    """
    def __init__(self, n):
        self.n = n
        self.INF = 10**18
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.node = [self.INF] * (2*self.size - 1)

    def update(self, i, val):
        i += (self.size - 1)
        self.node[i] = val
        while i > 0:
            i = (i - 1) // 2
            self.node[i] = min(self.node[2*i + 1], self.node[2*i + 2])

    def get_min(self, begin, end):
        begin += (self.size - 1)
        end += (self.size - 1)
        s = self.INF
        while begin < end:
            if (end - 1) & 1:
                end -= 1
                s = min(s, self.node[end])
            if (begin - 1) & 1:
                s = min(s, self.node[begin])
                begin += 1
            begin = (begin - 1) // 2
            end = (end - 1) // 2
        return s


from operator import itemgetter


n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

info = sorted(info, key = itemgetter(1))
st = SegmentTree(n)
st.update(0, 0)

i = 0
for num in range(n+1):
    while True:
        if i >= m:
            break
        if info[i][1] != num:
            break
        else:
            l = info[i][0] - 1
            r = num
            tmp = min(st.get_min(l, r) + info[i][2], st.get_min(num - 1, num))
            st.update(num-1, tmp)
            i += 1
ans = st.get_min(n-1, n)
if ans == 10**18:
    print(-1)
else:
    print(ans)