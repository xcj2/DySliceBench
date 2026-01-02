import sys
sys.setrecursionlimit(2**20)#再帰回数上限の向上

class Node():
    def __init__(self, parent = None, left = None, right = None):
        self.parent = parent
        self.left = left
        self.right = right

def pre_parse(T:dict, u: int, pre_lis: list):
    if u == None:
        return
    pre_lis.append(u)
    pre_parse(T, T[u].left, pre_lis)
    pre_parse(T, T[u].right, pre_lis)

def in_parse(T,u,in_lis):
    if u == None:
        return
    in_parse(T, T[u].left, in_lis)
    in_lis.append(u)
    in_parse(T, T[u].right, in_lis)

def insert(T, Root, z):
    #zは接点番号（そして接点番号が内容でもある）
    #この接点番号を二分探索木の条件に従うように挿入する
    #もしＴが空なら
    if Root == z:
        T[z] = Node()
    #もしTにいくつか入っていた場合
    else:
        T[z] = Node()#初期化
        x = Root
        while x is not None:
            #子供がNoneになったらbreakする。next_parentが挿入するものの親
            next_parent = x
            if x > z:
                x = T[x].left
                temp = 1
            else:
                x = T[x].right
                temp = 2

        T[z].parent = next_parent
        if temp == 1:
            T[next_parent].left = z
        else:
            T[next_parent].right = z

def find(T,Root,k):
    #Tからkを見つけ出す。ひたすらkの大きさによって左右のパスをたどっていくだけ。
    x = Root
    while x != None and x != k:
        if k < x:
            x = T[x].left
        else:
            x = T[x].right
    return x

def delete_node(T,z):
    # case1指定したzが子を持たないとき
    parent = T[z].parent
    if (T[z].left is None) and (T[z].right is None):
        #そのノードを消去する
        if T[parent].left == z:
            T[parent].left = None
        elif T[parent].right == z:
            T[parent].right = None
        else:
            raise ValueError("something wrong in case 1")

        del T[z]

    #case2 指定した子が一つの子を持つ場合
    elif T[z].right is None:
        #左の子だけある場合、左の子ノードを親に繋ぐ
        #親の左右どちらかにつけるかはzの繋がり方に依存する。
        z_is_left = True if T[parent].left == z else False
        child = T[z].left
        if z_is_left:
            T[parent].left = child
            T[child].parent = parent
            del T[z]
        else:
            T[parent].right = child
            T[child].parent = parent
            del T[z]

    elif T[z].left is None:
        z_is_left = True if T[parent].left == z else False
        child = T[z].right
        if z_is_left:
            T[parent].left = child
        else:
            T[parent].right = child
        T[child].parent = parent
        del T[z]

    #case3 zが二つの子を持つ場合
    elif (T[z].left is not None) and (T[z].right is not None):
        left, right = T[z].left, T[z].right
        #指定したノードの右部分木の中の子孫の中で最も小さいノードをもらう
        node_next_more = get_min_in_descendants(T,T[z].right)
        next_more_right = T[node_next_more].right
        next_more_parent = T[node_next_more].parent
        #zがRootなら
        if parent is None:
            if node_next_more == right:
                #node_next_moreがrightの場合
                T[right].parent = None
                T[right].left = left
                Root = right
                del T[z]
                return

            else:
                #node_next_moreがもっと下流に存在する場合
                #zの子と親の接続
                T[node_next_more].left = left
                T[node_next_more].right = right
                T[node_next_more].parent = None
                T[left].parent = node_next_more
                T[right].parent = node_next_more
                if next_more_right is not None:
                    T[next_more_right].parent = next_more_parent
                    T[next_more_parent].left = next_more_right
                Root = node_next_more
                del T[z]
                return

        else:
            #zが非Root
            #zが親から見てどっち側についているか
            z_is_left = True if T[parent].left == z else False
            if node_next_more == right:
                if z_is_left:
                    T[parent].left = node_next_more
                else:
                    T[parent].right = node_next_more

                T[node_next_more].parent = parent
                T[node_next_more].left = left
                del T[z]
                return
            else:
                #zの親とnext_moreの接続
                if z_is_left:
                    T[parent].left = node_next_more
                else:
                    T[parent].right = node_next_more

                #next_moreと子供との接続
                T[node_next_more].left = T[z].left
                T[node_next_more].right = T[z].right
                T[node_next_more].parent = parent
                T[left].parent = node_next_more
                T[right].parent = node_next_more

                T[next_more_parent].left = next_more_right
                if next_more_right is not None:
                    T[next_more_right].parent = next_more_parent

                del T[z]
                return

def get_min_in_descendants(T,z):
    x = z
    while T[x].left is not None:
        x = T[x].left

    return x

def print_result(T):
    pre_ls = []
    in_ls = []
    in_parse(T,Root,in_ls)
    pre_parse(T,Root,pre_ls)
    print('', *in_ls)
    print('', *pre_ls)

N = int(input())
T = {}
for i in range(N):
    tmp = input()
    if tmp.startswith('print'):
        print_result(T)
    elif tmp.startswith('insert'):
        z = int(tmp.split()[1])
        if i == 0:
            Root = z
        insert(T,Root,z)
    elif tmp.startswith('find'):
        z = int(tmp.split()[1])
        if find(T,Root,z) is None:
            print('no')
        else:
            print('yes')
    elif tmp.startswith('delete'):
        z = int(tmp.split()[1])
        delete_node(T,z)

