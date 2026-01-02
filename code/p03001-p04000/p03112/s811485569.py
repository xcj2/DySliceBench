from bisect import bisect_left, bisect_right
mx = 10**10

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

a, b, q = map(int, input().split())
aa = []
bb = []
for i in range(a):
  aa.append(int(input()))
for i in range(b):
  bb.append(int(input()))

aa.append(mx * 2)
bb.append(mx * 2)
aa.insert(0, -mx * 2)
bb.insert(0, -mx * 2)
#print(f'aa={aa}, bb={bb}')

for i in range(q):
  qi = int(input())
  #print(f'q = {qi}')

  a_low = find_lt(aa, qi)
  a_high = find_gt(aa, qi)

  b_low = find_lt(bb, qi)
  b_high = find_gt(bb, qi)

  len1 = qi - min([a_low, b_low])
  len2 = max([a_high, b_high]) - qi
  len3 = (a_high - qi) + (a_high - b_low)
  len4 = (b_high - qi) + (b_high - a_low)
  len5 = (qi - b_low) + (a_high - b_low)
  len6 = (qi - a_low) + (b_high - a_low)
  lens = [len1, len2, len3, len4, len5, len6]
  print(min(lens))

