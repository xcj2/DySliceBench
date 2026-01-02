def case_k1(n):
    digit = len(str(n))
    if digit ==1:
        return n
    else:
        return (n//(10**(digit-1))+(digit-1)*9)

def case_k2(n):
    digit = len(str(n))
    if digit == 1:
        return 0
    elif digit ==2:
        return (n//10-1)*9+n%10
    else:
        sum = 0
        for i in range(1,digit-1):
            sum += i*81
        q = n//(10**(digit-1))
        r = n-q*10**(digit-1)
        r_digit = len(str(r))
        sum += (q-1)*(case_k1(10**(digit-1)-1)) + case_k1(r)
        return sum

def case_k3(n):
    digit = len(str(n))
    if digit <3:
        return 0
    else:
        sum = 0
        for i in range(2,digit-1):
            sum += 9*case_k2(10**(i)-1)
        q = n//(10**(digit-1))
        r = n-q*10**(digit-1)
        sum += (q-1)*(case_k2(10**(digit-1)-1)) + case_k2(r)
        return sum

N = input()
K = int(input())
n = int(N)
if K ==1:
    print(case_k1(n))
elif K ==2:
    print(case_k2(n))
else:
    print(case_k3(n))
