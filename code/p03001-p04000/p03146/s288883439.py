def f(n):
   return n//2 if(n % 2 == 0) else 3*n + 1

def myAnswer(s:int) -> int:
   i = 1
   a = [s]
   hantei = False
   while True:
      tmp = f(a[i - 1])
      if(tmp == 1):
         if(hantei == True):
            a.append(tmp)
            break
         else:
            hantei = True
      a.append(tmp)
      i+=1
   ans = 10**9
   while len(a) != 0:
      n = len(a)
      m = a.pop(-1)
      if(m in a):
         ans = min(ans,n)
   return ans



def modelAnswer():
   tmp=1
def main():
   s = int(input())
   print(myAnswer(s))

if __name__ == '__main__':
   main()