def read():
    return int(input())

def reads(sep=None):
    return list(map(int, input().split(sep)))

def main():
    n, a, b = reads()
    s = input()
    
    ai, bi = 0, 0
    for c in s:
        if c == 'a':
            if ai+bi < a+b:
                print('Yes')
                ai += 1
            else:
                print('No')
        elif c == 'b':
            if ai+bi < a+b and bi < b:
                print('Yes')
                bi += 1
            else:
                print('No')
        else:
            print('No')

main()
