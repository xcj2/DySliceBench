from collections import deque

def only_color(s):
  temp = s[0]
  for i in range(1, len(s)):
    c = s[i]
    if temp != c:
      return False
    temp = c

  return True

def new_color(s, i):
  color = [c for c in ("r", "g", "b") if c not in (s[i], s[i + 1])][0]
  return s[:i] + color * 2 + s[i + 2:]

def solve(s):
  if only_color(s):
    print(0)
    return
  length = len(s)
  dic = {}
  que = deque()
  que.append((s, 0))

  while que:
    colors, score = que.popleft()
    score += 1
    temp = colors[0]
    for i in range(1, length):
      ci = colors[i]
      if ci != temp:
        new = new_color(colors, i - 1)
        if only_color(new):
          print(score)
          return
        if new not in dic:
          dic[new] = score
          que.append((new, score))
      temp = ci
  else:
    print("NA")

def main():
  while True:
    s = input()
    if s == "0":
      break
    solve(s)

main()
