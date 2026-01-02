
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def myAnswer(N:int) -> int:
   divisors = make_divisors(N)
   length = len(divisors)
   if(length % 2 == 1):
      return divisors[length//2]*2 - 2
   else:
      return divisors[length//2] + divisors[length//2 - 1] - 2



def modelAnswer():
   tmp=1
def main():
   N = int(input())
   print(myAnswer(N))
if __name__ == '__main__':
   main()