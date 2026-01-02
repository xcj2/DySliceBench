s = list(input())
d = 3
def operate1(string):
  string += "-"
  return string
def operate2(string):
  string += "+"
  return string
def bfs(list_hoge = [s[0]],depth = 0,deepest = d):
    queue = []
    for e in list_hoge:
        for b in [0,1]:
            if b == 0:
                operated = operate1(e)
                operated += s[depth + 1]
                queue.append(operated)
            elif b == 1:
                operated = operate2(e)
                operated += s[depth + 1]
                queue.append(operated)
    list_hoge = queue[:]
    depth += 1
    if depth == deepest:
        return list_hoge
    else:
        return bfs(list_hoge,depth)
for e in bfs():
  if eval(e) == 7:
    print(e + "=7")
    break