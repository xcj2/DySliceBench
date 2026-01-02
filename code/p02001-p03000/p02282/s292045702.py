class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder(root, out):
    if root == None:
        pass
    else:
        postorder(root.left, out)
        postorder(root.right, out)
        out.append(root.value)

def build_tree(pres, ins):
    if len(pres) < 1:
        return None
    else:
        node = Node(pres[0])
        index = 0
        for i in range(len(ins)):
            if ins[i] == pres[0]:
                index = i
                break
        
        node.left = build_tree(pres[1:1+index], ins[0:index])
        node.right = build_tree(pres[1+index:], ins[1+index:])
        return node


if __name__ == '__main__':
    n = int(input())
    pres = [int(num) for num in input().split(' ')]
    ins = [int(num) for num in input().split(' ')]
    root = build_tree(pres, ins)
    out = []
    postorder(root, out)
    print(str(out).replace(',', '').replace('[', '').replace(']', ''))

