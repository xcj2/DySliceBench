N,X = map(int,input().split())
x = [int(i) for i in input().split()]
def main():
      global X
      global x
      print(answer(pre(X,x)))
def pre(a,b):
      b = [i-a for i in b]
      return b
def answer(k):
      Min = min([abs(i) for i in k])
      flag = False
      for i in range(1,Min+1):
            if flag == True:
                  break
            flag = True
            if Min%i==0:
                  ans = Min//i
                  for j in k:
                        if j%ans!=0:
                              flag = False
            else:
                  flag = False
      return ans
main()