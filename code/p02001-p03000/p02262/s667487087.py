import sys

cnt = 0
g = []

def insertion_sort(a, n, g):
    global cnt
    
    for i in range(g, n):
        v = a[i]
        j = i - g

        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j -= g
            cnt += 1

        a[j+g] = v

def shell_sort(a, n):
    global g

    h = 1
    while True:
        if h > n:
            break

        g.append(h)
        h = h * 3 + 1

    for i in range(len(g)-1, -1, -1):
        insertion_sort(a, n, g[i])
    
def main():
    n = int(sys.stdin.readline().strip())
    a = []

    for i in range(n):
        a.append(int(sys.stdin.readline().strip()))

    shell_sort(a, n)

    print(len(g))

    for i in range(len(g)-1, -1, -1):
        print(g[i], end='')
        if i:
            print(' ', end='')

    print('')
    print(cnt)

    for i in range(n):
        print(a[i])

if __name__ == '__main__':
    main()