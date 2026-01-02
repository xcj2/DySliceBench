def main():
  n, m = map(int, input().split())
  s = input()
  mem = set()
  base = ord("a") - 1
  mod1 = 1000000007
  mod2 = 2147483647
  h1 = [0]
  h2 = [0]
  for c in s:
    h1.append((h1[-1] * 27 + ord(c) - base) % mod1)
    h2.append((h2[-1] * 27 + ord(c) - base) % mod2)
  pow_mem1 = {0:1}
  pow_mem2 = {0:1}
  def my_pow1(x):
    if x in pow_mem1:return pow_mem1[x]
    pow_mem1[x] = my_pow1(x - 1) * 27 % mod1
    return pow_mem1[x]

  def my_pow2(x):
    if x in pow_mem2:return pow_mem2[x]
    pow_mem2[x] = my_pow2(x - 1) * 27 % mod2
    return pow_mem2[x]
  
  left = right = 1
  for _ in range(m):
    com = input()
    if com == "L++":
      left += 1
    if com == "L--":
      left -= 1
    if com == "R++":
      right += 1
    if com == "R--":
      right -= 1
    x = (h1[right] - h1[left - 1] * my_pow1(right - left + 1)) % mod1
    y = (h2[right] - h2[left - 1] * my_pow2(right - left + 1)) % mod2
    mem.add((x, y))

  print(len(mem))

main()
