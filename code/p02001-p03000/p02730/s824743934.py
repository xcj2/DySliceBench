word = input()

length = int((len(word) - 1) / 2)


def judge_a(kaibun):
    if kaibun == kaibun[::-1]:
        return True
    return False


def judge_b(kaibun):
    if kaibun[:length] == kaibun[length-1::-1]:
        return True
    return False


def judge_c(kaibun):
    if kaibun[length + 1:] == kaibun[:length:-1]:
        return True
    return False


if judge_a(word) == True:
    if judge_b(word) == True:
        if judge_c(word) == True:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
