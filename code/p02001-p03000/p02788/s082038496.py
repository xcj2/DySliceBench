import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

class DualSegmentTree:
    def __init__(self, n) :
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [0] * (self.N0*2)

    def update(self, l, r, val) :
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = self.data[l] + val
                l += 1
            if r & 1:
                self.data[r-1] = self.data[r-1] + val
                r -= 1
            l //= 2
            r //= 2

    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = ret + self.data[i]
        return ret




def main():
    N,D,A = list(map(int,input().split()))

    enemy = []
    for i in range(N):
        x,h = list(map(int,input().split()))
        if h%A==0:
            enemy.append([x,h//A])
        else:
            enemy.append([x,h//A+1])

    enemy.sort(key=lambda x:x[0])
    def bisect(index):
        x = enemy[index][0]
        if enemy[N-1][0] <= x + 2*D:
            return N-1
        l = index
        r = N-1
        while r-l>1:
            if enemy[(r+l)//2][0] <= x + 2*D:
                l = (r+l)//2
            else:
                r = (r+l)//2
        return l
    ST = DualSegmentTree(N)

    for i in range(N):
        ST.update(i,i+1,enemy[i][1])

    count = 0
    for i in range(N):
        v = ST.query(i)
        if v>0:
            count += v
            j = bisect(i)
            ST.update(i,j+1,-v) 

    print(count)

if __name__ == '__main__':
    main()

