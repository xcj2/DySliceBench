def solve():
    n=int(input())
    num=[]
    def append(num1):
        num.append(num1)
    def count1(num2):
        return num.count(num2)
    for i in range(n):
        a=int(input())
        append(a)
    max1=max(num)
    count=count1(max1)
    if count>1:
        for i in range(n):
            print(max1)
    else:
        for i in range(n):
            if num[i]==max1:
                if i==0:
                    print(max(num[1:]))
                elif i==n-1:
                    print(max(num[:n-1]))
                else:
                    print(max(max(num[:i]),max(num[i+1:])))
            else:
                print(max1)
solve()
