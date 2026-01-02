def get_char_value(char):
    if char == "C":
        return 1;
    if char == "A":
        return 2;
    if char == "G":
        return 3;
    if char == "T":
        return 4;

def get_string_value(string):
    s = 0;
    p = 1;
    for char in string:
        s += p * get_char_value(char);
        p *= 5;
    return s;

def h1(value, M):
    return value % M;

def h2(value, M):
    return 1 + value % (M - 1);

def insert(dic, M, string):
    value = get_string_value(string);
    h1_value = h1(value, M);
    h2_value = h2(value, M);
    i = 0;
    while True:
        index = (h1_value + i * h2_value) % M;
        if dic[index] == string:
            break;
        elif dic[index] is None:
            dic[index] = string;
            break;
        i += 1;

def find(dic, M, string):
    value = get_string_value(string);
    h1_value = h1(value, M);
    h2_value = h2(value, M);
    i = 0;
    while True:
        index = (h1_value + i * h2_value) % M;
        if dic[index] == string:
            return True;
        elif dic[index] is None:
            return False;
        i += 1;

M = 1046527;
dic = [None for i in range(M)];
count = int(input());
for i in range(count):
    command = input().split();
    if command[0] == "insert":
        insert(dic, M, command[1]);
    elif command[0] == "find":
        if find(dic, M, command[1]):
            print("yes");
        else:
            print("no");


