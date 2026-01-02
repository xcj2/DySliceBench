import sys
rd = sys.stdin.readline

class BIT:
    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)
        
    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def add(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)
    
    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

n,q = map(int,rd().split())
c = list(map(int,rd().split()))
lr = []
for i in range(q):
    l,r = map(int,rd().split())
    lr.append([l,r,i])
lr.sort(key = lambda x:x[1])

last = [-1]*(n+1)
bit = BIT(n+1)
ans = [0]*q
current = 1
for i in range(q):
    # rightに達するまで
    while current <= lr[i][1]:
        # 今の色が過去にあった場合、bitの値を0に戻す
        if last[c[current-1]] != -1:
            bit.add(last[c[current-1]], -1)
        last[c[current-1]] = current
        bit.add(current, 1)
        current += 1
    ans[lr[i][2]] = bit.query(lr[i][1]) - bit.query(lr[i][0] - 1)

print(*ans, sep = "\n")