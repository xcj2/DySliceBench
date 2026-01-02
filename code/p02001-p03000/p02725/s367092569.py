def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

K, N = input_int()

A = many_int()

b_list=[]
n_list=[]
for i,a in enumerate(A):
    nexts = 0 if i+1==N else i+1
    back  = N-1 if i==0 else i-1
    
    if A[back] > a:
        back = (a+K)-A[back]
    else:
        back = a-A[back]
    
    if A[nexts] < a:
        nexts = (A[nexts]+K)-a
    else:
        nexts = A[nexts]-a
    
    
    b_list.append(back)
    n_list.append(nexts)

print(sum(b_list)-max(b_list))