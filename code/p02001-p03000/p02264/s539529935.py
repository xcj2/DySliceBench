class ArrayDeque:
    def __init__(self):
        self.a_size = 1
        self.a = [None]
        self.n = 0
        self.head = 0
        self.tail = 0

    def __bool__(self):
        return self.n != 0

    def _resize(self):
        new_a = [None] * ((self.n + 1) << 1)
        for i in range(self.n):
            new_a[i] = self.a[(self.head + i) & (self.a_size - 1)]
        self.a = new_a
        self.a_size = (self.n + 1) << 1
        self.head = 0
        self.tail = self.n

    def append(self, val):
        if self.n == self.a_size - 1:
            self._resize()
        self.a[self.tail] = val
        self.tail = (self.tail + 1) & (self.a_size - 1)
        self.n += 1

    def appendleft(self, val):
        if self.n == self.a_size - 1: 
            self._resize()
        self.head = (self.head - 1) & (self.a_size - 1)
        self.a[self.head] = val
        self.n += 1

    def popleft(self):
        if self.n == 0:
            raise IndexError()
        val = self.a[self.head]
        self.head = (self.head + 1) & (self.a_size - 1)
        self.n -= 1
        if self.a_size >= 4 * self.n + 2:
            self._resize()
        return val

    def pop(self):
        if self.n == 0:
            raise IndexError()
        self.tail = (self.tail - 1) & (self.a_size - 1)
        val = self.a[self.tail]
        self.n -= 1
        if self.a_size >= 4 * self.n + 2:
            self._resize()
        return val


n, q = map(int, input().split())
info = [input().split() for i in range(n)]

que = ArrayDeque()
for name, time in info:
    que.append((name, int(time)))

ans_time = 0
ans = []
while que:
    name, time = que.popleft()
    if time > q:
        que.append((name, time - q))
        ans_time += q
    else:
        ans_time += time
        ans.append((name, ans_time))

for name, time in ans:
    print(name, time)
