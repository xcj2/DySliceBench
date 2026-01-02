import heapq

code_list = dict()

class Node():
    def __init__(self, alphabet, rate):
        self.alphabet = alphabet
        self.rate = rate
        self.left = None
        self.right = None

def create_code(node, target, code):
    
    if node == None:
        return 

    if node.alphabet == target:
        code_list[target] = code
        return
        
    create_code(node.left, target, code + "0")
    create_code(node.right, target, code + "1")

def Main():
    S = input().replace("\n", "")
    N = len(S)

    node_list = list()
    count_list = dict()

    character = set(S)
    character = sorted(character)

    for c in character:
        count = S.count(c)
        count_list[c] = count
        n = Node(c, float(count/N))
        node_list.append(n)

    huf_tree = None

    if len(node_list) == 1:
        n1 = node_list.pop()
        new = Node("", n1.rate)
        new.left = n1

        huf_tree = new

    else:
        while len(node_list) >= 2:
            node_list.sort(key = lambda x : x.rate, reverse = True)

            n1 = node_list.pop()
            n2 = node_list.pop()

            new = Node("", n1.rate + n2.rate)
            new.left = n1
            new.right = n2
            node_list.append(new)

            huf_tree = new

    code_length = 0

    for c in character:
        create_code(huf_tree, c, "")
        code_length += len(code_list[c]) * count_list[c]

    print(code_length)

Main()
