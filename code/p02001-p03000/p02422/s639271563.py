def print_list(s, a, b):
    print(s[a:b+1])

def reverse_list(s, a, b):
    s1 = "".join(s[:a])
    s2 = "".join(reversed(s[a:b+1]))
    s3 = "".join(s[b+1:])
    return list(s1+s2+s3)

def replace_list(s, a, b, p):
    s1 = "".join(s[:a])
    s3 = "".join(s[b+1:])
    return list(s1+p+s3)

s = list(input())
pl = []
cmd = []
n = int(input())
i = 0

while n > i:
    cmd = input().split()
    if cmd[0] == "print":
        pl.append("".join(s[int(cmd[1]):int(cmd[2])+1]))
    elif cmd[0] == "reverse":
        s = reverse_list(s, int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "replace":
        s = replace_list(s, int(cmd[1]), int(cmd[2]), cmd[3])
    i += 1

for p in pl:
    print(p)

