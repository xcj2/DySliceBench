n = int(input())
a = [int(item) for item in input().split()]
a_sorted = sorted(a)

def can_be_midofmid(b):
    high_low_cum = [0] * (n + 1)
    for i, item in enumerate(a):
        if item >= b:
            high_low_cum[i+1] = 1
        else:
            high_low_cum[i+1] = -1
    for i in range(n):
        high_low_cum[i+1] += high_low_cum[i]
    bit_n = 1 << n.bit_length()
    bit = [0] * (bit_n+1)

    def bit_add(x, w):
        while x <= bit_n:
            bit[x] += w
            x += x & -x

    def bit_sum(x):
        ret = 0
        while x > 0:
            ret += bit[x]
            x -= x & -x
        return ret

    val = 0
    dic = dict(zip(sorted(high_low_cum), [item for item in range(len(high_low_cum))]))
    for i, item in enumerate(high_low_cum):
        val += bit_sum(dic[item] + 1)
        bit_add(dic[item] + 1, 1)
    return val  >= ((n+1) * n + 2)// 4  

l = -1; r = n
while r - l > 1:
    mid = (r + l) // 2
    if can_be_midofmid(a_sorted[mid]):
        l = mid
    else:
        r = mid
print(a_sorted[r-1])