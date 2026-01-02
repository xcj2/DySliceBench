sentinel = str(10**9+1)

def partition(A, p, r):
    x = int(A[r][1])
    i = p - 1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def merge(lst,left,middle,right):
    left_lst  =  lst[left:middle] + [['',sentinel]]
    right_lst = lst[middle:right] + [['',sentinel]]

    i,j = 0,0
    for k in range(left,right):
        if int(left_lst[i][1]) <= int(right_lst[j][1]):
            lst[k] = left_lst[i]
            i += 1
        else:
            lst[k] = right_lst[j]
            j += 1

def merge_sort(lst,left,right):
    if left+1 < right:
        middle = (left+right)//2
        merge_sort(lst,left,middle)
        merge_sort(lst,middle,right)
        merge(lst,left,middle,right)


n = int(input())
n_lst = [[i for i in input().split()] for _ in range(n)]
m_lst = list(n_lst)
quick_sort(n_lst,0,n-1)
merge_sort(m_lst,0,n)
print('Stable' if n_lst == m_lst else 'Not stable')
for ans in n_lst:
    print('{} {}'.format(ans[0],ans[1]))

