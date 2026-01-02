N = input()
K = int(input())

# K = 1の時の組み合わせを求める関数
def func_1(N):
    Nm = int(N[0])
    return Nm + 9 * (len(N) - 1)

# K = 2の時の組み合わせを求める関数
def func_2(N):
    #NはStringなので
    #print(N[0])

    Nm = int(N[0])
    m = len(N)
    #if m == 1:
     #   print("0")
    #print((Nm-1)*(m-1)*9)
    #print((m - 1) * (m - 2) * 9 * 9 / 2)
    x = int(N) - Nm * pow(10, m-1)
    #print(x)
    #print(1)
    #print(func_1(str(x)))


    return  int((Nm-1)*(m-1)*9+(m-1)*(m-2)*9*9/2+func_1(str(x)))

def func_3(N):
    #print("OK")
    Nm = int(N[0])
    m = len(N)
   # if m == 1 or m == 2:
     #   print("0")
    return int(pow(9,3)*(m-1)*(m-2)*(m-3)/6+(Nm-1)*(m-1)*(m-2)*9*9/2+func_2(str(int(N)-Nm*(10**(m-1)))))



if K == 1:
    print(func_1(N))
elif K == 2:
    print(func_2(N))
elif K == 3:
    print(func_3(N))