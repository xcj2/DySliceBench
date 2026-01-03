N=int(input())
A=input()
def check_l(A):
    for i in range(1,len(A)+1):
        if not i==len(A):
            if A[-i]=="(":
                pass
            else:
                return i
                break
        elif i==len(A):
            if A[-i]=="(":
                return 0
            else:
                return i
                break
def check_t(A):
    for i in range(0,len(A)):
        if not i==len(A)-1:
            if A[i]==")":
                pass
            else:
                return i
                break
        elif i==len(A)-1:
            if A[i]==")":
                a=len(A)
                return a
            else:
                return i
def all(A,C):
    if check_l(A)==0:
        for i in range(len(A)):
            C=C+")"
        print(C)
        exit()
    elif not check_l(A)==0:
        for i in range(check_l(A)-1):
            A=A+")"
            C=C+")"

    if check_t==len(A):
        for i in range(len(A)):
            C="("+C
        print(C)
        exit()
    else:
        for i in range(check_t(A)):
            A="("+A
            C="("+C

    for i in range(10**9):
        if "()" in A:
            A=A.replace("()","")
        else:
            break
    return A,C

X=A

for i in range(N):
    if A=="":
        print(X)
        break
    else:
        A,X=all(A,X)
