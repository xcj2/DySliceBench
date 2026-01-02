class node():
    def __init__(self, data, child=None):
        self.child = child
        self.data = data

class head():
    def __init__(self, data):
        self.child = None
        self.length = 0
        for i in data:
            self.add(i)

    def add(self, i):
        self.child = node(i, child=self.child)
        self.length += 1
    
    def remove(self):
        idx = self.length
        root = self
        child = self.child
        while child is not None:
            if child.data == idx:
                root.child = child.child
                self.length -= 1
                return child.data
            idx -= 1
            root = child
            child = root.child

        return False

n = int(input())
data = list(map(int, input().split()))
linked = head(data)
ans = []
while True:
    step = linked.remove()
    if step is False:
        break
    ans.append(step)

if len(ans) != n:
    print(-1)
else:
    for a in reversed(ans):
        print(a)