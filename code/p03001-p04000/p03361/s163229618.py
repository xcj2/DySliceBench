from itertools import product
from collections import deque
import numpy as np
inputs = open(0).readlines()
class Grid():
    def __init__(self, grid, w=0, h=0, function=lambda x: x):
        self.w = w = w if w else len(grid[0])
        self.h = h = h if h else len(grid)
        dtype = type(function(grid[0][0]))
        self.grid = np.empty((h, w), dtype=dtype)
        for i, row in zip(range(h), grid):
            for j, val in zip(range(w), row):
                self.grid[i][j] = function(val)
    
    def is_valid_x(self, x):
        return 0 <= x < self.w
    def is_valid_y(self, y):
        return 0 <= y < self.h
    def is_valid_xy(self, x, y):
        return self.is_valid_x(x) and self.is_valid_y(y) 
    
    def __iter__(self):
        return iter(self.grid)
    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
    def __getitem__(self, x):
        return self.grid[x]
    def __setitem__(self, x, val):
        self.grid[x] = val

h, w = map(int, inputs[0].split())
grid = Grid(inputs[1:], function=lambda x: int(x == '#'))

def dfs(root):
    count = 1
    stack = [root]
    while stack:
        x, y = stack.pop()
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            if grid.is_valid_xy(x+dx, y+dy) and grid[y+dy, x+dx]:
                stack.append((x+dx, y+dy))
                grid[y+dy, x+dx] = 0
                count += 1
    return count
    
ans = 'Yes'
for i, j in product(range(h), range(w)):
    if grid[i, j]:
        if dfs((j, i)) == 1:
            ans = 'No'
            break
print(ans)