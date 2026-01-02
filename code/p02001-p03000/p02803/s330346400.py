from copy import deepcopy
from collections import deque
from itertools import product
import numpy as np
inputs = open(0).readlines()
class Grid():
    def __init__(self, grid, w=0, h=0, function=lambda x: x):
        self.w = w = w if w else len(grid[0])
        self.h = h = h if h else len(grid)
        dtype = type(function(grid[0][0]))
        self.grid = np.empty((h, w), dtype=dtype)
        for i, rows in zip(range(h), grid):
            for j, val in zip(range(w), rows):
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
        return '\n'.join([' '.join(map(str, rows)) for rows in self.grid])
    def __getitem__(self, x):
        return self.grid[x]
    def __setitem__(self, x, val):
        self.grid[x] = val
h, w = map(int, inputs[0].split())
grid_origin = Grid(inputs[1:], function=lambda x: int(x == '.'))

def bfs(root):
    queue = deque([root])
    while queue:
        x, y, d = queue.popleft()
        d += 1
        grid[y, x] = 0
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            if grid.is_valid_xy(x+dx, y+dy) and grid[y+dy, x+dx]:
                queue.append((x+dx, y+dy, d))
                grid[y+dy, x+dx] = 0
    return d-1
    
ans = 0
for i, j in product(range(h), range(w)):
    if grid_origin[i, j]:
        grid = deepcopy(grid_origin)
        ans = max(ans, bfs((j, i, 0)))
print(ans)