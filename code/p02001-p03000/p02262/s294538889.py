def insertion_sort(a, n, g, cnt):
    for i in range(g,n,1):
        v = a[i]
        j = i - g #initial value
        while j>=0 and a[j]>v:
            a[j+g]=a[j]
            j -= g
            cnt += 1
        a[j+g] = v
    return a, cnt

def shell_sort(a,n,m,g):
    cnt = 0
    for i in range(m):
        sorted_list, cnt = insertion_sort(a,n,g[i],cnt)
    return sorted_list, cnt

def seqforshell(n):
    seq = [1]
    next_num = 3*seq[0] + 1
    while next_num<n:
        seq.insert(0, next_num)
        next_num = 3*next_num + 1
    return seq

if __name__ == "__main__":
    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    
    g = seqforshell(n)
    m = len(g)
    res, cnt = shell_sort(a,n,m,g)
    
    print(m)
    print(*g)
    print(cnt)
    for i in range(n):
        print(res[i])
