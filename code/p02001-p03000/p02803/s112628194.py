class Node:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.next_nodes = []

    def add_next(self, node):
        self.next_nodes.append(node)


def all_pats():
    pat = []
    for i in range(H):
        for j in range(W):
            pat.append((i, j))
    return pat


def dfs(start):
    queue = []
    queue.append(start)
    count = dict()
    count[start.pos] = 0

    while True:
        if not queue:
            break
        node = queue[0]
        queue = queue[1:]

        for next_node in node.next_nodes:
            if next_node.pos in count:
                continue
            count[next_node.pos] = count[node.pos] + 1
            queue.append(next_node)
    return max(count.values())


H, W = [int(x) for x in input().split(" ")]
nodes = dict()
for i in range(H):
    for j, text in enumerate(input()):
        nodes[(i, j)] = Node(text, (i, j))


for i in range(H):
    for j in range(W):
        node = nodes[(i, j)]
        if node.text == "#":
            continue
        for pos in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if 0 <= pos[0] <= H-1 and 0 <= pos[1] <= W-1 and nodes[pos].text == ".":
                node.add_next(nodes[pos])


all_pats = all_pats()

counts = []
for start in all_pats:
    counts.append(dfs(nodes[start]))

print(max(counts))
