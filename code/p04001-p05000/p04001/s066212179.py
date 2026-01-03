import copy

s = input()

def value(s, adding_list):
    insert_index = []
    for index in range(len(adding_list)):
        if adding_list[index]:
            insert_index.append(index)

    if len(insert_index) == 0:
        return int(s)

    value_list = []

    for index in range(len(insert_index)):
        if index == 0:
            value_list.append(s[0:insert_index[index]+1])
        if index < len(insert_index)-1:
            value_list.append(s[(insert_index[index]+1) : insert_index[index+1]+1])

        if index == len(insert_index)-1:
            value_list.append(s[insert_index[index]+1:])

    ret_val = 0
    for value in value_list:
        ret_val += int(value)

    return ret_val

def dfs(adding_list, changing_index):
    sum = 0
    if changing_index == len(s)-2:
        return value(s, adding_list)
    else:
        changing_index += 1
        new_adding_list = copy.copy(adding_list)
        sum += dfs(new_adding_list, changing_index)

        new_adding_list = copy.copy(adding_list)
        new_adding_list[changing_index] = True
        sum += dfs(new_adding_list, changing_index)
        return sum

def main():
    if len(s) > 1:
        ret_val = 0
        plus_list = [False for _ in range(len(s)-1)]
        ret_val += dfs(plus_list, 0)

        plus_list = [False for _ in range(len(s)-1)]
        plus_list[0] = True
        ret_val += dfs(plus_list, 0)
        print(ret_val)
    else:
        print(s)

main()