AB = input().split(' ')
A = int(AB[0])
B = int(AB[1])
'''
def cf(x1,x2):
    cf=[]
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
                cf.append(i)
    return cf
 
def check_cf(x1,x2):
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            return False
    return True
candidate = cf(A,B)
'''
'''
decided_list = [candidate[0]]
 
for i in range(1,len(candidate)):
    flag = True
    for s in range(2,candidate[i]):
        if candidate[i]%s == 0:
            flag = False
            break
    if flag:
        decided_list.append(candidate[i])
'''
#print(candidate)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)
max_gcd = gcd(A,B)
result = factorization(max_gcd)
#print(result)
if len(result) == 1 and result[0][0] == 1:
    print(1)
else:
    print(len(result)+1)