import random

b = input()


def ans_1():
    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    else:
        print("C")


def ans_2():
    Dic = {"A": "T", "T": "A", "C": "G", "G": "C"}
    print(Dic[b])


def ans_3():
    keys = ["A", "T", "C", "G"]
    values = keys[:]
    values[0], values[1] = values[1], values[0]
    values[2], values[3] = values[3], values[2]

    Dic = dict(zip(keys, values))
    print(Dic[b])


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


def ans_4():
    Dic = {"A": "T", "C": "G"}
    if get_key_from_value(Dic, b):
        print(get_key_from_value(Dic, b))
    else:
        print(Dic[b])


method = random.randrange(4)
if method == 0:
    ans_1()
elif method == 1:
    ans_2()
elif method == 2:
    ans_3()
else:
    ans_4()