def test(x, j):
    # X, A = map(int, input().split())
    A = j.split()
    numbers = []
    result = True
    for i in A:
        numbers.append(int(i))
    result = sorted(numbers)
    if (result == True):
        print("YES")
        return "YES"
    if (result == False):
        # numbers2 = numbers[:]
        for i in range(len(numbers)):
            for x in range(i+1, len(numbers)):
                numbers2 = numbers[:]
                if swap(numbers2, i, x) == True:
                    print("YES")
                    return "TRUE"
    print("NO")
    return "FALSE"


def sorted(list):
    result = True
    for i in range(len(list)):
        if i < len(list) - 1:
            if (list[i] > list[i+1]):
                result = False
    return result


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return sorted(list)


N = int(input())
p = input()
test(N, p)
