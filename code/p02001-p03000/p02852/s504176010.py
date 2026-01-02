class SegmentTree():
    """区間更新、一点取得クエリをそれぞれO(logN)で答えるデータ構造を構築する
    update: 区間[begin, end)をvalに更新する
    get_val: i番目の値を求める
    """
    def __init__(self, n):
        self.update_cnt = 0
        self.n = n
        self.size = 1
        INF = 2**32 - 1
        while self.size < n:
            self.size *= 2
        self.node = [(self.update_cnt, -1) for i in range(2*self.size - 1)]

    def update(self, begin, end, val):
        self.update_cnt += 1
        begin += (self.size - 1)
        end += (self.size - 1)
        while begin < end:
            if (end - 1) & 1:
                end -= 1
                self.node[end] = (self.update_cnt, val)
            if (begin - 1) & 1:
                self.node[begin] = (self.update_cnt, val)
                begin += 1
            begin = (begin - 1) // 2
            end = (end - 1) // 2

    def get_val(self, i):
        i += (self.size - 1)
        val = self.node[i]
        while i > 0:
            i = (i - 1) // 2
            val = max(val, self.node[i])
        return val[1]


n, m = map(int, input().split())
s = input()
st = SegmentTree(n+1)

for i in range(n+1)[::-1]:
    if s[i] == "0":
        st.update(i+1, min(i+1+m,n+1) , i)

pos = []
start = n
while True:
    if start == 0:
        break
        
    tmp = st.get_val(start)
    if tmp == -1:
        print(-1)
        exit()
    pos.append(start - tmp)
    start= tmp
print(*pos[::-1])