def get_order(numbers, originals):
    
    from math import factorial
    from copy import copy
    numbers = copy(numbers)
    originals = copy(originals)
    
    total = 0
    while numbers:
        number = numbers.pop(0)
        number_index = originals.index(number)
        originals.pop(number_index)
        count = (number_index ) * factorial(len(originals))
        total += count
    return total
        
def get_next_int():
    return int(float(input()))
def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])

def main(print=__builtins__.print):
    n = get_next_int()
    
    a = list(get_next_ints())
    b = list(get_next_ints())
    originals = list(map(int, range(1, n+1)))
    print(abs(get_order(a, originals) - get_order(b, originals)))

if __name__ == '__main__':
    main()
    