class Dice(object):
    def __init__(self, nums):
        from collections import deque
        self.ns = deque([nums[4], nums[0], nums[1]])
        self.we = deque([nums[3], nums[0], nums[2]])
        self.bk = deque([nums[5]])

    def __str__(self):
        return str({"ns": self.ns, "we": self.we, "bk": self.bk})

    def operation(self, o):
        if o == "N":
            self.n()
        elif o == "S":
            self.s()
        elif o == "W":
            self.w()
        elif o == "E":
            self.e()
        else:
            raise BaseException("invalid", o)

    def n(self):
        self.ns.append(self.bk.popleft())
        self.bk.append(self.ns.popleft())
        self.we[1] = self.ns[1]

    def s(self):
        self.ns.appendleft(self.bk.pop())
        self.bk.appendleft(self.ns.pop())
        self.we[1] = self.ns[1]

    def w(self):
        self.we.append(self.bk.popleft())
        self.bk.append(self.we.popleft())
        self.ns[1] = self.we[1]

    def e(self):
        self.we.appendleft(self.bk.pop())
        self.bk.appendleft(self.we.pop())
        self.ns[1] = self.we[1]

    def get_top(self):
        return self.ns[1]


def resolve():
    nums = [int(i) for i in input().split()]
    ops = input()
    dc = Dice(nums)
    for o in ops:
        dc.operation(o)
    print(dc.get_top())


resolve()

