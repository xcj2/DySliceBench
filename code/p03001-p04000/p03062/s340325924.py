def get_next_int():
    return int(float(input()))
def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])

def main():
    n = get_next_int()
    numbers = get_next_ints()
    
    minimum_number = abs(numbers[0])
    
    count_of_minus = 0
    total = 0
    
    for number in numbers:
        if number < 0:
            count_of_minus += 1
        abs_number = abs(number)
        total += abs_number
        if abs_number < minimum_number:
            minimum_number = abs_number
        
    if count_of_minus % 2 == 1:
        total -= minimum_number * 2
    
    print(total)
    
if __name__ == '__main__':
    main()
