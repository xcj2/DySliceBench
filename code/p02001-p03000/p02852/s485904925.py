# swag
from collections import deque
class SWAG_Stack():
    def __init__(self, F):
        self.stack1 = deque()
        self.stack2 = deque()
        self.F = F
        self.len = 0

    def push(self, x):
        if self.stack2:
            self.stack2.append((x, self.F(self.stack2[-1][1], x)))
        else:
            self.stack2.append((x, x))
        self.len += 1

    def pop(self):
        if not self.stack1:
            while self.stack2:
                x, _ = self.stack2.pop()
                if self.stack1:
                    self.stack1.appendleft((x, self.F(x, self.stack1[0][1])))
                else:
                    self.stack1.appendleft((x, x))
        self.stack1.popleft()
        self.len -= 1

    def sum_all(self):
        if self.stack1 and self.stack2:
            return self.F(self.stack1[0][1], self.stack2[-1][1])
        elif self.stack1:
            return self.stack1[0][1]
        elif self.stack2:
            return self.stack2[-1][1]
        else:
            raise IndexError

n,m = map(int, input().split())
s = input()

stack = SWAG_Stack(min)
stack.push((0,n))
turn = [-1]*(n+1)
turn[-1] = 0
for i in range(n-1, -1, -1):
    if s[i] == "1":
        stack.push((float("inf"), i))
    else:
        cost, ind = stack.sum_all()
        if cost == float("inf"):
            break
        turn[i] = cost+1
        stack.push((cost+1, i))
    if stack.len > m:
        stack.pop()
# print(turn)

if turn[0] == -1:
    print(-1)
    exit()
prev_turn=turn[0]
prev_ind = 0
ans = []
for i in range(1, n+1):
    if prev_turn-turn[i] == 1:
        ans.append(i-prev_ind)
        prev_ind = i
        prev_turn = turn[i]
print(*ans)
