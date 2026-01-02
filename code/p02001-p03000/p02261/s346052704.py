def bubbleSort(c,n):
    for i in range(n):
        for j in range(i+1,n)[::-1]:
            if int(c[j-1][1]) > int(c[j][1]): c[j],c[j-1] = c[j-1],c[j]
    return

def selectionsSort(c,n):
    for i in range(n):
        minj = i
        for j in range(i,n):
            if int(c[minj][1]) > int(c[j][1]): minj = j
        c[i],c[minj] = c[minj],c[i]
    return 

def isStable(inp,outp,n):
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                for l in range(k+1,n):
                    if all((inp[i][1] == inp[j][1],inp[i] == outp[l],inp[j] == outp[k])): return False
    return True

if __name__ == "__main__":
    n = int(input())
    lst = [i for i in input().split()]
    a = lst[:]
    b = lst[:]
    bubbleSort(a,n)
    print(" ".join(a))
    print("Stable" if isStable(lst,a,n) else "Not stable")
    selectionsSort(b,n)
    print(" ".join(b))
    print("Stable" if isStable(lst,b,n) else "Not stable")
