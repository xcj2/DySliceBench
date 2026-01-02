class Node():
    """節クラス: valは節の値, parent/left/rightはそれぞれ親/左側の子/右側の子へのポインタを表す"""
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.right = None
        self.left = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def search(self, val: int) -> bool:
        """二分木に値valを持つ節が存在するかどうか判定する
        根から順番に子を辿っていき、valと一致する節が存在する場合はTrue、存在しない場合はFalseを返す
        """
        ptr = self.root
        while ptr is not None:
            if ptr.val == val:
                return True
            if val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False 

    def insert(self, val: int):
        """二分木に値valを持つ節を追加する（すでに二分木内に同じ要素が存在している場合も追加する）
        根から順番に子を辿っていき、ポインタが示す先に節が存在しなくなったらNode(val)として節を追加する
        """
        if self.root is None:
            # 二分木の根が存在しないときはrootに節を作る
            self.root = Node(val)
            return

        ptr = self.root 
        while True:
            if val < ptr.val:
                if ptr.left is None:
                    # ポインタの示す先に節が存在しない場合はNode(val)を追加する
                    ptr.left = Node(val)
                    ptr.left.parent = ptr
                    return
                ptr = ptr.left
            else:
                if ptr.right is None:
                    # ポインタの示す先に節が存在しない場合はNode(val)を追加する
                    ptr.right = Node(val)
                    ptr.right.parent = ptr
                    return
                ptr = ptr.right
        
    def delete(self, val: int):
        """二分木から値valを持つ節を削除する
        根から順番に子を辿っていき、ptr.val == val が見つかったらptrをつなぎ替える。
        """
        if self.root is None:
            # 二分木の根に節が存在しないときは何もしない
            return 
        
        ptr = self.root
        # ptr.val == valとなる節を探す             
        while True: 
            if ptr is None:
                return
            if ptr.val == val:
                break
            elif val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
       
        # 子が存在しないとき
        if ptr.left is None and ptr.right is None:
            if ptr.parent.left == ptr:
                ptr.parent.left = None
            else:
                ptr.parent.right = None
        # 子が右側にのみ存在するとき
        elif ptr.left is None:
            if ptr.parent.left == ptr:
                ptr.parent.left = ptr.right
                ptr.right.parent = ptr.parent
            else:
                ptr.parent.right = ptr.right
                ptr.right.parent = ptr.parent
        # 子が左側にのみ存在するとき
        elif ptr.right is None:
            if ptr.parent.left == ptr:
                ptr.parent.left = ptr.left
                ptr.left.parent = ptr.parent
            else:
                ptr.parent.right = ptr.left
                ptr.left.parent = ptr.parent
        # 子が両側にのみ存在するとき
        else:
            s = self.search_min(ptr.right)
            ptr.val = s.val
            if s.parent.left == s:
                s.parent.left = None
            else:
                s.parent.right = None            
    
    def search_min(self, ptr):
        """ptrを部分木の根としたときのptrの最小値の節へのポインタを返す
        ptr.leftをひたすら辿っていくことで可能"""
        while True:
            if ptr.left is None:
                return ptr
            ptr = ptr.left
            
    def rotate_left(self, ptr):
        """木を左回転する"""
        w = ptr.right
        w.parent = ptr.parent
        if w.parent is not None:
            if w.parent.left == ptr:
                w.parent.left = w
            else:
                w.parent.right = w
        ptr.right = w.left
        if ptr.right is not None:
            ptr.right.parent = ptr
        ptr.parent = w
        w.left = ptr
        if ptr == self.root:
            self.root = w
            self.root.parent = None

 
    def rotate_right(self, ptr):
        """木を右回転する"""
        w = ptr.left
        w.parent = ptr.parent
        if w.parent is not None:
            if w.parent.right == ptr:
                w.parent.right = w
            else:
                w.parent.left = w
        ptr.left = w.right
        if ptr.left is not None:
            ptr.left.parent = ptr
        ptr.parent = w
        w.right = ptr
        if ptr == self.root:
            self.root = w
            self.root.parent = None

    def preorder_tree_walk(self, ptr, res):
        """先行順巡回(preorder tree walk)"""
        if ptr is None:
            return res
        res.append(ptr.val)
        if ptr.left is not None:
            self.preorder_tree_walk(ptr.left, res)
        if ptr.right is not None:
            self.preorder_tree_walk(ptr.right, res)
        return res

    def inorder_tree_walk(self, ptr, res):
        """中間順巡回(inorder tree walk)"""
        if ptr is None:
            return res
        if ptr.left is not None:
            self.inorder_tree_walk(ptr.left, res)
        res.append(ptr.val)
        if ptr.right is not None:
            self.inorder_tree_walk(ptr.right, res)
        return res

    def postorder_tree_walk(self, ptr, res):
        """後行順巡回(postorder tree walk)"""
        if ptr is None:
            return res
        if ptr.left is not None:
            self.inorder_tree_walk(ptr.left, res)
        if ptr.right is not None:
            self.inorder_tree_walk(ptr.right, res)
        res.append(ptr.val)
        return res
      
      
n = int(input())
info = [list(input().split()) for i in range(n)]
bt = BinaryTree()

for i in range(n):
    if info[i][0] == "insert":
        if bt.search(int(info[i][1])):
            continue
        else:
            bt.insert(int(info[i][1]))
    elif info[i][0] == "find":
        if bt.search(int(info[i][1])):
            print("yes")
        else:
            print("no")
    elif info[i][0] == "delete":
        bt.delete(int(info[i][1]))
    else:
        print(" ", end="")
        print(*bt.inorder_tree_walk(bt.root, res=[]))
        print(" ", end="")
        print(*bt.preorder_tree_walk(bt.root, res=[]))
