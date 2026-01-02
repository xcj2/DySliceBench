def main():
  size = input()
  a = list(map(int, input().split()))
  a = merge_sort(a)
  
  alice_res = 0
  bob_res = 0
  
  for i in range(len(a)):
    if i%2 == 0:
      alice_res += a[i]
    else:
      bob_res += a[i]
 
  print(alice_res-bob_res)
  
 
def merge_sort(array):
  if len(array)<=1:
    return array
  
  spl_size = len(array)//2
  
  left_list = merge_sort(array[:spl_size])
  right_list = merge_sort(array[spl_size:])
  
  return merge_list(left_list, right_list)
 
 
def merge_list(left_list, right_list):
  left_index = 0
  right_index = 0
  sorted_list = []
  
  while left_index<len(left_list) and right_index<len(right_list):
    if left_list[left_index] < right_list[right_index]:
      sorted_list.append(right_list[right_index])
      right_index+=1
    else:
      sorted_list.append(left_list[left_index])
      left_index+=1
      
  if left_index == len(left_list):
    sorted_list.extend(right_list[right_index:])
  if right_index == len(right_list):
    sorted_list.extend(left_list[left_index:])
      
  return sorted_list
    
                          
main()