n = int(input())
c = list(map(str, input().split()))
c_copy = list(c)

def bubble_sort(c, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if c[j][1] < c[j - 1][1]:
                c[j], c[j - 1] = c[j - 1], c[j]
    return c

def selection_sort(c, n):
    for i in range(n):
        minj = i
        for j in range(i+1, n):
            if c[minj][1] > c[j][1]:
                minj = j
        c[minj],c[i]=c[i],c[minj]
    return c

def is_stable(c1, c2):
    if c1 == c2:
        print("Stable")
    else:
        print("Not stable")

c1 = bubble_sort(c, n)
print(' '.join(c1))
print('Stable')
c2 = selection_sort(c_copy, n)
print(' '.join(c2))
is_stable(c1,c2)
