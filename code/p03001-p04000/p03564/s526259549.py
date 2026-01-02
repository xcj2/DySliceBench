def A(n,k):
    return 2*n
def B(n,k):
    return n+k
def square(n,k):
    a=A(c[0],k)
    b=B(c[0],k)
    i[0]-=1
    if i[0]==-1:
        return n
    else: 
        if a>=b:
            """
            print("A")
            print(a)
            print("B")
            print(b)
            """
            c[0]=b
            return square(c[0],k)
        else:
            """
            print("B")
            print(b)
            """
            c[0]=a
            return square(c[0],k)
c=[1]
n=int(input())
i=[n]
k=int(input())
print(square(n,k))