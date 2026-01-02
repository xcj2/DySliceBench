'''
左子右兄弟表現で記載する。
元々の木の形を変形させて保存しておく。
具体的には左の木は自分の子供
右の木は自分の兄弟を連結させる。
深さは親を辿っていって、根につくまで加算することで計算する

'''


class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

    def get_depth(self):
        if self.parent == -1:
            return 0
        else:
            depth = 1
            t = Nodes[self.parent]
            while t.parent != -1:
                t=Nodes[t.parent]
                depth += 1
            return depth

    def get_type(self):
        if self.parent == -1:
            return 'root'
        elif self.left == None:
            return 'leaf'
        else:
            return 'internal node'


def decode_node_data(n):
    '''
    n...受け取る文字列、一行ずつ
    一行ずつ、文字列からノードに変化する
    '''
    global Nodes
    num_of_elem = len(n)
    if num_of_elem < 2:
        raise ValueError
    elif num_of_elem == 2:  # leaf
        pass

    else:
        id, num_of_children = int(n[0]), int(n[1])
        # 子供
        children = n[2:]
        # まず、一人目の子供をとりあえず左に格納する
        Nodes[id].left = int(children[0])
        prev_child = None

        for c in children:
            # 子Nodeの親を登録しておく
            Nodes[int(c)].parent = id
            if prev_child != None:
                # 兄弟の右の木にprev_childを登録する
                Nodes[prev_child].right = int(c)

            # かこに同じdepthの子供がいる場合、それを登録する
            prev_child = int(c)


MAX_NODES = 100001
Nodes = [Node(-1, None, None) for _ in range(MAX_NODES)]

if __name__ == "__main__":

    num_of_nodes = int(input())
    node_data = []
    for _ in range(num_of_nodes):
        node_data.append(input().split(' '))

    for n in node_data:
        decode_node_data(n)

    for node_id in range(num_of_nodes):
        type = Nodes[node_id].get_type()
        children = []
        #葉でなければ子ノードを集める
        if type != 'leaf':
            #左がついてない時はleaf
            if Nodes[node_id].left != None:
                c = Nodes[node_id].left
                children.append(c)
                #右は兄弟なので追加する
                while Nodes[c].right != None:
                    c = Nodes[c].right
                    children.append(c)
        print('node {0}: parent = {1}, depth = {2}, {3}, [{4}]'.format(
            node_id, Nodes[node_id].parent, Nodes[node_id].get_depth(), type,
            ', '.join(map(str, children))))

