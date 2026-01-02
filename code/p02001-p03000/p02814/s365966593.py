N, M = list(map(int, input().split(" ")))
list_a = list(map(int, input().split(" ")))

##半公倍数が存在するかチェック
def check_exist(l) :
  if(len(l) == 1) :
    return True
  while(True) :
    flag = l[0] % 2
    for x in l[1:] :
      if(x % 2 != flag) :
        return False
    if(flag == 0) :
      l = list(map(lambda x: int(x/2), l))
    else :
      return True
    

##最大公約数を求める

def gcd(a, b) :
  if(b==0) :
    return a
  else :
    return gcd(b, a%b)
   
##最小公倍数を求める
def lcm(a, b) :
  cd = gcd(a, b)
  return (a / cd) * b
  
##複数個の整数の最小公倍数を求める
def lcm_multi(l) :
  cm = 1
  for x in l :
    cm = lcm(x, cm)
    if(cm > 4 * M) :
      print(0)
      exit()
    
  return cm

if(not(check_exist(list_a))) :
  print(0)
  exit()

## 1/2の公倍数
lcm_m = lcm_multi(list(map(lambda x: int(x/2), list_a)))

if(M-lcm_m < 0) :
  print(0)
else :
  print(int((M-lcm_m) / (2*lcm_m)) + 1)

