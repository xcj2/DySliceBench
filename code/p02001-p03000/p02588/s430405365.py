class cumsum2D:
    def __init__(self, data):
        self.N = len(data)
        self.M= len(data[0])
        self.cum = [[0] * (self.M + 1) for _ in range(self.N + 1)]
        for i in range(self.N):
            for j in range(self.M):
                self.cum[i + 1][j + 1] = self.cum[i][j + 1] + self.cum[i + 1][j] - self.cum[i][j] + data[i][j]

    def get(self,x1,y1,x2,y2):
        """
        長方形の領域 [x1,x2)*[y1,y2) の範囲内にインプットされた数字の和を取る
        """
        return self.cum[x2][y2] - self.cum[x1][y2] - self.cum[x2][y1] + self.cum[x1][y1]

def five(x):
    cnt1 = 0
    while x%5==0:
        cnt1+= 1
        x = x//5
    cnt2 = 0
    while x%2==0:
        cnt2+= 1
        x = x//2
    return (min(cnt1,18), min(cnt2,18))

def digit_lift(S, l):
    if '.' in S:
        a, b = S.split('.')
        n = int(a + b) * 10 ** (l - len(b))
    else:
        n = int(S) * 10 ** l
    return n

data = [[0]*19 for _ in range(19)]

N = int(input())
Q = set()
for _ in range(N):
    A = digit_lift(input().rstrip(),9)
    x, y = five(A)
    data[x][y] += 1
    Q.add((x,y))

cum = cumsum2D(data)
res = 0
for x, y in Q:
    res += (cum.get(18-x,18-y,-1,-1)- (x>=9 and y>=9))*data[x][y]
print(res//2)