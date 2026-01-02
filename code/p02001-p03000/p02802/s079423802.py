init = input().split(" ")
n = int(init[0])
m = int(init[1])

class problem():
  right_or_wrong = 0
  mistake = 0
  
  def set_right(self):
    self.right_or_wrong = 1
  
  def set_wrong(self):
    self.mistake += 1
  
  def check(self, result):
    if result == "AC":
      self.set_right()
    elif result == "WA" and self.right_or_wrong == 0:
      self.set_wrong()

if m == 0:
  print("0 0")
  exit()

result = {}
for i in range(m):
  score = input().split(" ")
  p = int(score[0])
  s = score[1]
  if p not in result:
    result[p] = problem()
  result[p].check(s)

ans = [0, 0]
for v in result.values():
  if v.right_or_wrong == 1:
    ans[0] += 1
    ans[1] += v.mistake

print(" ".join([str(i) for i in ans]))