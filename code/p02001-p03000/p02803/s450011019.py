# -*- coding: utf-8 -*-

from queue import Queue

def main():
     h, w = map(int, input().split())
     maze = list()
     ans = -1

     for i in range(h):
          maze.append(list(input()))
     # print(maze)

     for i in range(h):
          for j in range(w):
               ans = max(ans, solver(maze, h, w, i, j))
     
     print(ans)

def solver(maze, h, w, i, j):
     # スタート地点が壁の場合、return
     if maze[i][j] == '#':
          return -1

     # スタート地点が道の場合、探索
     solve = [['inf' for x in range(w)] for y in range(h)]
     check = [[False for x in range(w)] for y in range(h)]
     q = Queue()

     # スタート地点をキューに登録
     solve[i][j] = 0
     q.put((i, j))
     check[i][j] = True

     # スタート地点から探索
     while(not q.empty()):
          # baseを取り出す
          point = q.get()
          # print(point)
          # up:
          if point[0] - 1 >= 0:
               target = (point[0] - 1, point[1])
               if maze[target[0]][target[1]] == '.':
                    solve[target[0]][target[1]] = checker(solve[target[0]][target[1]], solve[point[0]][point[1]] + 1)
                    if not check[target[0]][target[1]]:
                         q.put(target)
                         check[target[0]][target[1]] = True

          # down
          if point[0] + 1 < h:
               target = (point[0] + 1, point[1])
               if maze[target[0]][target[1]] == '.':
                    solve[target[0]][target[1]] = checker(solve[target[0]][target[1]], solve[point[0]][point[1]] + 1)
                    if not check[target[0]][target[1]]:
                         q.put(target)
                         check[target[0]][target[1]] = True

          # left
          if point[1] - 1 >= 0:
               target = (point[0], point[1] - 1)
               if maze[target[0]][target[1]] == '.':
                    solve[target[0]][target[1]] = checker(solve[target[0]][target[1]], solve[point[0]][point[1]] + 1)
                    if not check[target[0]][target[1]]:
                         q.put(target)
                         check[target[0]][target[1]] = True

          # right
          if point[1] + 1 < w:
               target = (point[0], point[1] + 1)
               if maze[target[0]][target[1]] == '.':
                    solve[target[0]][target[1]] = checker(solve[target[0]][target[1]], solve[point[0]][point[1]] + 1)
                    if not check[target[0]][target[1]]:
                         q.put(target)
                         check[target[0]][target[1]] = True

     # print(solve)
     # print(check)

     ret = 0
     for i in range(h):
          line = [x for x in solve[i] if type(x) == int]
          if not len(line) == 0:
               ret = max(ret, max(line))

     return ret


def checker(now, new):
     if now == 'inf':
          return new
     else:
          return min(now, new)


if __name__ == "__main__":
    main()
