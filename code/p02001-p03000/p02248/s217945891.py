def calc_prefix(pattern):
    """
        a b|c   a b[c] # matched        matched_len = 2
        1 2
        a b c|  a b[c] # increase       matched_len = 3
        1 2 3

        a b|c   a b[d] # not matched    matched_len = 2
        1 2
        a|b c   a b[d] # not matched    matched_len = 1
        1 2
       |a b c   a b[d] # not matched    matched_len = 0
        1 2 0

        a b|c   a b[a] # not matched    matched_len = 2
        1 2
        a|b c   a b[a] # not matched    matched_len = 1
        1 2
       |a b c   a b[a] # matched        matched_len = 0
        1 2
        a|b c   a b[a] # increase       matched_len = 1
    """
    pattern_len = len(pattern)
    # matched_len = 0
    matched_table = [0] * pattern_len
    for calc_idx in range(1, pattern_len):
        matched_len = matched_table[calc_idx - 1]
        while matched_len > 0 and pattern[matched_len] != pattern[calc_idx]:  # not matched
            matched_len = matched_table[matched_len - 1]  # matched_lenが-1される
        if pattern[matched_len] == pattern[calc_idx]:  # matched!
            matched_len += 1
        matched_table[calc_idx] = matched_len
    return matched_table


def kmp(text, pattern):
    matched_table = calc_prefix(pattern)
    pattern_len = len(pattern)
    text_len = len(text)
    text_idx = 0
    pattern_idx = 0
    matched_idxs = []
    while text_idx < text_len:
        if pattern[pattern_idx] == text[text_idx]:
            pattern_idx += 1
            text_idx += 1
        if pattern_idx == pattern_len:
            matched_idxs.append(text_idx - pattern_idx)
            pattern_idx = matched_table[pattern_idx - 1]
        elif text_idx < text_len and pattern[pattern_idx] != text[text_idx]:
            if pattern_idx == 0:
                text_idx += 1
            else:
                pattern_idx = matched_table[pattern_idx - 1]

    return matched_idxs


def main():
    text = input()
    pattern = input()
    matched = kmp(text, pattern)
    for match_idx in matched:
        print(match_idx)


if __name__ == "__main__":
    main()

