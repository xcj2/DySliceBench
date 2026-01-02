n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
lst_num = [lst[i][0] for i in range(n)]
A = []
B = []
C = []

def Insertion_Sort(arg_lst, arg_lst_num, arg_n):
    for i in range(1,arg_n):
        v = arg_lst_num[i]
        w = arg_lst[i]
        j = i-1
        while j>=0 and arg_lst_num[j]>v:
            arg_lst_num[j+1]=arg_lst_num[j]
            arg_lst[j+1]=arg_lst[j]
            j-=1
        arg_lst_num[j+1]=v
        arg_lst[j+1]=w

def find_root(arg_lst):
    TMP = []
    for i in range(n):
        TMP.extend(arg_lst[i][1:])
    for i in range(n):
        if not i in TMP:
            return i

def Preorder(arg_Q, arg_lst, arg_num):
    arg_Q.append(arg_num)
    if lst[arg_num][1] != -1:
        Preorder(arg_Q, arg_lst, lst[arg_num][1])
    if lst[arg_num][2] != -1:
        Preorder(arg_Q, arg_lst, lst[arg_num][2])

def Inorder(arg_Q, arg_lst, arg_num):
    if lst[arg_num][1] != -1:
        Inorder(arg_Q, arg_lst, lst[arg_num][1])
    arg_Q.append(arg_num)
    if lst[arg_num][2] != -1:
        Inorder(arg_Q, arg_lst, lst[arg_num][2])

def Postorder(arg_Q, arg_lst, arg_num):
    if lst[arg_num][1] != -1:
        Postorder(arg_Q, arg_lst, lst[arg_num][1])
    if lst[arg_num][2] != -1:
        Postorder(arg_Q, arg_lst, lst[arg_num][2])
    arg_Q.append(arg_num)

Insertion_Sort(lst, lst_num, n)
root = find_root(lst)
Preorder(A, lst, root)
print("Preorder")
for i in A:
    print(f" {i}",end="")
print()
Inorder(B, lst, root)
print("Inorder")
for i in B:
    print(f" {i}",end="")
print()
Postorder(C, lst, root)
print("Postorder")
for i in C:
    print(f" {i}",end="")
print()
