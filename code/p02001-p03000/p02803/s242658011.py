import sys
import socket
from heapq import heappush, heappop

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('d2.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def dijkstra(a, s):
  i0, j0 = s

  debug = i0 == 1 and j0 == 2

  H = len(a)
  W = len(a[0])
  inf = 1000
  d = [[inf]*W for i in range(H)]
  d[i0][j0] = 0
  q = []
  item = (0, i0, j0)
  heappush(q, item)
  for i in range(H):
    for j in range(W):
      if a[i][j] == '#':
        continue
      v = 0 if (i, j) == s else inf
      item = (v, i, j)
      # heappush(q, item)
  
  # print('q:', q)

  while q != []:
    v, i, j = heappop(q)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for k in range(4):
      ii = i + di[k]
      jj = j + dj[k]
      if not (0 <= ii < H and 0 <= jj < W):
        continue
      if a[ii][jj] == '#':
        continue
      
      # if debug:
      #   print(' ', i, j, ii, jj, d, d[i][j] + 1, d[ii][jj])

      if d[i][j] + 1 < d[ii][jj]:
        d[ii][jj] = d[i][j] + 1
        item = (d[i][j] + 1, ii, jj)
        heappush(q, item)
      # print('  ',  d[ii][jj])  
  return d


def main():
    H, W = read_int_list()
    a = [read_str() for i in range(H)]
    res = 0
    for i in range(H):
      for j in range(W):
        if a[i][j] == '#':
          continue
        s = (i, j)
        d = dijkstra(a, s)
        
        # print('  d:', d)
        # break

        for k in range(H):
          for l in range(W):
            if a[k][l] == '#':
              continue
            if d[k][l] > res:
              res = d[k][l]

    print(res)


def bfs(a, s):
  i0, j0 = s
  H = len(a)
  W = len(a[0])
  inf = 1000
  d = [[inf]*W for i in range(H)]
  d[i0][j0] = 0

  state = [[0] * W for i in range(H)]
  q = []
  q.append(s)
  state[i0][j0] = 1
  while q != []:
    u = q.pop(0)
    i, j = u
    state[i][j] = 2
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for k in range(4):
      ii = i + di[k]
      jj = j + dj[k]
      if not (0 <= ii < H and 0 <= jj < W):
        continue
      if a[ii][jj] == '#':
        continue

      # if d[i][j] + 1 < d[ii][jj]:
      if state[ii][jj] == 0:
        d[ii][jj] = d[i][j] + 1
        q.append((ii, jj))
        state[ii][jj] = 1


  return d


def main2():
    H, W = read_int_list()
    a = [read_str() for i in range(H)]
    res = 0
    for i in range(H):
      for j in range(W):
        if a[i][j] == '#':
          continue
        s = (i, j)
        d = bfs(a, s)
        
        # print('  d:', d)
        # break

        for k in range(H):
          for l in range(W):
            if a[k][l] == '#':
              continue
            if d[k][l] > res:
              res = d[k][l]

    print(res)

main2()
