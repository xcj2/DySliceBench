#! /usr/bin/env python3
# -*- coding:utf-8 -*-

def generate_children(num_children, pl):
    children = ["0"]*num_children
    if num_children == 0: return []
    if num_children%2 == 0:
        children[pl-1] = str(int(num_children/2))
        children[pl] = str(int(num_children/2))
    else:
        if (num_children - pl)%2 == 0:
            children[pl-1] = str(int((num_children+1)/2))
            children[pl] = str(int((num_children-1)/2))
        else:
            children[pl-1] = str(int((num_children-1)/2))
            children[pl] = str(int((num_children+1)/2))
    return children


def gathering(s):
    children = []
    pr = 0
    pl = 0
    now = ""
    for i, x in enumerate(s):
        if x == now: continue
        if x == 'L': pl = i
        if x == 'R':
            children.extend(generate_children(i-pr, pl-pr))
            pr = i
        now = x
    children.extend(generate_children(len(s)-pr, pl-pr))
    return ' '.join(children)

def main():
    s = input()
    print(gathering(s))

if __name__ == '__main__':
    main()
