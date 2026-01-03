

# all_split("abc") -> [['abc'], ['ab', 'c'], ['a', 'bc'], ['a', 'b', 'c']]
def all_split(s):
    if len(s) == 1:
        return [s]
    
    ans = []
    for i in range(2 ** (len(s) - 1)):
        b = list(map(int, format(i, "0" + str(len(s) - 1) + "b")))
        ans.append(split(s, b))
    return ans


def split(s, split_positions):
    assert len(s) - 1 == len(split_positions)

    ans = []
    pre = 0
    for i, is_split in enumerate(split_positions, start=1):
        if is_split:
            ans.append(s[pre:i])
            pre = i

    ans.append(s[pre:])
    return ans


def main():
    s = input()
    ans = 0
    for a in all_split(s):
        ans += eval("+".join(a))
    print(ans)


if __name__ == '__main__':
    main()
