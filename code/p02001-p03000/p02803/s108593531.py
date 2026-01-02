

def read_input():
    h, w = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    cell = lambda x, y : x * w + y

    edges = {}
    for hi in range(h):
        for wi in range(w):
            edges[cell(hi, wi)] = []

            if maze[hi][wi] == "#":
                continue
            if 0 <= hi - 1:
                if maze[hi - 1][wi] == '.':
                    edges[cell(hi, wi)].append(cell(hi - 1, wi))
            if hi + 1 < h:
                if maze[hi + 1][wi] == '.':
                    edges[cell(hi, wi)].append(cell(hi + 1, wi))
            if 0 <= wi - 1:
                if maze[hi][wi - 1] == '.':
                    edges[cell(hi, wi)].append(cell(hi, wi - 1))
            if wi + 1 < w:
                if maze[hi][wi + 1] == '.':
                    edges[cell(hi, wi)].append(cell(hi, wi + 1))

    return h, w, edges, maze


def warshall_floyd(h, w, edges):
    v = h * w
    d = [[v + 1 for _ in range(v)] for _ in range(v)]

    for i in range(v):
        d[i][i] = 0

    for f, tlist in edges.items():
        for t in tlist:
            d[f][t] = 1

    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d   
    

def submit():
    h, w, edges, maze = read_input()
    dist = warshall_floyd(h, w, edges)

    max_dist = 0
    v = h * w
    for i in range(v):
        for j in range(v):
            d = dist[i][j]
            if d > v:
                continue
            if d > max_dist:
                max_dist = d
    print(max_dist)


if __name__ == "__main__":
    submit()