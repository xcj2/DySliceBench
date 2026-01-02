def gcd(c, d):
  if c < d:
    tmp = d
    d = c
    c = tmp
  ret = c
  if d != 0:
    ret = gcd(d, c % d)
  return ret

def lcm(c, d):
  return (c * d) // gcd(c, d)

def union_cardinality(a_cardi, b_cardi, ab_cardi):
  return a_cardi + b_cardi - ab_cardi

def count_cm(maxi, divi):
  return maxi // divi

def count_cm2(maxi, divi1, divi2):
  num1 = count_cm(maxi, divi1)
  num2 = count_cm(maxi, divi2)
  num12 = count_cm(maxi, lcm(divi1, divi2))
  return union_cardinality(num1, num2, num12)

def count_cm2_band(mini, maxi, divi1, divi2):
  return count_cm2(maxi, divi1, divi2) - count_cm2(mini - 1, divi1, divi2)

a, b, c, d = (int(x) for x in input().split())
print(b - a + 1 - count_cm2_band(a, b, c, d))
