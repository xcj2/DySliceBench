def north(d):
    return [d[1], d[5], d[2], d[3], d[0], d[4]]

def east(d):
    return [d[3], d[1], d[0], d[5], d[4], d[2]]

def south(d):
    return [d[4], d[0], d[2], d[3], d[5], d[1]]

def west(d):
    return [d[2], d[1], d[5], d[0], d[4], d[3]]

numbers = list(map(int, input().split()))
directions = list(input())

for d in directions:
    if d == "N":
        numbers = north(numbers)
    elif d == "E":
        numbers = east(numbers)
    elif d == "S":
        numbers = south(numbers)
    elif d == "W":
        numbers = west(numbers)

print(numbers[0])