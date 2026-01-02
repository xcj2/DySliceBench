T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

def cross_foo(turn):
  posA1 = (T1 * A1 + T2 * A2) * (turn - 1)
  posB1 = (T1 * B1 + T2 * B2) * (turn - 1)
  posA2 = posA1 + T1 * A1
  posB2 = posB1 + T1 * B1
  if (posA1 - posB1 == 0): return False
  return ((posA1 - posB1) * (posA2 - posB2) <= 0)

def cross_bar(turn):
  posA1 = (T1 * A1 + T2 * A2) * (turn - 1) + T1 * A1;
  posB1 = (T1 * B1 + T2 * B2) * (turn - 1) + T1 * B1;
  posA2 = posA1 + T2 * A2;
  posB2 = posB1 + T2 * B2;
  if (posA1 - posB1 == 0): return False
  return ((posA1 - posB1) * (posA2 - posB2) <= 0)

def main():
  if (T1 * A1 + T2 * A2 == T1 * B1 + T2 * B2):
    print("infinity")
    return

  if (not cross_bar(1)):
    print(0)
    return

  if (not cross_foo(2)):
    print(1)
    return

  ans = 0

  foo_ok = 2
  foo_ng = 1
  for i in range(110):
    foo_ng *= 10
  while (foo_ok < foo_ng - 1):
    mid = int((foo_ok + foo_ng) / 2)
    if (cross_foo(mid)): foo_ok = mid
    else: foo_ng = mid
  ans += foo_ok - 1

  bar_ok = 1
  bar_ng = 1
  for i in range(110):
    bar_ng *= 10
  while (bar_ok < bar_ng - 1):
    mid = int((bar_ok + bar_ng) / 2)
    if (cross_bar(mid)): bar_ok = mid
    else: bar_ng = mid;
  ans += bar_ok

  print(ans)

main()
