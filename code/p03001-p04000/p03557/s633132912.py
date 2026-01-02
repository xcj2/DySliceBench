n = int(input())
a_ls = list(map(int, input().split()))
b_ls = list(map(int, input().split()))
c_ls = list(map(int, input().split()))
for ls in [a_ls,b_ls,c_ls]:
    ls.sort()

def is_not_less_than(ls, ind, key):
    if ls[ind] >= key:
        return True
    else:
        return False

def return_min_ind_whose_value_not_less_than(ls,key):
    r = len(ls)
    l = -1
    while True:
        next_ind = (r+l) // 2
        if is_not_less_than(ls, next_ind, key):
            r = next_ind
        else:
            l = next_ind
        if r - l == 1:
            return r

def is_more_than(ls, ind, key):
    if ls[ind] > key:
        return True
    else:
        return False

def return_min_ind_whose_value_more_than(ls,key):
    r = len(ls)
    l = -1
    while True:
        next_ind = (r+l) // 2
        if is_more_than(ls, next_ind, key):
            r = next_ind
        else:
            l = next_ind
        if r - l == 1:
            return r

ans = 0
for i in range(n):
    b_c = n - return_min_ind_whose_value_more_than(c_ls, b_ls[i])
    a_b = return_min_ind_whose_value_not_less_than(a_ls, b_ls[i])
    ans += b_c*a_b
print(ans)
