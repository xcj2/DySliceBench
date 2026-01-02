from collections import defaultdict,deque
class dfs:
    def __init__(self,n,a,b,c,d):
        self.N = n
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.ans = self.N * self.D
        self.memory = defaultdict(int)
        self.Q = deque([[self.N,0]])
    def dfs(self):
        while self.Q:
            num,cost = self.Q.popleft()
            if self.memory[num] > cost :
                pass
            else:
                if num == 0:
                    self.ans = min(self.ans,cost)
                elif num == 1:
                    self.ans = min(self.ans,cost+self.D)
                else:
                    for step,a_cost in [[2,self.A],[3,self.B],[5,self.C]]:
                        if num % step != 0:
                            temp_num = (num//step)+1
                            temp_cost = cost + (((num//step)+1)*step - num) * self.D + a_cost
                            self.memo_check_append(temp_num,temp_cost)
                        temp_num = num//step
                        temp_cost = cost + (num - (num//step)*step) * self.D + a_cost
                        self.memo_check_append(temp_num,temp_cost)
                    self.ans = min(self.ans,cost + num * self.D)
        return self.ans
    def memo_check_append(self,n,c):
        if self.memory[n] > c or self.memory[n] == 0:
            self.Q.append([n,c])
            self.memory[n] = c

N = int(input())
for _ in range(N):
  N,A,B,C,D = map(int,input().split())
  T = dfs(N,A,B,C,D)
  print(T.dfs())
