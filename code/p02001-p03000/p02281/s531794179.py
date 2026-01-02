import collections

nil = -1

def preParse(u):
    if u == nil:
        return None
    print(' {}'.format(u), end='')
    preParse(tree[u]['left'])
    preParse(tree[u]['right'])

def inParse(u):
    if u == nil:
        return None
    inParse(tree[u]['left'])
    print(' {}'.format(u), end='')
    inParse(tree[u]['right'])

def postParse(u):
    if u == nil:
        return None
    postParse(tree[u]['left'])
    postParse(tree[u]['right'])
    print(' {}'.format(u), end='')

if __name__ == '__main__':
    n = int(input())
    tree = collections.defaultdict(dict)
    roots = list()
    for _ in range(n):
        id_num, left, right = [int(x) for x in input().split()]
        tree[id_num]['left'] = left
        tree[id_num]['right'] = right
        if left != nil:
            tree[left]['parent'] = id_num
        if right != nil:
            tree[right]['parent'] = id_num
    
    for key, val in tree.items():
        if not 'parent' in tree[key]:
            roots.append(key)
    
    print('Preorder')
    preParse(roots[0])
    print()
    print('Inorder')
    inParse(roots[0])
    print()
    print('Postorder')
    postParse(roots[0])
    print()
