def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))


def convert(nums):
    # print('conv', [2**i for i in nums])
    return sum([2**i for i in nums])


def is_on(ons, bulb, p):
    return bin(ons & bulb).count('1') % 2 == p

def is_all_on(ons, bulbs, ps):
    res = True
    for bulb, p in zip(bulbs, ps):
        # print(ons, bulb, is_on(ons, bulb, p))
        res &= is_on(ons, bulb, p)
    return res


n, m = LI()
k, s = [], []
for _ in range(m):
    _input = LI_()
    s.append(convert(_input[1:]))
    # print('s', _input[1:])

p = LI()

res = 0
for ons in range(2**n):
    res += is_all_on(ons, s, p)

print(res)
