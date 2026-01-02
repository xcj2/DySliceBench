
def search_root(x):
    i = x
    while True:
        if i == nodes[i]:
            nodes[x] = i
            return i
        else:
            i = nodes[i]

def unite(x,y):
    nodes[search_root(x)] = search_root(y)

def same(x,y):
    if search_root(x) == search_root(y):
        print(1)
    else:
        print(0)


n, q = map(int, input().split())
nodes = [i for i in range(n)]
commands = []
for _ in range(q):
    commands.append(input())
for cmd in commands:
    c,x,y = map(int,cmd.split())
    if c == 0:
        unite(x,y)
    else:
        same(x,y)

