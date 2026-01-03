n = int(input())
s_list = list(input())
def main():
  animal_list = [None] * n
  sonzai = False
  #SS
  if not sonzai:
    animal_list[0] = True
    animal_list[1] = True
    animal_list = create_animal_list(animal_list)
    sonzai = is_valid_list(animal_list)
  if not sonzai:
    animal_list[0] = True
    animal_list[1] = False
    animal_list = create_animal_list(animal_list)
    sonzai = is_valid_list(animal_list)
  if not sonzai:
    animal_list[0] = False
    animal_list[1] = False
    animal_list = create_animal_list(animal_list)
    sonzai = is_valid_list(animal_list)
  if not sonzai:
    animal_list[0] = False
    animal_list[1] = True
    animal_list = create_animal_list(animal_list)
    sonzai = is_valid_list(animal_list)
  if not sonzai:
    print(-1)
  else:
    animal_list2 = []
    for animal in animal_list:
      if animal:
        animal_list2.append("S")
      else:
        animal_list2.append("W")
    animal_list2 = "".join(animal_list2)
    print(animal_list2)
def is_valid_list(animal_list):
  return is_ok(animal_list, 0) and is_ok(animal_list,-1)
  
def is_ok(animal_list, index):
  if animal_list[index%n]:
    if s_list[index%n] == "o":
      return animal_list[(index+1)%n] == animal_list[index-1]
    else:
      return not (animal_list[(index+1)%n] == animal_list[index-1])
  else:
    if s_list[index%n] == "o":
      return not (animal_list[(index+1)%n] == animal_list[index-1])
    else:
      return (animal_list[(index+1)%n] == animal_list[index-1])
def create_animal_list(animal_list):
  for index in range(2, len(animal_list)):
    if animal_list[index-1]:
      if s_list[index-1] == "o":
        animal_list[index] = animal_list[index-2]
      else:
        animal_list[index] = not animal_list[index-2]
    else:
      if s_list[index-1] == "o":
        animal_list[index] = not animal_list[index-2]
      else:
        animal_list[index] = animal_list[index-2]
  return animal_list
main()