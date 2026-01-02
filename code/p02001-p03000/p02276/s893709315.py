def swap(A, i, j):
#    print("\tswap Aj:{} Ai:{}\n".format(A[j], A[i]))
    x = A[i]
    A[i] = A[j]
    A[j] = x

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
#        print("j:{} Aj:{} i:{} Ai:{} Ar:{}".format(j, i, A[j], A[i], A[r]))
#        print(A)
#        print(" ")
    A[r] = "[{}]".format(A[r])
    swap(A,i+1, r)
    i += 1
    return i

def main():
    """ ????????? """
    num = int(input().strip())
    A = list(map(int,input().split()))
    partition(A, 0, num-1)
    print(" ".join(map(str,A)))

if __name__ == '__main__':
    main()