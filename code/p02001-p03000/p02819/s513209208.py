X = int(input())

import math
import copy
def sieve_of_eratosthenes(target):
    dest = int(math.sqrt(target))
    target_list = list(range(2, target + 1))
    prime_list = []
    
    while True:
        num_min = min(target_list)
        if num_min >= dest:
            prime_list.extend(target_list)
            break
        prime_list.append(num_min)
 
 
        i = 0
 
        while True:
            if i >= len(target_list):
                break
            elif target_list[i] % num_min == 0:
                target_list.pop(i)
            i += 1
    return prime_list

def binary_search_exist(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        center = int((left + right) / 2)
        if target == nums[center]:
            return True
        elif target < nums[center]:
            right = center
        else:
            left = center + 1
    return False

def binary_search(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        center = int((left + right) / 2)
        if target == nums[center]:
            return center
        elif target < nums[center]:
            right = center
        else:
            left = center + 1
    return right

prime_list = sieve_of_eratosthenes(X + 1000)
if binary_search_exist(prime_list, X):
    print(X)
else:
    prime_list.append(X)
    prime_list.sort()
    r = binary_search(prime_list, X)
    print(prime_list[r + 1])