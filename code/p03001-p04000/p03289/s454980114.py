def check_string(s):
  if(a_exist(s)):
    c_index = c_find(s)
    if(c_index != False):
      if(is_lower(s,c_index)):
        return 'AC'
  return 'WA'

def a_exist(s):
  if(s[0] == 'A'):
    return True
  else:
    return False

def c_find(s):
  c_cnt = 0
  for i in range(len(s)):
    if(i < 2):
      continue
    if(i == len(s)-1):
      continue
    if(s[i] == 'C'):
      c_cnt += 1
      index = i
  if(c_cnt == 1):
    return index
  else:
    return False

def is_lower(s,index):
  for i in range(len(s)):
    if(i == 0):
      continue
    if(i == index):
      continue
    if(s[i].islower() == False):
      return False
  return True

if __name__ == '__main__':
  s = input()
  print(check_string(s))