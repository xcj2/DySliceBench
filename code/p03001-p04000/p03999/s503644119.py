s = input()
l = [s[0]]
d = len(s) - 1
if d == 0:
  print(s)
  exit()
def operate_1(string):
  return string
def operate_2(string):
  string += "+"
  return string
# l,d は未定義注意
def bfs(list_hoge = l,depth = 0,deepest = d):
    queue = []
    for e in list_hoge:
        for b in [0,1]:
            if b == 0:
                operated = operate_1(e)
                operated += s[depth + 1]
                queue.append(operated)
            elif b == 1:
                operated = operate_2(e)
                operated += s[depth + 1]
                queue.append(operated)
    list_hoge = queue[:]
    depth += 1
    if depth == deepest:
        return list_hoge
    else:
        return bfs(list_hoge,depth)
ans = 0
for e in bfs():
  ans += eval(e)
print(ans)