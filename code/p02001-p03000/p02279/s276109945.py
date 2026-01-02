class node:
    def __init__(self, s):
        self.id = int(s.split()[0])
        self.dim = int(s.split()[1])
        self.child_ids = None
        if self.dim>0:
            self.child_ids = list(map(int, s.split()[2:]))
        
        self.pearent = None
        self.child = None
    
    def set_pearent(self, p):
        self.pearent = p
    
    def set_depth(self, d):
        self.depth = d
    
    def set_kind(self, k):
        self.kind = k
    
    def __repr__(self):
        str_node = 'node ' + str(self.id) + ': '
        str_pearent = 'parent = ' + str(self.pearent if self.pearent is not None else -1)
        str_depth = 'depth = ' + str(self.depth)
        str_kind = self.kind
        str_child = '[' + ', '.join([str(i) for i in self.child_ids] if self.child_ids is not None else '') + ']'
        return str_node + ', '.join([str_pearent, str_depth, str_kind, str_child])
        

n = int(input())
inputs = [input() for i in range(n)]
nodes = [0]*n

for i in inputs:
    nd = node(i)
    nodes[nd.id] = nd
    
for nd in nodes:
    if nd.child_ids:
        for i in nd.child_ids:
            nodes[i].set_pearent(nd.id)
            
def get_depth(idx):
    nd = nodes[idx]
    d = 0
    while nd.pearent is not None:
        nd = nodes[nd.pearent]
        d += 1
     
    nodes[idx].depth = d

def get_kind(idx):
    nd = nodes[idx]
    if nd.pearent is None:
        nd.kind = 'root'
    elif nd.child_ids:
        nd.kind = 'internal node'
    else:
        nd.kind = 'leaf'

for i in range(n):
    get_depth(i)
    get_kind(i)

for nd in nodes:
    print(nd)
