import sys
import time
input = sys.stdin.readline

def left_rot(node):
    s = node['right'].copy()
    node['right'] = s['left']#.copy()
    s['left'] = node
    return s

def right_rot(node):
    s = node['left'].copy()
    node['left'] = s['right']#.copy()
    s['right'] = node
    return s

def insert(node,k,p):
    if(node is None):
        child = {
            'left' : None,
            'right' : None,
            'key' : k,
            'priority' : p}
        return child
    if(k == node['key']):
        return node
    # Left side
    if(k < node['key']):
        node['left'] = insert(node['left'],k,p)
        #追加したらあとは優先度による回転を行う
        if(node['priority'] < node['left']['priority']):
            node = right_rot(node)
    # Right side
    else:
        node['right'] = insert(node['right'],k,p)
        #追加したらあとは以下略
        if(node['priority'] < node['right']['priority']):
            node = left_rot(node)

    return node

def find(node, k):
    if(node is None):
        return 'no'
    if(node['key'] == k):
        return 'yes'
    if(k < node['key']):
        return find(node['left'],k)
    else:
        return find(node['right'],k)

def delete(node, k):
    if(node is None):
        return None

    if(node['key'] == k):
        if(node['left'] is None and node['right'] is None):
            return None
        elif(node['left'] is None):
            node = left_rot(node)
        elif(node['right'] is None):
            node = right_rot(node)
        else:
            if(node['left']['priority'] > node['right']['priority']):
                node = right_rot(node)
            else:
                node = left_rot(node)
        return delete(node, k)
    if(k < node['key']):
        node['left'] = delete(node['left'], k)
    else:
        node['right'] = delete(node['right'], k)

    return node

def print_treap(node,values):
    if(node is None):
        return values
    values.append(node['key'])
    values = print_treap(node['left'],values)
    values = print_treap(node['right'],values)
    return values

num = int(input())
req = [input().split() for _ in range(num)]
node = None
values = []
for q in req:
    if(q[0] == 'insert'):
        node = insert(node, int(q[1]),int(q[2]))
    elif(q[0] == 'find'):
        print(find(node,int(q[1])))
    elif(q[0] == 'delete'):
        node = delete(node, int(q[1]))
    else:
        print_treap(node, values)
        print(" "+" ".join(map(str, sorted(values))))
        print(" "+" ".join(map(str, values)))
        values.clear()

