class Telp:
    def __init__(self, to, idx):
        self.to = to
        self.idx = idx
        self.visited = False
        self.step = -1

    def visit(self, step):
        self.visited = True
        self.step = step

    def is_visited(self):
        return self.visited


n, k = map(int, input().split())

a = list(map(int, input().split()))

net = {}

for i in range(n):
    net[i] = Telp(a[i], i)

current = net[0]
count = 0
path = []

while not current.visited:
    # print(current.to)
    path.append(current)
    current.visit(count)
    current = net[current.to - 1]
    count += 1
    if count == k:
        print(path[-1].to)
        exit(0)
    # print("count", count)

offset = current.step
loop = count - offset
fact_idx = (k - offset) % loop

# print("count, offset, loop, fact_idx", count, offset, loop, fact_idx)
# print("ans", path[offset + fact_idx - 1].to)

print(path[offset + fact_idx - 1].to)
