#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

# # # # AVL class # # # #

# NOTE multi_mode not well tested 2020-08-02

DBG_TEST_AVL = False
AVL_INF = 10**16

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVL(object):

    def __init__(self,multi=False):
        self.root = None
        self.multi_mode = multi

    def get_height(self, node):
        if not node:
            return -1
        return node.height

    def get_balance(self, node):
        '''
        返り値が1より大きい場合、左の部分木が重い　→　右回転
        返り値が-1より小さい場合、右の部分木が重い　→　左回転
        '''
        if not node:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def rotate_right(self, node):
        temp_left_child = node.left_child
        temp_left_right_child = temp_left_child.right_child

        temp_left_child.right_child = node
        node.left_child = temp_left_right_child

        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        temp_left_child.height = max(self.get_height(temp_left_child.left_child), self.get_height(temp_left_child.right_child)) + 1

        return temp_left_child

    def rotate_left(self, node):
        temp_right_child = node.right_child
        temp_right_left_child = temp_right_child.left_child

        temp_right_child.left_child = node
        node.right_child = temp_right_left_child

        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        temp_right_child.height = max(self.get_height(temp_right_child.left_child), self.get_height(temp_right_child.right_child)) + 1

        return temp_right_child

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self._insert(data, node.left_child)
        else:
            if not self.multi_mode and data==node.data:
                return node
            node.right_child = self._insert(data, node.right_child)

        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        return self.settle_unbalance(data, node)

    def settle_unbalance(self, data, node):

        balance = self.get_balance(node)

        # balace >1 -> 左の方が重い
        # data < node.left_child.data 左の子より左側にデータが挿入されたので、左の子の左の子の方が重い
        # つまり、left-left heavy　右回転を行う
        if balance > 1 and data < node.left_child.data:
            return self.rotate_right(node)

        # balace > -1 -> 右の方が重い
        # data > node.right_child.data 右の子より右側にデータが挿入されたので、右の子の右の子の方が重い
        # つまり、right-right heavy　左回転を行う
        if balance < -1 and data > node.right_child.data:
            return self.rotate_left(node)

        # balace >1 -> 左の方が重い
        # data > node.left_child.data 左の子より右側にデータが挿入されたので、左の子の右の子の方が重い
        # つまり、left-right heavy　左回転を行い右回転を行う
        if balance > 1 and data > node.left_child.data:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        # balace > -1 -> 右の方が重い
        # data < node.right_child.data 右の子より左側にデータが挿入されたので、右の子の左の子の方が重い
        # つまり、right-left heavy　右回転を行い左回転を行う
        if balance < -1 and data < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def traverse_inorder(self):
        if self.root:
            self._traverse_inorder(self.root)
            # 改行対策
            print()
        else:
            print('木は空です。')

    def _traverse_inorder(self, node):
        if node.left_child:
            self._traverse_inorder(node.left_child)

        print(node.data, end=' ')

        if node.right_child:
            self._traverse_inorder(node.right_child)

    def remove(self, data):
        if self.root:
            self.root = self._remove(data, self.root)

    def _remove(self, data, node):
        # 単体の木の場合
        if not node:
            return node

        if data < node.data:
            node.left_child = self._remove(data, node.left_child)
        elif data > node.data:
            node.right_child = self._remove(data, node.right_child)
        else:
            # 削除ノードが子を持たない場合は、ノードを削除する。
            if not node.right_child and not node.left_child:
                del node
                # None を返すことで、親ノードの削除子ノードへのポインタを None に変更
                return None

            # 削除ノードが左の子だけを持つ場合、ノードを削除し、左の子のノードを返す
            if not node.right_child:
                temp = node.left_child
                del node
                # 左の子のノードを返すことで、親ノードの削除子ノードへのポインタを新しい子ノードに変更
                return temp

            # 削除ノードが右の子だけを持つ場合、左の子だけの場合の逆の操作を行う
            if not node.left_child:
                temp = node.right_child
                del node
                return temp
            # 削除ノードが左右の子を持つ場合、ここでは、左側のsubtreeの最大のノードを代わりのノードにすることにする。
            #  subtreeの最大のノードを取得するヘルパー関数
            def _get_max_node(node):
                if node.right_child:
                    return _get_max_node(node.right_child)
                return node
            temp = _get_max_node(node.left_child)
            node.data = temp.data
            # 左側のsubtreeから削除ノードと入れ替えたノードを削除
            node.left_child = self._remove(temp.data, node.left_child)

        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left_child) >= 0:
            print('left-left heavy')
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.left_child) <= 0:
            print('right-right heavy')
            return self.rotate_left(node)

        if balance > 1 and self.get_balance(node.left_child) < 0:
            print('left-right heavy')
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.left_child) > 0:
            node.right_child = self.rotate_right(node.right_child)
            print('right-left heavy')
            return self.rotate_left(node)

        return node

    def find_bounds(self,d):
        return self._find(self.root,d,-AVL_INF,AVL_INF)

    def _find(self,nd,d,l,r):
        if not nd:
            return (l,r)
        elif nd.data==d:
            return (d,d)
        elif nd.data<d:
            return self._find(nd.right_child,d,max(l,nd.data),r)
        else:
            return self._find(nd.left_child,d,l,min(r,nd.data))

