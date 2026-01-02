def parent(i):
    if i / 2 <= 0:
        return 0
    else:
        return int(i/2)
    
def left_child(i):
    if 2*i >= len(L):
        return 0
    else :
        return int(2*i)

def right_child(i):
    if 2*i+1 >= len(L):
        return 0
    else :
        return int(2*i + 1)
    
def make_print(l_idx,p,l_c,r_c):
    print_str='node '+str(l_idx+1)+': key = '+str(L[l_idx+1])
    if p != 0:
        print_str+=', parent key = '+str(L[p])
    if l_c != 0:
        print_str+=', left key = '+str(L[l_c])
    if r_c != 0:
        print_str+=', right key = '+str(L[r_c])
        
    print_str+=', '
    print(print_str)
    
N=int(input())
L=list(map(int,input().split()))
L=[0]+L
    
for l_idx,l in enumerate(L[1:]):
#     print('=====')
#     print(l_idx,l)
    p = parent(l_idx+1)
    l_c = left_child(l_idx+1)
    r_c = right_child(l_idx+1)
#     print(p,l_c,r_c)
    make_print(l_idx,p,l_c,r_c)
