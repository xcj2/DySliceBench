def card_encoder(a):
  result = []
  for i in a:
    s = list(map(str,i))
    c_attr = s[0]
    s.pop(0)
    c_num = int(''.join(s))
    result.append([c_attr,c_num])
  return result

def card_encoder2(a):
  result = []
  for i in a:
    s = list(map(str,i))
    s.pop(0)
    c_num = int(''.join(s))
    result.append(c_num)
  return result

def card_decoder(a):
  result = []
  for t in a:
    result.append(t[0] + str(t[1]))
  return result

def bubble_sort(a,n):
  a = card_encoder(a)
  flag = 1
  while flag:
    flag = 0
    for i in range(1,n)[::-1]:
      if a[i][1] < a[i-1][1]:
        temp = a[i]
        a[i] = a[i-1]
        a[i-1] = temp
        flag = 1
  a = card_decoder(a)
  return a
  
def selection_sort(a,n):
  a = card_encoder(a)
  for i in range(0,n):
    minv = i
    for j in range(i,n):
      if a[j][1] < a[minv][1]:
        minv = j
    if a[i][1] != a[minv][1]:
      temp = a[i]
      a[i] = a[minv]
      a[minv] = temp
  a = card_decoder(a)
  return a

def main():
  num = int(input())
  s = list(input().split())
  bubble1 = bubble_sort(s,num)
  select1 = selection_sort(s,num)
  print(' '.join(bubble1))
  print(is_stable(s,bubble1))
  print(' '.join(select1))
  print(is_stable(s,select1))

def is_stable(a_in, a_out):
  v_in = card_encoder2(a_in)
  n = len(a_in)
  for i in range(0,n):
    for j in range(i + 1,n):
      for a in range(0,n):
        for b in range(a + 1,n):
          if v_in[i] == v_in[j] and a_in[i] == a_out[b] and a_in[j] == a_out[a]:
            return 'Not stable'
  return 'Stable'

main()
