s = input().split()
n = int(s[0])

st = ['a','b','c','d','e','f','g','h','i','j','k']

#initialize
inis = [1,1,1,1,1,1,1,1,1,1,1]

def print_str( arry , num):
   str_a = ''
   for i in range(num):
     #print(arry,i)
     str_a = str_a + st[arry[i]-1]
   print(str_a)

# len = 1 .. 10
def do_number_n( len ):
   global inis
   tsti = 0
   k = len - 1    
   print_str( inis , len)
   while True:
      inis[k] += 1
      for j in range(k,0,-1):
         #print(inis[0:j],j)
         if ( max(inis[0:j]) + 2 ) <= inis[j]  :
         #if ( inis[j-1] + 2 ) <= inis[j]  :
            inis[j-1] += 1
            inis[j] = 1
         #print('test:  {},{},   {}'.format(j,k,inis))
            
      #最後まで行った。
      if inis[0] > 1 :
         return        
      print_str( inis , len)
  
def main():
  do_number_n(n)
    
main()
