import sys
input = sys.stdin.readline

class Dict:
  def __init__(self, size):
    self.table = [None] * 1046527
    self.table_size = 1046527

  def insert(self, val):
    key = self.get_key(val)
    collision = 0
    while True:
      h = self.generate_hash(key, collision)
      if self.table[h] is None:
        self.table[h] = val
        break
      elif self.table[h] == val:
        break
      collision += 1
  def find(self, val):
    key = self.get_key(val)
    collision = 0
    while True:
      h = self.generate_hash(key, collision)
      if self.table[h] == val: return 1
      elif self.table[h] is None: return 0
      collision += 1

  def get_key(self, val):
    sum, P = 0, 1
    for i in range(len(val)):
      sum += P * self.get_char(val[i])
      P *= 5
    return sum

  def get_char(self, ch):
    if ch == 'A': return 1
    elif ch =='C': return 2
    elif ch =='G': return 3
    elif ch =='T': return 4
    else: return 0

  def generate_hash(self, key, collision):
    h1 = key % self.table_size
    h2 = 1 + key % (self.table_size - 1)
    return (h1 + collision * h2) % self.table_size

def _main():
  N = int(input())
  d = Dict(N)
  commands = [input().split() for _ in range(N)]

  for i in range(N):
    if commands[i][0] == 'insert':
      d.insert(commands[i][1])
    else:
      ans = 'yes' if d.find(commands[i][1]) else 'no'
      print(ans)



if __name__ == '__main__':
  _main()
