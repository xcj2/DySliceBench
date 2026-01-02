import sys


def print_str(str, a, b):
    print(str[a:b+1])


def reverse_str(str, a, b):
    return str[:a] + str[a:b+1][::-1] + str[b+1:]


def replace_str(str, a, b, p):
    return str[:a] + p + str[b+1:]


str = sys.stdin.readline().strip()
num_commands = int(sys.stdin.readline())

for _ in range(num_commands):
    command, *args = sys.stdin.readline().strip().split()
    if command == 'print':
        print_str(str, int(args[0]), int(args[1]))
    elif command == 'reverse':
        str = reverse_str(str, int(args[0]), int(args[1]))
    elif command == 'replace':
        str = replace_str(str, int(args[0]), int(args[1]), args[2])

