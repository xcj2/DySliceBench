def get_next_int():
    return int(input().rstrip("\n"))


def get_next_ints(delim=" "):
    return tuple([int(x) for x in input().rstrip("\n").split(delim)])


def main():
    n = get_next_int()

    a = get_next_ints()
    b = get_next_ints()

    a_offsets = []
    b_offsets = []
    for i in range(n):
        a_offsets.append(str(a[i] ^ a[i - 1]))
        b_offsets.append(str(b[i] ^ b[i - 1]))
    #print(a_offsets)
    #print(b_offsets)
    a_text = " ".join(a_offsets)
    b_text = " ".join(b_offsets)
    target_text = a_text + " " + a_text
    start_pos = 0
    if target_text.find(b_text, start_pos) >= 0:
        fisrt_pos = target_text.find(b_text, start_pos)
        fisrt_pos_diff = target_text[:fisrt_pos].count(" ")
        fisrt_xor_diff = b[0] ^ a[fisrt_pos_diff]
        print(fisrt_pos_diff, fisrt_xor_diff)
        if target_text.find(b_text, fisrt_pos+1) >= 0:
            second_pos = target_text.find(b_text, fisrt_pos+1)
            second_pos_diff = target_text[:second_pos].count(" ")
            if second_pos_diff < len(a):
                second_xor_diff = b[0] ^ a[second_pos_diff]
                print(second_pos_diff, second_xor_diff)
                interval = (second_pos_diff - fisrt_pos_diff)
                remain = (n - second_pos_diff - 1) // (second_pos_diff - fisrt_pos_diff)
                for i in range(remain):
                    print(second_pos_diff + interval * (i + 1), [fisrt_xor_diff,second_xor_diff ][i % 2])

if __name__ == '__main__':
    main()
