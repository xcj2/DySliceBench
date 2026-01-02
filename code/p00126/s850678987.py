def trans(mp):
  ret = [[None] * 9 for _ in range(9)]
  for x in range(9):
    for y in range(9):
      ret[x][y] = mp[y][x]

  return ret

def fix(mp):
  fix_lst = []
  mp2 = trans(mp)
  for i in range(9):
    for j in range(9):
      if mp[i].count(mp[i][j]) > 1:
        fix_lst.append((i, j))
      if mp2[i].count(mp2[i][j]) > 1:
        fix_lst.append((j, i))

  for ulx in (0, 3, 6):
    for uly in (0, 3, 6):
      tmp = []
      for dx in (0, 1, 2):
        for dy in (0, 1, 2):
          tmp.append(mp[ulx + dx][uly + dy])

      for dx in (0, 1, 2):
        for dy in (0, 1, 2):
          if tmp.count(mp[ulx + dx][uly + dy]) > 1:
            fix_lst.append((ulx + dx, uly + dy))
  
  fix_lst = list(set(fix_lst))
  for x, y in fix_lst:
    mp[x][y] = "*"  + mp[x][y]

  return mp

def _rj(c):
  return c.rjust(2)

def print_mp(mp):
  for line in mp:
    print("".join(map(_rj, line)))

n = int(input())
for i in range(n):
  if i != 0:
    print()
  mp = [input().split() for _ in range(9)]
  mp = fix(mp)
  print_mp(mp)
