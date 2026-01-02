#이런식으로 코드 짜니까 이문제가 왜 이런걸 물어보는건지 이해가 감... 대단하다
class Node():
    def __init__(self, parent = -1, left = -1, right = -1): ##초기값 설정
        self.parent = parent
        self.left = left
        self.right = right
##초기 Node()class는 parent,left,right모두 -1
n = int(input())
ns = [Node()for i in range(n)] ##ns[0~(n-1)]모두 Node class 인스턴스화
for i in range(n):
    p, l, r = map(int, input().split())
    if (l != -1):
        ns[l].parent = p ##클래스변수 (메소드 아님,()없음)
        ns[p].left = l
    if (r != -1):
        ns[r].parent = p
        ns[p].right = r
        
        
def preorder(ns, i):  ##여기서의 i는 root 
    print(" "+str(i), end ='')  ##preorder은 루트 쪽부터 print
    if (ns[i].left != -1):  ##left쪽으로 쭉감
        preorder(ns, ns[i].left) ##ns[i].left를 root로써 재귀함수!
    if (ns[i].right != -1):
        preorder(ns, ns[i].right) ##left다했으면 right으로도 똑같이 해줌

def inorder(ns, i):
    if (ns[i].left != -1):
        inorder(ns, ns[i].left)  ##inorder는 일단 재귀함수로 왼쪽 끝까지 감
    print(' ' + str(i), end = '') ##왼쪽 끝가지 간 후 print (더이상 왼쪽으로 갈 수 없을때 print)
    if (ns[i].right != -1):
        inorder(ns, ns[i].right)  ##left로 갈수없을때 실행됨 (오른쪽으로 한번)

def postorder(ns, i):
    if (ns[i].left != -1):
        postorder(ns, ns[i].left)  ##inorder는 일단 재귀함수로 왼쪽 끝까지 감
    if (ns[i].right != -1):
        postorder(ns, ns[i].right)  ##left로 갈수없을때 오른쪽으로 끝까지 감
    print(' ' + str(i), end = '')  ##더이상 갈 수 없을때 print

for i in range(n):
    if (ns[i].parent == -1): ##root를 찾아서 위의 세 함수에 대입하여 print
        print('Preorder')
        preorder(ns, i)
        print()
        print('Inorder')
        inorder(ns, i)
        print()
        print('Postorder')
        postorder(ns, i)
        print()
        break
