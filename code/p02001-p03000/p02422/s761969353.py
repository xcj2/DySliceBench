def print_ab(s, a, b):
    print(s[a:b+1])

def reverse_ab(s, a, b):
    s_f = s[:a]
    s_m = s[a:b+1]
    s_l = s[b+1:]
    return s_f+s_m[::-1]+s_l
def replace_ab(s, a, b, p):
    s_f = s[:a]
    s_l = s[b+1:]
    return s_f+p+s_l

s = input()
q = int(input())
for i in range(q):
    option = input().split()
    if option[0] == "print":
        print_ab(s,int(option[1]),int(option[2]))
    elif option[0] == "reverse":
        s = reverse_ab(s, int(option[1]), int(option[2]))
    elif option[0] == "replace":
        s = replace_ab(s, int(option[1]), int(option[2]), option[3])