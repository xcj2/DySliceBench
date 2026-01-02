import sys
import os

def file_input():
    f = open('ABC116/input.txt', 'r')
    sys.stdin = f

def minusmin(a):
    # print(a)
    if len(a)==1:
        # print('end:'+str(a[0]))
        return a[0]
    else:
        a_min=min(a)
        # print('min:'+str(a_min))
        # print(a_min)
        j=0
        out=a_min
        for i in range(len(a)):
            a[i]-=a_min
            if a[i]==0:
                # print("j="+str(j)+" i="+str(i))
                if i!=j:
                    out+=minusmin(a[j:i])
                j=i+1
            elif i==len(a)-1 and a[i]!=0:
                out+=minusmin(a[j:i+1])
        return out

def main():
    #file_input()
    N=int(input())
    h_li=list(map(int, input().split()))

    print(minusmin(h_li))


if __name__ == '__main__':
    main()
