'''ALDS1_8_A: Binary search trees - Binary Search Tree I
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_A
******
Search trees are data structures that support dynamic set operations including
insert, search, delete and so on. Thus a search tree can be used both as a
dictionary and as a priority queue.

Binary search tree is one of fundamental search trees. The keys in a binary
search tree are always stored in such a way as to satisfy the following binary
search tree property:

- Let x be a node in a binary search tree. If y is a node in the left subtree of
x, then y.key≤x.key. If y is a node in the right subtree of x, then x.key≤y.key.

The following figure shows an example of the binary search tree.

For example, keys of nodes which belong to the left sub-tree of the node
containing 80 are less than or equal to 80, and keys of nodes which belong to
the right sub-tree are more than or equal to 80. The binary search tree property
allows us to print out all the keys in the tree in sorted order by an inorder
tree walk.

A binary search tree should be implemented in such a way that the binary search
tree property continues to hold after modifications by insertions and deletions.
A binary search tree can be represented by a linked data structure in which each
node is an object. In addition to a key field and satellite data, each node
contains fields left, right, and p that point to the nodes corresponding to its
left child, its right child, and its parent, respectively.

To insert a new value v into a binary search tree T, we can use the procedure
insert as shown in the following pseudo code. The insert procedure is passed a
node z for which z.key=v, z.left=NIL, and z.right=NIL. The procedure modifies T
and some of the fields of z in such a way that z is inserted into an appropriate
position in the tree.

1 insert(T, z)
2     y = NIL // parent of x
3     x = 'the root of T'
4     while x ≠ NIL
5         y = x // set the parent
6         if z.key < x.key
7             x = x.left // move to the left child
8         else
9             x = x.right // move to the right child
10    z.p = y
11
12    if y == NIL // T is empty
13        'the root of T' = z
14    else if z.key < y.key
15        y.left = z // z is the left child of y
16    else
17        y.right = z // z is the right child of y

Write a program which performs the following operations to a binary search tree
T.

- insert k: Insert a node containing k as key into T.
- print: Print the keys of the binary search tree by inorder tree walk and
preorder tree walk respectively.

You should use the above pseudo code to implement the insert operation. TT is empty at the initial state.
******
Input
In the first line, the number of operations m is given. In the following m
lines, operations represented by insert kk or print are given.
******
Output
For each print operation, print a list of keys obtained by inorder tree walk
and preorder tree walk in a line respectively. Put a space character before each
key.
******
Constraints
- The number of operations ≤500,001
- The number of print operations ≤10.
- −2,000,000,000≤key≤2,000,000,000
- The height of the binary tree does not exceed 100 if you employ the above
pseudo code.
- The keys in the binary search tree are all different.
******
Sample Input 1
8
insert 30
insert 88
insert 12
insert 1
insert 20
insert 17
insert 25
print
Sample Output 1
 1 12 17 20 25 30 88
 30 12 1 20 17 25 88
******
Reference
Introduction to Algorithms, Thomas H. Cormen, Charles E. Leiserson, Ronald L.
Rivest, and Clifford Stein. The MIT Press.
******
＜方針１＞
    「__slots__」について
        Pythonではデフォルトではオブジェクトのインスタンスの属性はdictを使って保存している
        この保存の仕方では、実行中に新たな属性を動的に設定できたりして良い
        だけど、少数の固定な属性を持つ小さなクラスを扱うときにはdictはメモリの無駄
        こういう時は__slots__に属性の名前を記述することでメモリを節約したほうが良い
'''
import sys

class Node:
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        x = self.root
        y = None
        z = Node(key)
        while x != None:
            y = x
            x = x.left if z.key < x.key else x.right
        if y == None: self.root = z
        else:
            if z.key < y.key: y.left = z
            else: y.right = z
    def print_tree(self):
        def inorder(node):
            if node:
                inorder(node.left)
                print('',node.key, end='')
                inorder(node.right)
        def preorder(node):
            if node:
                print('',node.key, end='')
                preorder(node.left)
                preorder(node.right)
        inorder(self.root)
        print()
        preorder(self.root)
        print()

tree = BST()
for e in [0]*int(input()):
    e = input()
    if e[0] == 'i': tree.insert(int(e[7:]))
    else:
        tree.print_tree()
