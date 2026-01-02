
string = list(input())
q = int(input())

def print_func(head, end):
    string_p = ''
    for i in range(head,end + 1):
        string_p += string[i]
    print(string_p)

def reverse_func(head, end):
    i = 0
    while head + i <= end - i:
        string[head + i],string[end - i] = string[end - i],string[head + i]
        i += 1

def replace_func(head, end, r_str):
    l_r_str = list(r_str)
    for i in range(end - head + 1):
        string[head + i] = l_r_str[i]

for i in range(q):
    l = list(input().split())
    l[1] = int(l[1]); l[2] = int(l[2])
    if l[0] == 'print':
        print_func(l[1],l[2])
    elif l[0] == 'reverse':
        reverse_func(l[1],l[2])
    else:
        replace_func(l[1],l[2],l[3])
