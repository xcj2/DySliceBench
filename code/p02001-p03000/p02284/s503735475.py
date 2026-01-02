import sys
sys.setrecursionlimit(2**20)

class Node:
    
    def __init__(self, parent=None, left=None, right=None) -> None:
        self.parent = parent
        self.left = left
        self.right = right

def pre_parse(T: dict, u: int, pre_ls: list):
    if u is None:
        return
    pre_ls.append(u)
    pre_parse(T, T[u].left, pre_ls)
    pre_parse(T, T[u].right, pre_ls)

def in_parse(T: dict, u: int, in_ls: list):
    if u is None:
        return
    in_parse(T, T[u].left, in_ls)
    in_ls.append(u)
    in_parse(T, T[u].right, in_ls)


def insert(T: dict, ROOT: int , z: int):
    if ROOT == z:
        T[z] = Node()
    else:
        T[z] = Node()
        x = ROOT
        while x is not None: #子ノードがNoneになったらbreak
            next_parent = x
            if z < x: # 新たなノードが現在のノードより小さければ左の子ノードへ。
                x = T[x].left
            else:
                x = T[x].right
        T[z].parent = next_parent
        if z < next_parent: # 親より小さければ左の子ノードとして付ける
            T[next_parent].left = z
        else:
            T[next_parent].right = z

def find(T: dict, ROOT: int, k: int):
    """
    Tからkを見つけ出す。見つからなかったらNoneを返す
    """
    x = ROOT
    while x is not None and x != k:
        if k < x:
            x = T[x].left
        else:
            x = T[x].right
    return x

def delete_node(T: dict, z: int):
    # 1. zが子を持たない場合
    parent = T[z].parent
    if (T[z].left is None) and (T[z].right is None):
        # zを削除
        if T[parent].left == z:
            T[parent].left = None
        elif T[parent].right == z:
            T[parent].right = None
        else:
            raise ValueError
        del T[z]
    
    # 2. zがちょうど1つの子を持つ場合
    elif T[z].right is None:
        # 左だけ子がある場合
        is_z_left = True if T[parent].left == z else False
        child = T[z].left
        if is_z_left: # zが、zの親の左側の子なら
            T[parent].left = child
        else: # zが、zの親の右側の子なら
            T[parent].right = child
        T[child].parent = parent
        del T[z]
    
    elif T[z].left is None:
        # 右だけ子がある場合
        is_z_left = True if T[parent].left == z else False
        child = T[z].right
        if is_z_left: # zが、zの親の左側の子なら
            T[parent].left = child
        else: # zが、zの親の右側の子なら
            T[parent].right = child
        T[child].parent = parent
        del T[z]
    
    elif (T[z].left is not None) and (T[z].right is not None):
        left, right = T[z].left, T[z].right
        # 指定したノードの子孫の中で最も小さいノードを返す
        node_next_more = get_min_descendants(T, T[z].right)
        next_more_right = T[node_next_more].right
        next_more_parent = T[node_next_more].parent
        # z がROOTだったら
        if parent is None:
            if node_next_more == right:
                T[right].parent = None
                T[right].left = left
                ROOT = right
                del T[z]
                return
            else:
                # node_next_moreがもっと下にある場合
                T[node_next_more].left = left
                T[node_next_more].right = right
                T[node_next_more].parent = None
                T[left].parent = node_next_more # zの左側の子の親
                T[right].parent = node_next_more # zの右側の子の親
                # node_next_moreの親 -> node_next_more右子の接続
                T[next_more_parent].left = next_more_right
                if next_more_right is not None:
                    T[next_more_right].parent = next_more_parent
                
                del T[z]
                return
        
        else: # zが非ROOTだったら
            is_z_left = True if T[parent].left == z else False
            if node_next_more == right:
                # zをつぶしてzの(元)親の子の枠のうち、もともとｚがいた方に、zの右子を繋げる
                if is_z_left:
                    T[parent].left = right
                else:
                    T[parent].right = right
                T[right].parent = parent
                T[right].left = left
                del T[z]
                return
            else:
                # zの親->next_more
                if is_z_left:
                    T[parent].left = node_next_more
                else:
                    T[parent].right = node_next_more
                # next_more -> z の子
                T[node_next_more].left = left
                T[node_next_more].right = right
                T[node_next_more].parent = parent
                T[left].parent = node_next_more # ｚの左の接続
                T[right].parent = node_next_more # zの右の接続
                # node_next_moreの親 -> node_next_more右子の接続
                # (node_next_moreの親から見ると左に接続される)
                # next_moreはzの親と子の間に繋ぎ変えたので、
                # next_more_parentとnext_more_rightを繋げる。
                T[next_more_parent].left = next_more_right
                if next_more_right is not None:
                    # next_moreの右子があるなら、next_moreの分だけ詰める
                    T[next_more_right].parent = next_more_parent
                
                del T[z]
                return

def get_min_descendants(T:dict, z:int):
    x = z
    while T[x].left is not None:
        x = T[x].left
    return x

def print_result(T: dict, ROOT: int):
    pre_ls, in_ls = [], []
    in_parse(T, ROOT, in_ls)
    pre_parse(T, ROOT, pre_ls)
    print("", *in_ls)
    print("", *pre_ls)

def main():
    N = int(input())
    T = {}
    ROOT = 0
    for i in range(N):
        tmp = input().split()
        if tmp[0] == "insert":
            value = int(tmp[1])
            if i==0:
                ROOT = value
            insert(T, ROOT, value)
        elif tmp[0] == "find":
            value = int(tmp[1])
            if find(T, ROOT, value):
                print("yes")
            else:
                print("no")
        elif tmp[0] == "delete":
            value = int(tmp[1])
            delete_node(T, value)
        else:
            print_result(T, ROOT)

main()

