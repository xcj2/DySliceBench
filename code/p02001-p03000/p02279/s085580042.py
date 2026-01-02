from typing import List

class Node:
    def __init__(self, node_id, parent_id):
        self.node_id = node_id
        self.parent_id = parent_id
        self.children = []
        
        self.depth = None
        self.node_type =None

    def __str__(self):
        return str(self.node_id)
    def __repr__(self):
        return self.__str__()
        
    
class Tree:
    def __init__(self, n):
        self.root = None
        self.n_node = n
        self.node_list = [None for _ in range(n)]
    
    def find_node(self, node_id: int):
        if self.node_list[node_id] != None:
            return self.node_list[node_id]
        return None
    
    def add_children_from_ids(self, node_id: int, children_ids: List[int]):
        # check parent already exists
        parent_node = self.find_node(node_id)
        if parent_node == None:
            # create new node from parent_id
            parent_node = Node(node_id = node_id, parent_id = -1)
            self.node_list[node_id] = parent_node
            
        if len(children_ids) > 0:
            # add all the children (unregistered)
            # register parent_id, node_id, children
            for child_id in children_ids:
                child_node = self.find_node(child_id)
                
                if child_node == None:
                    child_node = Node(node_id = child_id, parent_id = node_id)
                else:
                    child_node.parent_id = node_id
                    
                parent_node.children.append(child_node)
                self.node_list[child_id] = child_node
    
    def overwrite_node_type(self):
        # find root and overwrite node type
        
        for node in self.node_list:
            # root, internal node, leaf
            if node.parent_id == -1:
                node_type = "root"
                self.root = node
            else:
                if node.children != []:
                    node_type = "internal node"
                else:
                    node_type = "leaf"
                    
            node.node_type = node_type

    def overwrite_depth(self, node, depth):
        if node.children == []:
            node.depth = depth
            # print("node.id: ", node.node_id, ",  node.depth: ", node.depth)
            return None
        else:
            node.depth = depth
            for child_node in node.children:
                self.overwrite_depth(child_node, depth+1)
        return None

    def print_nodes(self):
        for node in self.node_list:
            print("node {}: parent = {}, depth = {}, {}, {}".format(
                node.node_id, node.parent_id, node.depth, node.node_type, node.children
            ))            
  
def main():
    n = int(input())
    tree = Tree(n)
    for _ in range(n):
        node_id, k, *children = map(int, input().split())
        tree.add_children_from_ids(node_id = node_id, children_ids = children)
    tree.overwrite_node_type()

    tree.overwrite_depth(tree.root, 0)
    tree.print_nodes()    
main()

