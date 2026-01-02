class queue():
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.MAX = 100000
        self.Q = [[0] for i in range(self.MAX)]

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % self.MAX

    def enqueue(self, x):
        if self.is_full():
            raise ValueError("エラー（オーバーフロー）")
        self.Q[self.tail] = x
        if self.tail + 1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("エラー（アンダーフロー）")
        x = self.Q[self.head]
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x

n, q = input().split(" ")
n = int(n)
q = int(q)
q_name = queue()
q_val = queue()
for i in range(n):
    name, t = input().split(" ")
    t = int(t)
    q_name.enqueue(name)
    q_val.enqueue(t)

results = []
end_time = 0
while True:
    process_val = q_val.dequeue()
    process_name = q_name.dequeue()
    if process_val <= q:
        end_time += process_val
        results.append([process_name, end_time])
    else:
        end_time += q
        rest_val = process_val - q
        q_name.enqueue(process_name)
        q_val.enqueue(rest_val)
    
    if q_val.head == q_val.tail:
        break

for v in results:
    print("{} {}".format(v[0],v[1]))
