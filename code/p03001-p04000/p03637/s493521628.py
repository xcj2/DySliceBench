def count_four(lst):
    counter = 0
    for i in lst:
        if i%4 == 0:
            counter += 1
    return counter

def count_two(lst):
    counter = 0
    for i in lst:
        if i%2 == 0:
            counter += 1
    return counter

n = int(input())
lst = list(map(int,input().split()))

def solve(lst):
    four = count_four(lst)
    two = count_two(lst) - four
    others = n - four - two

    if two == 0:
        if four + 1 - others >= 0:
            return "Yes"
        else:
            return "No"

    if two > 0:
        two = 1
        if four + 1 - others - two >= 0:
            return "Yes"
        else:
            return "No"


print(solve(lst))