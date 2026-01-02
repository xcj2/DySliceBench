s = str(input())
l_s = list(s)

def inv(l_s):
    l_s_res = []
    for i in l_s[::-1]:
        l_s_res.append(i)
    return l_s_res

def repeat_str(l_s):
    return l_s == inv(l_s)

def first_rep(l_s):
    return repeat_str(l_s)

def second_rep(l_s):
    N = len(l_s)
    l_s_tmp = l_s[:int((N-1)/2)]
    return repeat_str(l_s_tmp)

def third_rep(l_s):
    N = len(l_s)
    l_s_tmp = l_s[int((N+3)/2-1):]
    return repeat_str(l_s_tmp)

if first_rep(l_s) == True and second_rep(l_s) == True and third_rep(l_s) == True:
    print('Yes')
else:
    print('No')