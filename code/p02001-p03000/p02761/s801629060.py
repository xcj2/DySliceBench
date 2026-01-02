n,m=map(int,input().split())
List=[list(map(int,input().split())) for i in range(m)]


s=[x[0] for x in List]
c=[x[1] for x in List]

def has_duplicates(seq):
    return len(seq) != len(set(seq))

def not_has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) == len(unique_list)

def get_unique_list(seq):
  seen = []
  return [x for x in seq if x not in seen and not seen.append(x)]
  
if has_duplicates(s) and not_has_duplicates2(List):
  print(-1)
else:
  new_List=get_unique_list(List)
  result=0
  for i in range(0,len(new_List)):
    result+=new_List[i][1]*(10**(n-new_List[i][0]))
  if n==1 and result==0:
    print(0)
  elif [1, 0] in new_List:
    print(-1)
  elif result<10**(n-1):
    result+=10**(n-1)
    print(result)
  else:
    print(result)
    