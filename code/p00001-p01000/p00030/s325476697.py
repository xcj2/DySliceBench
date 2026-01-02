class Node():
    def __init__(self, v):
        self.v = v
        self.parent = None
        self.children = []
        self.is_visited = False
    
    def add_child(self, node):
        self.children.append(node)
        node.parent = self


def construct_tree(node):
    start = -1 if node.v is None else node.v
    if node.v == 9:
        return
    for i in range(start + 1, 10):
        new_node = Node(i)
        node.add_child(new_node)
        construct_tree(new_node)

def reset_state(node):
    node.is_visited = False
    for child in node.children:
        reset_state(child)

def find_answer(node, n, s, cnt=0):
    node.is_visited = True
    
    depth, cur_sum = 0, 0
    cur = node
    while cur.parent is not None:
        cur_sum += cur.v
        depth += 1
        cur = cur.parent
    
    if cur_sum == s and depth == n:
        cnt += 1
   
    if depth < n:
        for child in node.children:
            if not child.is_visited:
                cnt = find_answer(child, n, s, cnt)
    
    return cnt

def solve():
    root = Node(None)
    construct_tree(root)
    
    while True:
        n, s = map(int, input().split())
        if n == 0 and s == 0:
            break
        
        count = find_answer(root, n, s)
        print(count)
        reset_state(root)

if __name__ == "__main__":
    solve()

