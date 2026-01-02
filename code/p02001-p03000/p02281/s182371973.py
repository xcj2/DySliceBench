ID,LEFT,RIGHT = 0,1,2
n = int(input())

preorder_list = []
def preorder(node):
  preorder_list.append(node[0][ID])
  if node[0][LEFT] != -1:
    preorder(nodes[node[0][LEFT]])
  if node[0][RIGHT] != -1:
    preorder(nodes[node[0][RIGHT]])

inorder_list = []
def inorder(node):
  if node[0][LEFT] != -1:
    inorder(nodes[node[0][LEFT]])
  inorder_list.append(node[0][ID])
  if node[0][RIGHT] != -1:
    inorder(nodes[node[0][RIGHT]])

postorder_list = []
def postorder(node):
  if node[0][LEFT] != -1:
    postorder(nodes[node[0][LEFT]])
  if node[0][RIGHT] != -1:
    postorder(nodes[node[0][RIGHT]])
  postorder_list.append(node[0][ID])

nodes = [[] for _ in range(n)]
for i in range(n):
  id, left, right = list(map(int, input().split()))
  nodes[id].append({ID:id, LEFT:left, RIGHT:right})

id_list = [0 for _ in range(n)]
for node in nodes:
  if node[0][LEFT] != -1:
    id_list[node[0][LEFT]] += 1
  if node[0][RIGHT] != -1:
    id_list[node[0][RIGHT]] += 1

root_id = -1
for i,v in enumerate(id_list):
  if v == 0:
    root_id = i
    break


preorder(nodes[root_id])
print ('Preorder')
print (' '+' '.join(map(str, preorder_list)))
inorder(nodes[root_id])
print ('Inorder')
print (' '+' '.join(map(str, inorder_list)))
postorder(nodes[root_id])
print ('Postorder')
print (' '+' '.join(map(str, postorder_list)))

