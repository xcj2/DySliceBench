def print_text(text, a, b):
    s = int(a)
    e = int(b)+1

    print(text[s:e])

def reverse_text(text, a, b):
    s = int(a)
    e = int(b)+1

    return text[:s] + text[s:e][::-1] + text[e:]

def replace_text(text, a, b, p):
    s = int(a)
    e = int(b)+1

    return text[0:s] + p + text[e:]

def main():
    text = input()
    q = int(input())

    for _ in range(q):
        op, *args = input().split()

        if   op == 'print':
            print_text(text, *args)
        elif op == 'reverse':
            text = reverse_text(text, *args)
        elif op == 'replace':
            text = replace_text(text, *args)

if __name__ == '__main__':
    main()
