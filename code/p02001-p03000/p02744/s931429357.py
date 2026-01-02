# -*- coding: utf-8 -*-

min_char = "abcdefghij"

def dtype_tree(tree, max, num):
    for i in range(max+1):
        tgt_tree = [i]
        if num > 0:
            new_max = max
            if new_max < i+1:
                new_max = i+1
            new_tree = dtype_tree([], new_max, num-1)
            tgt_tree.append(new_tree)

        if tree == None:
            tree = tgt_tree
        else:
            tree.append(tgt_tree)
    return tree

def print_tree(tree, prefix):
    new_prefix = prefix
    if len(tree) == 1:
        print(prefix + min_char[tree[0]])
    else:
        for elem in tree:
            if type(elem) != list:
                new_prefix += min_char[elem]
#                print(new_prefix)
            else:
                print_tree(elem, new_prefix)

    return


def abc_XXX(num):
    tree = dtype_tree(None, 0, num-1)
#    print(tree)
    print_tree(tree, "")
    return

###
# main
if(__name__ == '__main__'):
    # input
    n = int(input())
    
    abc_XXX(n)
    
    # output

# else:
    # do nothing
