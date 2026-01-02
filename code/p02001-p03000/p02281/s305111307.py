class Node():
  def __init__(self):
    self.parent = -1
    self.left = -1
    self.right = -1


n = int(input())
node  = [list(map(int, input().split())) for _ in range(n)] 
result = [Node() for _ in range(n)]
D = [0 for _ in range(n)]
H = [0 for _ in range(n)]


def initiate(li):
  for l in li:
    n = l[0]
    left = l[1]
    right = l[2]
    if left != -1:
      result[left].parent = n
      result[n].left = left
    if right != -1:
      result[right].parent = n
      result[n].right = right

post_list = []
pre_list = []
in_list = []

def preorder(li, root):
  pre_list.append(root)
  if li[root].left != -1:
    preorder(li, li[root].left)
  if li[root].right != -1:
    preorder(li, li[root].right)
  return 

def inorder(li, root):
  if li[root].left != -1:
    inorder(li, li[root].left)
  in_list.append(root)
  if li[root].right != -1:
    inorder(li, li[root].right)
  return 

def postorder(li, root):
  if li[root].left != -1:
    postorder(li, li[root].left)
  if li[root].right != -1:
    postorder(li, li[root].right)
  post_list.append(root)
  return

initiate(node)
root = 0
for i in range(n):
  if result[i].parent == -1:
    root = i 
    break


preorder(result, root)
pre_list = list(map(str, pre_list))
inorder(result, root)
in_list = list(map(str, in_list))
postorder(result, root)
post_list = list(map(str, post_list))

final = []

print("Preorder")
print("", ' '.join(pre_list))
print("Inorder")
print(""," ".join(in_list))
print("Postorder")
print(""," ".join(post_list))


