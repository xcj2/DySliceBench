def gcd(a, b):
    
    if a == b:
        return a
    
    small = large = 0
    if a > b:
        small = b
        large = a
    else:
        small = a
        large = b
    
    while True:
        
        d, m = divmod(large, small)
        if m == 0:
            return small
        else:
            large = small
            small = m
    
    
    

def get_next_int():
    return int(float(input()))
def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])

def main():
    n = get_next_int()
    numbers = get_next_ints()
    
    current = numbers[0]
    candidates = {numbers[1]}
    
    for number in numbers[1:]:
        
        next_candidates = {}
        for candidate in candidates:
            next_candidates[gcd(candidate, number)] = 1
        candidates = next_candidates
        #print(candidates.keys())
        candidates[current] = 1
        current = gcd(current, number)    
    
    print(max(candidates.keys()))
    
if __name__ == '__main__':
    main()
