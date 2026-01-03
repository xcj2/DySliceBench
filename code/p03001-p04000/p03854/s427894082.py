from math import *

def cin(): # To take limited number of inputs
    return map(int,input().split())

def cins(): # To take space sepreated strings
    return input.split()

def cino(test=False): # To take individual int input (test = False)
    if not test:
        return int(input())
    else: # To take string input (test = True)
        return input()

def cina(): # array input
  return list(map(int,input().split()))

def ssplit(): # multiple string input
    return list(input().split())

def printlist(l): # To print space seperated array
    for i in l:
        print(i,end=" ")

def main():
    a = cino(True)
    check = True
    # print(a[5:10])
    # print(a[11-6:11][::-1])
    i = len(a)-1
    # print(a[10])
    while i>=0:
        # print(i)
        if a[i-5:i+1][::-1]=="resare":
            # "remaerd"}:
            # print(a[i-5:i+1][::-1])
            i-=6
        elif a[i-6:i+1][::-1]=="remaerd":
            # print(a[i-6:i+1][::-1])
            i-=7
        elif a[i-4:i+1][::-1] in {"esare","maerd"}:
            # print(a[i-4:i+1][::-1])
            i-=5
        else:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()