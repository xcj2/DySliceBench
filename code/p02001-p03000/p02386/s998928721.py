from itertools import combinations

class Dice(object):

    def __init__(self, nums):
        self.nums = nums
        self.ifaces = [(1,2,3), (2,3,1), (3,1,2),
                       (1,4,2), (4,2,1), (2,1,4),
                       (1,5,4), (5,4,1), (4,1,5),
                       (1,3,5), (3,5,1), (5,1,3),
                       (2,6,3), (6,3,2), (3,2,6),
                       (2,4,6), (4,6,2), (6,2,4),
                       (4,5,6), (5,6,4), (6,4,5),
                       (3,6,5), (6,5,3), (5,3,6),]

    def index(self, num):
        return self.nums.index(num)

    def face(self, iface):
        return [self.nums[i-1] for i in iface]

    def all_face(self):
        for iface in self.ifaces:
            yield self.face(iface)

def is_same(d1, d2):
    for f1 in d1.all_face():
        found = False
        for f2 in d2.all_face():
            if f1 == f2:
                found = True
                break
        if not found:
            return False
    return True

n = int(input())

dices = []
for _ in range(n):
    dices.append(Dice([int(i) for i in input().split()]))

ans = True
for c in combinations(dices, 2):
    if is_same(c[0], c[1]):
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')
