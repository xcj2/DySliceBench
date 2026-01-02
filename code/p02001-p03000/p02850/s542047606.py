from collections import deque

N = int(input())
vertex_neighbor_vertices = {}  # 各頂点と、その頂点に隣接する頂点リストのマップ
vertex_colors = {}  # 各頂点と、その頂点を端点に持つ辺に塗られた色セットのマップ
sides = []  # 辺情報（(a_i, b_i)のタプル形式で、順番を保持）
side_color = {}  # 辺とその辺に塗られた色のマップ


def add_neighbors(start, end):
    neighbors_of_s = set()
    if start in vertex_neighbor_vertices:
        neighbors_of_s = vertex_neighbor_vertices[start]
    else:
        vertex_neighbor_vertices[start] = neighbors_of_s
    neighbors_of_s.add(end)


def init_colors(vertex):
    colors = set()
    if vertex not in vertex_colors:
        vertex_colors[vertex] = colors


def get_unused_color(colors_of_sv, colors_of_ev, color_start):
    for i in range(color_start, N + 1):
        if (i not in colors_of_sv) and (i not in colors_of_ev):
            return i


for i in range(N - 1):
    s, e = map(int, input().split())
    sides.append((s, e))
    add_neighbors(s, e)
    add_neighbors(e, s)
    init_colors(s)
    init_colors(e)

max_color_num = 0
max_neighbor_vertex = 0
for k, v in vertex_neighbor_vertices.items():
    if len(v) > max_color_num:
        max_color_num = len(v)
        max_neighbor_vertex = k

print(max_color_num)

# 辺を最も多く持つ頂点を起点に、幅優先探索で辺を色付けしていく
visited = set()
q = deque([max_neighbor_vertex])

while q:
    vertex = q.popleft()
    visited.add(vertex)
    # 色付け
    color_start = 1
    for neighbor in vertex_neighbor_vertices[vertex]:
        if neighbor in visited:
            continue
        q.append(neighbor)
        color = get_unused_color(vertex_colors[vertex], vertex_colors[neighbor], color_start)
        color_start = color + 1
        vertex_colors[vertex].add(color)
        vertex_colors[neighbor].add(color)
        side_color[(vertex, neighbor)] = color

for s, e in sides:
    color = 0
    if (s, e) in side_color:
        color = side_color[(s, e)]
    else:
        color = side_color[(e, s)]
    print(color)
