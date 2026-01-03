from collections import deque

class SlideMin:
    """
    スライド最小値\n
    各区間[ai, ai+leng]の最小値を取得する：O(n)\n
    self.que = [(i1, v1), (i2, v2), ..., (ik, vk)]\n
    i1 < ... < ik and v1 < ... < vk
    """
    def __init__(self, leng):
        self.que = deque([])
        self.leng = leng

    def top(self):
        return self.que[0]

    def getQue(self):
        return self.que

    def update(self, index, value):
        while self.que:
            if self.que[-1][1] >= value:
                self.que.pop()
            else:
                break

        self.que.append((index, value))

        if self.que[0][0] == index - self.leng:
            self.que.popleft()

N, X = map(int, input().split())
A = list(map(int, input().split()))

def sol(n):
    # n個前までの最小値
    B = A + A
    que = SlideMin(n + 1)
    ret = [10**18] * N
    for i, a in enumerate(B):
        que.update(i, a)
        ret[i % N] = min(ret[i % N], que.top()[1])
    return sum(ret) + n * X

ans = sum(A)
for i in range(N):
    ans = min(ans, sol(i))
print(ans)
