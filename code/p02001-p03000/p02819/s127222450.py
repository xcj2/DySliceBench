import math


def is_prime(x):
    root = int(math.sqrt(x))+1
    if x == 2:
        return True
    else:
        for i in range(2, root+1):
            if x % i == 0:
                return False
    return True


'''
def find_prime(x):
    while True:
        if x == 2:
            return x
        else:
            for i in range(2, x+1):
                if x % i == 0:
                    if i == x:
                        return x
                    else:
                        break
                else:
                    continue
            x += 1
'''


def main():
    x = int(input())
    while True:
        if is_prime(x) == False:
            x += 1
        else:
            print(x)
            break


if __name__ == "__main__":
    main()
