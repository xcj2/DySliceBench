import sys
sys.setrecursionlimit(10000000)

N = None
As = None
used_plus = 0
used_minus = 0

def make_leaf():
    return [True, None, None, None]

def make_branch(left, right):
    return [False, None, left, right]

def count(nminus):
    global N, As
    res = 0
    for i in range(N):
        if i < nminus:
            res -= As[i]
        else:
            res += As[i]
    return res

def make_tree(a, b):
  if a + b == 1:
      if a == 1:
        return make_leaf()
      else:
          raise Exception("tukurenai")
  else:
      x = 1
      z = 1
      y = b - z
      w = a - x
      return make_branch(make_tree(x, y), make_tree(z, w))


def f(node, minus):
    global N, As, used_plus, used_minus
    [leaf, value, left, right] = node
    if leaf:
        if minus:
            node[1] = As[used_minus]
            used_minus += 1
        else:
            node[1] = As[N - 1 - used_plus]
            used_plus += 1
    else:
        f(left, minus)
        f(right, not minus)

def g(node):
    [leaf, value, left, right] = node
    if leaf:
        return value;
    else:
        x = g(left);
        y = g(right);
        print(str(x) + " " + str(y))
        return x - y

def show(nminus):
    node = make_tree(N - nminus, nminus)
    f(node, False)
    g(node)

def main():
    global N, As
    N = int(input())
    As = list(map(int,input().split()))
    As.sort()
    best = 0
    for i in range(N):
        if As[i] < 0: best = i
    m = -1
    argmax = 0
    for i in range(-1, 2):
        j = min(max(best + i, 1), N - 1)
        c = count(j)
        if c > m:
            m = c
            argmax = j
    print(m)
    show(argmax)

main()