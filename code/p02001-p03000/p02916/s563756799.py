def _input():
    n = int(input())
    a = input().split()
    foods = convrt_to_int(a)
    b = input().split()
    satisfaction = convrt_to_int(b)
    c = input().split()
    add = convrt_to_int(c)
    return foods, satisfaction, add

def convrt_to_int(array):
    int_array = []
    for i in array:
        int_array.append(int(i))
    return int_array

def calc(foods, satisfaction, add):
    counter = 0
    total = satisfaction[foods[0] - 1]
    for i in foods:
        if counter == 0:
            counter += 1
            continue
        if i == foods[counter - 1] + 1:
            option = optional(i - 1,add)
            total += satisfaction[i - 1]
            total += option
        else:
            total += satisfaction[i - 1]
        counter += 1
    return total

def optional(index, add):
    return add[index - 1]


if __name__ == "__main__":
    foods, satisfaction, add = _input()
    print(calc(foods, satisfaction, add))