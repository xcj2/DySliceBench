def resolve():
    a = []
    for i in range(3):
        a.append([int(x) for x in input().split(" ")])
    
    n = int(input())
    lst = []
    for i in range(n):
        lst += [int(input())]

    flag = False
    for i in range(3):
        if row(i,lst,a):
            print("Yes")
            return
        if col(i,lst,a):
            print("Yes")
            return
    if diag1(lst,a) or diag2(lst,a):
        print("Yes")
        return
    print("No")
        
        

def row(i,lst,a):
    '''print("aは", file=sys.stderr)
    print(a, file=sys.stderr)
    print("lstは", file=sys.stderr)
    print(lst, file=sys.stderr)'''
    for j in range(3):
        if not a[i][j] in lst:
            return False
    return True

def col(j,lst,a):
    for i in range(3):
        if not a[i][j] in lst:
            return False
    return True

def diag1(lst,a):
    for i in range(3):
        if not a[i][i] in lst:
            return False
    return True

def diag2(lst,a):
    for i in range(3):
        if not a[2-i][i] in lst:
            return False
    return True

resolve()