#if __name__ == '__main__':
def test_avl_alone():
    avl = AVL()

    avl.insert(2)
    avl.insert(4)
    avl.insert(8)
    avl.insert(16)
    avl.insert(16)
    avl.insert(32)
    avl.insert(64)
    avl.insert(128)
    avl.insert(256)
    avl.insert(512)
    # 2 4 8 16 32 64 128 256 512
    avl.traverse_inorder()
    avl.remove(2)
    # right-right heavy
    avl.remove(4)
    print(avl.find_bounds(3))
    avl.remove(512)
    avl.remove(256)
    # left-left heavy
    avl.remove(64)
    print(avl.find_bounds(37))
    print(avl.find_bounds(128))
    avl.remove(128)
    # 8 16 32
    avl.traverse_inorder()
    # height 1
    print('height', avl.get_height(avl.root))

if DBG_TEST_AVL:
    test_avl_alone()

# # # # AVL class end # # # #


n = inn()
a = inl()
mnl = [0]*n
mnr = [0]*n
mxl = [0]*n
mxr = [0]*n

lacc = a[0]
av = AVL()
av.insert(lacc)
for i in range(1,n-2):
    lacc += a[i]
    r1 = av.find_bounds(lacc//2)
    r2 = av.find_bounds(lacc//2+1)
    #if min([abs(r1[0]),abs(r1[1]),abs(r2[0]),abs(r2[1])])>10**10:
    #    3/0
    mnl[i+1] = max([ \
     min(r1[0],lacc-r1[0]),
     min(r1[1],lacc-r1[1]),
     min(r2[0],lacc-r2[0]),
     min(r2[1],lacc-r2[1]) ])
    mxl[i+1] = min([ \
     max(r1[0],lacc-r1[0]),
     max(r1[1],lacc-r1[1]),
     max(r2[0],lacc-r2[0]),
     max(r2[1],lacc-r2[1]) ])
    av.insert(lacc)

racc = a[n-1]
av = AVL()
av.insert(racc)
for i in range(n-2,1,-1):
    racc += a[i]
    r1 = av.find_bounds(racc//2)
    r2 = av.find_bounds(racc//2+1)
    mnr[i] = max([ \
     min(r1[0],racc-r1[0]),
     min(r1[1],racc-r1[1]),
     min(r2[0],racc-r2[0]),
     min(r2[1],racc-r2[1]) ])
    mxr[i] = min([ \
     max(r1[0],racc-r1[0]),
     max(r1[1],racc-r1[1]),
     max(r2[0],racc-r2[0]),
     max(r2[1],racc-r2[1]) ])
    av.insert(racc)

print(min( \
 [max(mxr[i],mxl[i])-min(mnr[i],mnl[i]) for i in range(2,n-1)]))
