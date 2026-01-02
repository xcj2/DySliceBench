import heapq


class Reverse:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        if len(self.hq) == 0:
            return None
        if self.desc:
            return heapq.heappop(self.hq).val
        else:
            return heapq.heappop(self.hq)

    def push(self, a):
        if self.desc:
            heapq.heappush(self.hq, Reverse(a))
        else:
            heapq.heappush(self.hq, a)


N, M = map(int, input().split())
q = Heapq(list(map(int, input().split())), desc=True)

while M > 0:
    a = q.pop() // 2
    q.push(a)
    M -= 1

tmp = 0
while True:
    try:
        a = q.pop()
        tmp += a
    except:
        break
print(tmp)
