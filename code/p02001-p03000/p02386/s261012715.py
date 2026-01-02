def roll(l, command):
    '''
    return rolled list

    l : string list
    command: string
    '''
    res = []
    i = -1
    if command =='N':
        res = [l[i+2], l[i+6], l[i+3], l[i+4], l[i+1], l[i+5]]
    if command =='S':
        res = [l[i+5], l[i+1], l[i+3], l[i+4], l[i+6], l[i+2]]
    if command =='E':
        res = [l[i+4], l[i+2], l[i+1], l[i+6], l[i+5], l[i+3]]
    if command =='W':
        res = [l[i+3], l[i+2], l[i+6], l[i+1], l[i+5], l[i+4]]

    return res

def spin(l):
    '''
    return right sppined list

    l : string list
    '''

    i = -1
    res = [l[i+1], l[i+3], l[i+5], l[i+2], l[i+4], l[i+6]]

    return res
def has_same_faces(a, b):
    '''
    check if all elements of a are equel to those of b.
    a : string list
    b : string list
    '''
    return set(a) == set(b)

def is_identical_lists(a, b):
    for x, y in zip(a, b):
        if x != y:
            return False

    return True

def check_two_dice(a, b):
    if not has_same_faces(a, b):
        return False
    
    orig_a = a[:]

    #roll and spin to check
    for i in range(6):
        if 1 <= i <= 3:
            a = roll(a, "N")
        elif i == 4:
            pass
            a = orig_a[:]
            a = roll(a, "W")
        elif i == 5:
            a = orig_a[:]
            a = roll(a, "E")

        # spin 4 times
        for _ in range(4): #spin 3 times
            a = spin(a)
            if is_identical_lists(a, b):
                return True
        
    return False

def check_all_different(dice):
    '''
    if all dice are different, return True

    dice : string list

    '''
    for i in range(len(dice)):
        if i == 0:
            continue
        for j in range(i):
            res = check_two_dice(dice[i], dice[j])

            if res:
                return False
    
    return True


if __name__ == "__main__":
    res = False
    n = int(input())
    dice = []
    for _ in range(n): 
        dice.append(input().split())

    res = check_all_different(dice)

    print("Yes") if res else print("No")



