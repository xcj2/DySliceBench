def print_ab(s, a, b):
    print(s[a:b+1])

def reverse_ab(s, a, b):
    s_f = s[:a]
    s_m = s[a:b+1]
    s_b = s[b+1:]

    return s_f + s_m[::-1] + s_b

def replace_ab(s, a, b, p):
    s_f = s[:a]
    s_b = s[b+1:]

    return s_f + p + s_b

if __name__ == "__main__":
    s = input()
    q = int(input())

    for i in range(q):
        ops = input().split()
        if ops[0] == "print":
            print_ab(s, int(ops[1]), int(ops[2]))
        elif ops[0] == "reverse":
            s = reverse_ab(s, int(ops[1]), int(ops[2]))
        elif ops[0] == "replace":
            s = replace_ab(s, int(ops[1]), int(ops[2]), ops[3])