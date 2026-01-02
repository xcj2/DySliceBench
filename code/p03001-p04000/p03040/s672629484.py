class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def reset(self):
        t = self.tree
        for i in range(len(t)):
            t[i] = 0

# bit = Bit(10)
# bit.add(1, 1)
# bit.add(1, 1)

# # bit.add(2, 2)
# # bit.add(3, 3)
# print(bit.sum(1))

N=int(input())
queries = [tuple(map(int, input().split())) for _ in range(N)]

numl = []
for q in queries:
    if q[0] == 1:
        numl.append(q[1])
numl.sort()
val_to_key = {}

for i,v in enumerate(numl):
    if not v in val_to_key:
        val_to_key[v] = i

# print(numl)
# print(val_to_key)

cum_b = 0
cum_a = 0
bit = Bit(200005)
bit2 = Bit(200005)
cnt = 0

def abs_sum(mid):
    loc_sum = bit.sum(mid+1)
    lft_cnt = bit2.sum(mid+1)
    lef_sum = numl[mid]*lft_cnt - loc_sum
    rig_sum = cum_a-loc_sum - numl[mid]*(cnt-lft_cnt)
    return lef_sum + rig_sum

def solve(cntmid):
    left = 0
    right = len(numl)
    while left < right:
        mid = (left + right) // 2
        # print(mid+1)
        nums = bit2.sum(mid+1)
        if nums < cntmid:
            left = mid + 1
        else:
            right = mid
    return numl[left], abs_sum(left)+cum_b

for qu in queries:
    if qu[0] ==  1:
        _, a, b = qu
        # print(val_to_key[a])
        bit.add(val_to_key[a]+1, a)
        bit2.add(val_to_key[a]+1, 1)
        cnt += 1
        cum_b += b
        cum_a += a
    else:
        if cnt % 2 == 0:
            sol, val = solve(cnt//2)
            sol2, val2 = solve(cnt//2+1)
            if val > val2: sol, val = sol2, val2
        else:
            sol, val = solve(cnt//2+1)
        print("{} {}".format(sol, val))

# cum = 0
# lis = []
# for _ in range(N):
#     qu=list(map(int, input().split()))
#     if qu[0] == 1:
#         lis.append(qu[1])
#         cum += qu[2]
#     else:
