import sys


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


# A
def A():
    s = input()
    if s == "Sunny":
        print("Cloudy")
    elif s == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")
    return


# B
def B():
    s = S()
    for i in range(len(s)):
        if i % 2:
            if s[i] not in ["L", "U", "D"]:
                print("No")
                return
        else:
            if s[i] not in ["R", "U", "D"]:
                print("No")
                return
    print("Yes")
    return


# C
def C():
    return


# D
def D():
    return


# E
def E():
    return


# F
def F():
    return


# Unittest
def resolve():
    B()
    return


# Solve
if __name__ == "__main__":
    B()
