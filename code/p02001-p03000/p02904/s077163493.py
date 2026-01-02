class SparseTableMAX():
    def __init__(self, array, n):
        '''テーブルを構築する'''
        self.row_size = n.bit_length()
        
        # log_tableを構築する
        # log_table = [0, 0, 1, 1, 2, 2, 2, 2, ...]
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i//2] + 1
        
        # sparse_tableを構築する
        self.sparse_table = [[0] * n for _ in range(self.row_size)]
        for i in range(n):
            self.sparse_table[0][i] = array[i]
        for row in range(1, self.row_size):
            for i in range(n - (1 << row) + 1):
               self.sparse_table[row][i] = self._merge(self.sparse_table[row - 1][i], \
                                                       self.sparse_table[row - 1][i + (1 << row - 1)])

    def _merge(self, num1, num2):
        '''クエリの内容'''
        return max(num1, num2)

    def query(self, l, r):
        '''区間[l, r)に対するクエリに答える'''
        if r == l:
            return None
        row = self.log_table[r - l]
        return self._merge(self.sparse_table[row][l], self.sparse_table[row][r - (1 << row)])


class SparseTableMIN():
    def __init__(self, array, n):
        '''テーブルを構築する'''
        self.row_size = n.bit_length()
        
        # log_tableを構築する
        # log_table = [0, 0, 1, 1, 2, 2, 2, 2, ...]
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i//2] + 1
        
        # sparse_tableを構築する
        self.sparse_table = [[0] * n for _ in range(self.row_size)]
        for i in range(n):
            self.sparse_table[0][i] = array[i]
        for row in range(1, self.row_size):
            for i in range(n - (1 << row) + 1):
               self.sparse_table[row][i] = self._merge(self.sparse_table[row - 1][i], \
                                                       self.sparse_table[row - 1][i + (1 << row - 1)])

    def _merge(self, num1, num2):
        '''クエリの内容'''
        return min(num1, num2)

    def query(self, l, r):
        '''区間[l, r)に対するクエリに答える'''
        if r == l:
            return None
        row = self.log_table[r - l]
        return self._merge(self.sparse_table[row][l], self.sparse_table[row][r - (1 << row)])
      
n, k = map(int, input().split())
a = list(map(int, input().split()))
max_st = SparseTableMAX(a, n)
min_st = SparseTableMIN(a, n)

ans = 0
for i in range(1,n-k+1):
    l = a[i-1]
    r = a[i+k-1]
    min_ = min_st.query(i-1, i-1+k)    
    max_ = max_st.query(i, i+k)
    if l != min_ or r != max_:
        ans += 1

tmp = 0
cnt = 0
tmp_ans = 0
l = -1
for i in range(1, n):
    if a[i-1] > a[i]:
        tmp = i
    if i >= k-1 and tmp <= i - k + 1:
        if i - l > 1:
            cnt += 1
        l = i
ans += 1 - max(cnt - 1, 0)

print(ans)