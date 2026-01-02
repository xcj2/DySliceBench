def main():
  str = input()
  first = str[:2]
  second = str[2:]
  first = change(first)
  second = change(second)
  f_y = 0; s_y = 0;
  f_y = check_y(first)
  s_y = check_y(second)
  if(f_y == 0 and s_y == 0):
    print("AMBIGUOUS")
  elif(f_y == 0 and s_y == 1):
    print("MMYY")
  elif(f_y == 1 and s_y == 0):
    print("YYMM")
  else:
    print("NA")
    
def change(str):
  if(str[0] == "0"):
    return int(str[1])
  else:
    return int(str)
  
def check_y(num):
  if(num == 0 or num > 12):
    return 1
  else:
    return 0
  
if __name__ == "__main__":
  main()

