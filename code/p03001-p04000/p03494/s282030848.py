

def is_odd(num):
    return num % 2 != 0

def odd_in_list(num_list):
    for num in num_list:
        if is_odd(num):
            return True
    
    return False

def half(num):
    return num / 2

def shift_only(num_list, counter):
    if odd_in_list(num_list):
        print('its over')
        return counter
    else:
        new_list = list(map(half, num_list))
        counter += 1
        print('continue', num_list, counter)
        return shift_only(new_list, counter)


n = int(input())

a_list = list(map(int, input().split()))


counter = 0
flag = True

while flag:
    for i in range(n):
        # print(a_list[i])
        if a_list[i] % 2 != 0:
            # print('is odd')
            flag = False
            break
        else:
            continue
    
    if not flag:
        break
    
    for i in range(n):
        a_list[i] /= 2
    counter += 1

    # print('-----loop------')
    # print(a_list, counter)

print(counter)