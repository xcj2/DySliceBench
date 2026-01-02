import re

S_IN = input()
T = input()
U = 'UNRESTORABLE'

def get_substring(start_index, len, str):
    """
    get substring.
    """
    return str[start_index:start_index + len]

def validate(str, cmp):
    """
    validate.
    """
    is_valid = True
    for index, c in enumerate(str):
        if c == '?':
            continue
        elif c == cmp[index]:
            continue
        else:
            is_valid = False
            break
    return is_valid

def make_string(start_index, replacement, str):
    """
    make string.
    """
    length = len(replacement)
    before = str[:start_index].replace('?', 'a')
    repl = replacement
    after = str[start_index + length:].replace('?', 'a')
    return before + repl + after

def main():
    """
    main function
    """
    s_length = len(S_IN)
    t_length = len(T)
    limit = s_length - t_length + 1

    if limit < 0:
        print(U)

    list = []
    # print("limit - {0}".format(limit))
    for i in range(limit):
        substr = get_substring(i, t_length, S_IN)
        # print(substr)
        if validate(substr, T):
            list.append(make_string(i, T, S_IN))

    list.sort()
    ans = list[0] if bool(list) else U

    print(ans)

if __name__ == '__main__':
    main()