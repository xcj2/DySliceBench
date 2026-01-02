def replace(str):
    for i, c in enumerate(command[3], command[1]):
        str[i] = c
    return str

def reverse(str):
    for i, c in enumerate(reversed(str[command[1]: command[2]+1]), command[1]):
        str[i] = c
    return str

def str_print(str):
    str = ''.join(str)
    print(str[command[1]: command[2]+1])
    str = list(str)
    return str

str = list(input())
q = int(input())
for i in range(q):
    command = input().split()
    command[1], command[2] = int(command[1]), int(command[2])
    if command[0] == 'replace':
        str = replace(str)
    elif command[0] == 'reverse':
        str = reverse(str)
    else:
        str = str_print(str)

