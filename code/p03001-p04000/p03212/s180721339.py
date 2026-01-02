def abc114_c():
  n = int(input())

  def bit_mask(n):
    b, d = 4, 9  # bit, digit
    arr = []
    for i in range(d-1, -1, -1):
      arr.append(n // (b**i))
      n = n % (b**i)
    ret = str(int(''.join(map(str, arr))))
    return ret

  def decode753(arr):
    ret = ''.join(map(str, arr)).replace('3','7').replace('2','5').replace('1','3')
    return int(ret)

  ans = 0
  b, d = 4, 9
  for m in range(b**d):
    mask = bit_mask(m)
    if mask.count('0') == 0 and mask.count('1') > 0 and mask.count('2') > 0 and mask.count('3') > 0:
      x = decode753(mask)
      if x <= n: ans += 1
      else: break
  print(ans)

abc114_c()