def determine_string_code(bracket_string):
  brackets_left = 0 # )
  brackets_right = 0 # (
  for char in bracket_string:
    if char == "(":
      brackets_right += 1
    else:
      if brackets_right > 0:
        brackets_right -= 1
      else:
        brackets_left += 1
  return (brackets_left, brackets_right)

def build_left(in_list):
  in_list.sort(key=lambda x: x[0])
  final_res = (0, 0)
  for res in in_list:
    if res[0]>final_res[1]:
      final_res = (final_res[0]+res[0]-final_res[1], res[1])
    elif res[0]<final_res[1]:
      final_res = (final_res[0], res[1]+final_res[1]-res[0])
    else:
      final_res = (final_res[0], res[1])
  return final_res

def build_right(in_list):
  in_list.sort(key=lambda x: x[1])
  final_res = (0, 0)
  for res in in_list:
    if final_res[0]>res[1]:
      final_res = (res[0]+final_res[0]-res[1], final_res[1])
    elif final_res[0]<res[1]:
      final_res = (res[0], final_res[1]+res[1]-final_res[0])
    else:
      final_res = (res[0], final_res[1])
  return final_res

n = int(input())
residues = list()
for _ in range(n):
  new_string = input()
  residues.append(determine_string_code(new_string))
first_half = list()
second_half = list()
for res in residues:
  if res[1] > res[0]:
    first_half.append(res)
  else:
    second_half.append(res)
first_res = build_left(first_half)
second_res = build_right(second_half)
if first_res[0] == 0 and second_res[1] == 0 and first_res[1] == second_res[0]:
  print("Yes")
else:
  print("No")