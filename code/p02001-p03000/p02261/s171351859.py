def bubble_sort(a,n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if a[j][1] < a[j-1][1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

def selection_sort(a,n):
    for i in range(n):
        minj = i
        for j in range(i+1,n):
            if a[j][1] < a[minj][1]:
                minj = j
        a[i],a[minj] = a[minj],a[i]
    return a

def is_stable(a, sa, n):
    stable = True
    for i in range(n-1):
        if sa[i][1] == sa[i+1][1] and a.index(sa[i]) > a.index(sa[i+1]):
                stable = False
                break
    if stable:
        print('Stable')
    else:
        print('Not stable')

n = int(input())
a = [ (s[0], int(s[1:])) for s in input().split() ]
ba = bubble_sort(a.copy(),n)
print(*[ s[0]+str(s[1]) for s in ba])
is_stable(a,ba,n)
ia = selection_sort(a.copy(),n)
print(*[ s[0]+str(s[1]) for s in ia])
is_stable(a,ia,n)
