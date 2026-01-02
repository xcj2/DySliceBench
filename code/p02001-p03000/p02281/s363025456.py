class Node:
    def __init__(self, node_id, left_child, right_child):
        self.node_id = node_id
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.node_type = ''

        self.left_child = left_child
        self.right_child = right_child
        

def binarytrees():
    def input_node_list():
        n = int(input())

        for i in range(n):
            node_id, left_child, right_child = list(map(int, input().split()))

            node = Node(node_id, left_child, right_child)
            node_list.append(node)

        node_list.sort(key = lambda node: node.node_id)

    def calc_parent_sibling_degree():
        if node.left_child != -1:
            node_list[node.left_child].parent = node.node_id
            node_list[node.left_child].sibling = node.right_child
            node.degree += 1

        if node.right_child != -1:
            node_list[node.right_child].parent = node.node_id
            node_list[node.right_child].sibling = node.left_child
            node.degree += 1

    def calc_depth(node_id):
        if  node_list[node_id].parent == -1:
            return 0
        else:
            return calc_depth(node_list[node_id].parent) + 1

    def calc_height(node_id):
        if node_list[node_id].degree == 0:
            return 0
        else:
            left_height = right_height = 0

            if node_list[node_id].left_child != -1:
                left_height = calc_height(node_list[node_id].left_child)
            if node_list[node_id].right_child != -1:
                right_height = calc_height(node_list[node_id].right_child)

            return max(left_height, right_height) + 1

    def calc_node_type():
        if node.depth == 0:
            node.node_type = 'root'
        elif node.height == 0:
            node.node_type = 'leaf'
        else:
            node.node_type = 'internal node'

    def show_node_info():
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'
            .format(node.node_id, node.parent, node.sibling,
            node.degree, node.depth, node.height, node.node_type))

    node_list = []
    input_node_list()

    for node in node_list:
        calc_parent_sibling_degree()

    # for node in node_list:
    #     node.depth = calc_depth(node.node_id)
    #     node.height = calc_height(node.node_id)

    #     calc_node_type()

    #     show_node_info()

    return node_list

def treewalk():
    def show_preorder(node_id):
        current_node = node_list[node_id]

        print(' {}'.format(current_node.node_id), end='')

        if current_node.left_child != -1:
            show_preorder(current_node.left_child)
        if current_node.right_child != -1:
            show_preorder(current_node.right_child)

    def show_inorder(node_id):
        current_node = node_list[node_id]

        if current_node.left_child != -1:
            show_inorder(current_node.left_child)

        print(' {}'.format(current_node.node_id), end='')

        if current_node.right_child != -1:
            show_inorder(current_node.right_child)

    def show_postorder(node_id):
        current_node = node_list[node_id]

        if current_node.left_child != -1:
            show_postorder(current_node.left_child)
        if current_node.right_child != -1:
            show_postorder(current_node.right_child)

        print(' {}'.format(current_node.node_id), end='')

    node_list = binarytrees()

    root_id = 0
    for node in node_list:
        if node.parent == -1:
            root_id = node.node_id
    
    print('Preorder')
    show_preorder(root_id)
    print('')

    print('Inorder')
    show_inorder(root_id)
    print('')

    print('Postorder')
    show_postorder(root_id)
    print('')

if __name__ == '__main__':
    treewalk()