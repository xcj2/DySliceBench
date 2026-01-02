# スタックの実装。
class Stack():
    def __init__(self):
        self.stack = []
    # データを追加する。
    def push(self, item):
        self.stack.append(item)
    # データを取り出す。
    def pop(self):
        return self.stack.pop()
    # スタックの中身を確認する。
    def get_stack(self):
        return self.stack
    # スタックが空ならばTrueを返す。
    def isEmpty(self):
        return len(self.stack) == 0
    # スタックに格納されているものの数を返す。
    def count(self):
        return len(self.stack)
    #　スタックのトップを見る（取り出さずに）。
    def top(self):
        return self.stack[-1]

# ヒストグラムの最大長方形を求める関数。
def Histogram(n,l):
    if n == 0:
        return 0
    stack = Stack()
    t = 0
    ans = 0
    while t < n:
        r = l[t]
        if stack.isEmpty():
            stack.push((r,t))
            t += 1
            # print(stack.get_stack(),t)
        elif stack.top()[0] < r:
            stack.push((r,t))
            t += 1
            # print(stack.get_stack(),t)
        elif stack.top()[0] == r:
            t += 1
            # print(stack.get_stack(),t)
        elif stack.top()[0] > r:
            while stack.top()[0] > r:
                p,q = stack.pop()
                ans = max(ans,p*(t-q))
                # print(stack.get_stack(),t)
                if stack.isEmpty():
                    break;
            stack.push((r,q))
            t += 1
    while not stack.isEmpty():
        p,q = stack.pop()
        ans = max(ans, p*(t-q))
        # print(stack.get_stack(),t)
    return ans


H,W  = [int(_) for _ in input().split()]
dp = [[0]*W for _ in range(H)]
for i in range(H):
    for j,value in enumerate([int(_) for _ in input().split()]):
        dp[i][j] = value
c = 1
for j in range(W):
    i = 0
    while i < H:
        if dp[i][j] == 0:
            dp[i][j] = c
            c += 1
        else:
            dp[i][j] = 0
            c = 1
        i += 1
    c = 1

# for i in range(H):
#     print(dp[i])

ans = 0
l = []
for i in range(H):
    for j in range(W):
        if dp[i][j] == 0:
            ans = max(ans,Histogram(len(l),l))
            # print(len(l),l)
            l = []
        else:
            l.append(dp[i][j])
    ans = max(ans,Histogram(len(l),l))
    # print(len(l),l)
    l = []
print(ans)


# print('TEST')
# print(Histogram(5, [3,5,4,5,5]))
