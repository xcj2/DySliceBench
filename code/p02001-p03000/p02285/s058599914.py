err = 2*(10**9)+1

class STNode:
    def __init__(self, k, l, r, p):
        self.key = k
        self.left = l
        self.right = r
        self.parent = p

def STinsert(h, z):
    global err
    p = None
    while True:
        if h.key == err:
            break
        p = h
        if z.key < h.key:
            h = h.left
        else:
            h = h.right
    if z.key < p.key:
        p.left = z
    else:
        p.right = z
    z.parent = p

def STsearch(h, k):
    global err
    while h.key != err:
        if k < h.key:
            h = h.left
        elif h.key < k:
            h = h.right
        else:
            return h
    return None

def STdelete(head, k):
    global err
    h = STsearch(head, k)
    if h is None:
        pass
    else:
        if h.left.key == err and h.right.key == err:
            if k < h.parent.key: #h.leftはNULLnode
                h.parent.left = h.left
            else:
                h.parent.right = h.left
        elif h.left.key == err: #right child exists
            h.right.parent = h.parent
            if k < h.parent.key: #h.leftはNULLnode
                h.parent.left = h.right
            else:
                h.parent.right = h.right
        elif h.right.key == err: #left child exists
            h.left.parent = h.parent
            if k < h.parent.key: #h.rightはNULLnode
                h.parent.left = h.left
            else:
                h.parent.right = h.left
        else:
            #一度右の子に移りそこから限界まで左の子を見る
            #左の子がNULLnodeならループを抜ける
            #その節点の子が0個か1個かにより処理を分ける
            temp = h.right
            flg = 0 #一度でもwhile内部で左の子に移動したら1
            while temp.left.key != err:
                temp = temp.left
                flg = 1

            #tempは中間順でhの次節点を参照する
            h.key = temp.key
            if temp.right.key == err:
                if flg == 1:
                    temp.parent.left = temp.left
                else:
                    temp.parent.right = temp.left
            else:
                temp.right.parent = temp.parent
                if flg == 1:
                    temp.parent.left = temp.right
                else:
                    temp.parent.right = temp.right


def preorder(head, h, A):
    global err
    if h.key == err:
        return
    A.append(h.key)
    preorder(head, h.left, A)
    preorder(head, h.right, A)
    if head == h:
        print('', *A)

def inorder(head, h, B):
    global err
    if h.key == err:
        return
    inorder(head, h.left, B)
    B.append(h.key)
    inorder(head, h.right, B)
    if head == h:
        print('', *B)

n = int(input())
NULLnode = STNode(err, None, None, None)

first = list(input().split())
head = STNode(int(first[1]), NULLnode, NULLnode, NULLnode)

for i in range(n-1):
    temp = list(input().split())
    if temp[0] == "insert":
        z = STNode(int(temp[1]), NULLnode, NULLnode, NULLnode)
        STinsert(head, z)
    elif temp[0] == "print":
        A = []
        B = []
        inorder(head, head, B)
        preorder(head, head, A)
    elif temp[0] == "find":
        res = STsearch(head, int(temp[1]))
        if res is None:
            print("no")
        else:
            print("yes")
    else: #delete
        STdelete(head, int(temp[1]))
