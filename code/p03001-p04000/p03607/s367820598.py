#feel like this is to easy

def read_input():
  n = int(input())
  a = []
  for i in range(n):
    a.append(int(input()))
  return n,a

def TLE():
  n,a = read_input()
  sheet = []
  for item in a:
    if item not in sheet:
      sheet.append(item)
    else:
      sheet.pop(sheet.index(item))
  print(len(sheet))
  
def TLE2():
  n,a = read_input()
  items = list(set(a))
  count = 0
  for item in items:
    if a.count(item)%2 != 0:
      count += 1
  print(count)

def main():
  n,a = read_input()
  a.sort()
  items = list(set(a)).sort()
  t = 1
  count = 0
  for i in range(len(a)):
    if i+1 == len(a):
      count += t%2
      break
    if a[i] == a[i+1]:
      t += 1
    else:
      count += t%2
      t = 1
  print(count)

if __name__ == '__main__':
  main()