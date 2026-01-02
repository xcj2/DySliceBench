class SegTree():
    def segfunc(self, x, y):
        return x+y

    def __init__(self, ide, n, init_val):
        self.ide_ele = ide
        self.num = 2**(n-1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num-1] = init_val[i]    
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1], self.seg[k*2+2])
    def query(self, p, q):#p <= x < q
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res

def main():
    q = int(input())
    ans = []
    query = [list(map(int, input().split())) for _ in range(q)]
    a_arr = []
    for arr in query:
        if arr[0] == 1:
            a_arr.append(arr[1])
    a_arr.sort()
    dic = {}
    rev_dic = {}
    p = 0
    for v in a_arr:
        if not v in dic:
            dic[v] = p
            rev_dic[p] = v
            p += 1
    seg_arr = [0]*p
    seg = SegTree(0, p, seg_arr)
    b_sum = 0
    cnt = 0
    add = 0
    f = False
    range_L, range_R = -1, -1
    for arr in query:
        if arr[0] == 1:
            x = dic[arr[1]]
            b_sum += arr[2]
            seg_arr[x] += 2
            seg.update(x, seg_arr[x])
            cnt += 1
            if f:
                if range_L <= x <= range_R:
                    add += 0
                elif x < range_L:
                    add += rev_dic[range_L] - arr[1]
                else:
                    add += arr[1] - rev_dic[range_R]
        L, R = -1, p-1
        while L+1 < R:
            P = (L+R+1)//2
            if seg.query(0, P+1)-cnt >= 0:
                R = P
            else:
                L = P
        range_L = R
        L, R = 0, p
        while L+1 < R:
            P = (L+R)//2
            if seg.query(P, p)-cnt >= 0:
                L = P
            else:
                R = P
        range_R = L
        f = True
        if arr[0] == 2:
            ans.append([rev_dic[range_L], b_sum + add])
    for a, b in ans:
        print(a, b)

if __name__ == "__main__":
    main()