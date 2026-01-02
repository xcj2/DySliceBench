M = 1046527
POW = [pow(4, i) for i in range(13)]


def insert(dic, string):
    # i = 0
    # while dic[(hash1(string) + i*hash2(string)) % M]:
    #     i += 1
    # dic[(hash1(string) + i*hash2(string)) % M] = string
    dic[get_key(string)] = string


def find(dic, string):
    # i = 0
    # while dic[(hash1(string) + i*hash2(string)) % M] and dic[(hash1(string) + i*hash2(string)) % M] != string:
    #     i += 1
    # return True if dic[(hash1(string) + i*hash2(string)) % M] == string else False
    # print(dic[get_key(string)], string)
    return True if dic[get_key(string)] == string else False


def get_num(char):
    if char == "A":
        return 1
    elif char == "C":
        return 2
    elif char == "G":
        return 3
    else:
        return 4


def get_key(string):
    num = 0
    for i in range(len(string)):
        num += POW[i] * get_num(string[i])
    return num


def main():
    n = int(input())
    dic = [None] * POW[12]
    # print(dic)
    for i in range(n):
        order, string = input().split()
        if order == "insert":
            insert(dic, string)
        else:
            if find(dic, string):
                print('yes')
            else:
                print('no')


if __name__ == "__main__":
    main()

