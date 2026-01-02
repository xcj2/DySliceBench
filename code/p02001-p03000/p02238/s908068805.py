ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

class tree:
    def __init__(self,n):
        self.n = n
        self.vlist = [None]*self.n
        self.start = [None]*self.n
        self.finish = [None]*self.n
        self.time = 0
    
    def add(self,n,v):
        v.sort()
        self.vlist[n] = v

    def search(self,u):
        if self.start[u] != None:
            return
        else:
            self.time += 1
            self.start[u] = self.time

            for i in self.vlist[u]:
                self.search(i-1)

            self.time += 1
            self.finish[u] = self.time
            return

n = ii()
t = tree(n)

for i in range(n):
    vk = li()
    u = vk[0]
    k = vk[1]
    v = vk[2:]
    t.add(u-1,v)

for i in range(n):
    t.search(i)

for i in range(n):
    print(i+1, t.start[i], t.finish[i])

