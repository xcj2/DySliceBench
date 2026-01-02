import sys

def flatten(data):
    for item in data:
        if hasattr(item, '__iter__'):
            for element in flatten(item):
                yield element
        else:
            yield item

n = int(sys.stdin.readline())
preorder = list(map(int, sys.stdin.readline().split()))
inorder = list(map(int, sys.stdin.readline().split()))

def eq(a, b):
    if type(a)!=type(b):  return False   
    if type(a)==list:     return set(flatten(a))== set(flatten(b)) 
    return a==b   

while len(preorder)>1:
    for i in range(len(preorder)-3,-2,-1):
        seq = preorder[i:i+3]
        for j in range(len(inorder)-3,-2,-1):
            if type(preorder[i+1])==int:
                if eq(preorder[i+1], inorder[j+1]) and eq(preorder[i+2], inorder[j+2]):
                    
                    preorder[i+1:i+3] = [[preorder[i+1], 0, preorder[i+2]]]
                    inorder[j+1:j+3]  = [[0, inorder[j+1], inorder[j+2]]]
                    break
                if eq(preorder[i+1], inorder[j+2]) and eq(preorder[i+2], inorder[j+1]):
                    
                    preorder[i+1:i+3] = [[preorder[i+1], preorder[i+2], 0]]
                    inorder[j+1:j+3]  = [[inorder[j+1], inorder[j+2], 0]]
                    break
            if i>=0 and j>=0 and type(preorder[i])==int and eq(preorder[i], inorder[j+1]) and eq(preorder[i+1], inorder[j]) and  eq(preorder[i+2], inorder[j+2]): 
                preorder[i:i+3]=[seq]
                inorder[j:j+3]=[inorder[j:j+3]]
                break
        else:  continue
        break


postorder=[]
def create_postorder(a):
    if type(a)==list:
        for i in [1, 2, 0]: 
            if type(a[i])==list:  create_postorder(a[i])
            elif a[i]>0:          postorder.append(a[i])
    else:  postorder.append(a)
create_postorder(preorder[0])
print(' '.join(map(str, postorder)))
