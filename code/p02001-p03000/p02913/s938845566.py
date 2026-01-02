class Rori:
  B1 = 1009
  B2 = 1007
  MOD1 = 10 ** 9 + 7
  MOD2 = 10 ** 9 + 9
  H1, H2 = None, None
  P1, P2 = None, None
  def __init__(s, L):
    n = len(L) + 1
    s.H1 = [0] * n
    s.H2 = [0] * n
    s.P1 = [1] * n
    s.P2 = [1] * n
    for i in range(n - 1):
      S = ord(L[i]) - ord('a') + 1
      s.H1[i + 1] = (s.H1[i] * s.B1 + S) % s.MOD1
      s.H2[i + 1] = (s.H2[i] * s.B2 + S) % s.MOD2
      s.P1[i + 1] = s.P1[i] * s.B1 % s.MOD1
      s.P2[i + 1] = s.P2[i] * s.B2 % s.MOD2
  def hashLR(s, l, r):
    t = ((s.H1[r] - s.H1[l] * s.P1[r - l]) % s.MOD1 + s.MOD1) % s.MOD1
    k = ((s.H2[r] - s.H2[l] * s.P2[r - l]) % s.MOD2 + s.MOD2) % s.MOD2
    return (t, k)


class AVL:
  import sys
  sys.setrecursionlimit(1000000)
  class Node:
    def __init__(s, k):
      s.k = k
      s.l = None
      s.r = None
      s.d = 1
  def __init__(s):
    s.x = None
  def l_rot(s, z):
    y = z.r
    t = y.l
    y.l, z.r = z, t
    z.d = s.get_depth(z)
    y.d = s.get_depth(y)
    return y
  def r_rot(s, z):
    y = z.l
    t = y.r
    y.r, z.l = z, t
    z.d = s.get_depth(z)
    y.d = s.get_depth(y)
    return y
  def depth(s, node):
    if not node:
      return 0
    else:
      return node.d
  def get_depth(s, node):
    return 1 + max(s.depth(node.l), s.depth(node.r))
  def add(s, k):
    s.x = s.add_sub(s.x, k)
  def add_sub(s, node, k):
    if not node:
      return s.Node(k)
    elif node.k == k:
      return node
    elif node.k > k:
      node.l = s.add_sub(node.l, k)
    else:
      node.r = s.add_sub(node.r, k)
    node.d = s.get_depth(node)
    bal = s.depth(node.l) - s.depth(node.r)
    if bal > 1:
      if node.l.k > k:
        return s.r_rot(node)
      else:
        node.l = s.l_rot(node.l)
        return s.r_rot(node)
    elif bal < -1:
      if node.r.k < k:
        return s.l_rot(node)
      else:
        node.r = s.r_rot(node.r)
        return s.l_rot(node)
    return node
  def check(s, k):
    return s.check_sub(k, s.x)
  def check_sub(s, k, node):
    if node == None:
      return False
    if node.k == k:
      return True
    if node.k > k:
      return s.check_sub(k, node.l)
    else:
      return s.check_sub(k, node.r)

def hersCode(n):
  ok = 0
  ng = n
  while abs(ok - ng) > 1:
    mid = abs(ok + ng) // 2
    if nasu(mid):
      ok = mid
    else:
      ng = mid
  return ok

def nasu(n):
  L = [None] * (N - n + 1)
  for i in range(len(L)):
    L[i] = R.hashLR(i, i + n)
  T = AVL()
  T.add(L[0])
  for i in range(n, len(L)):
    if T.check(L[i]):
      return True
    T.add(L[i - n + 1])
  return False

def honya(x, y, n):
  for i in range(n):
    if S[x + i] != S[y + i]:
      return i
  return n

N = int(input())
S = input()

R = Rori(S)
print(hersCode(N))
