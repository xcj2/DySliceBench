# ABC 075 B

# H, W = 4, 3
# S = "#.."\
#     "..#"\
#     ".#."\
#     ".#."

H, W = map(int, input().split())
S = ''
for _ in range(H):
    S += input()
    

def cell_of(x, y):
    return S[W*x + y]

def neighbor_indice_of(x, y):
    return [
        (x+m, y+n)
        for m in range(-1, 2)
        for n in range(-1, 2)
        if 0 <= x+m < H and 0 <= y+n < W
    ]

def neighbors_of(x, y):
    return [cell_of(i, j) for i, j in neighbor_indice_of(x, y)]

def mine(x, y):
    cell = cell_of(x, y)
    if cell != '.':
        return cell
    return str(neighbors_of(x, y).count('#'))


for x in range(H):
    print(''.join([mine(x, y) for y in range(W)]))