S = input()
K = int(input())

REPLACED = '_'


def get_start(s):
    i = 1
    while i < len(s):
        if s[0] != s[i]:
            break
        i += 1
    return s[:i]


def replace(s):
    characters = list(s)
    s_length = len(s)
    s_types = len(set(s))

    if s_length == s_types:
        return s

    start = get_start(s)
    if len(start) == 1:
        pass
    elif len(start) % 2 == 0:
        for i in range(0, len(start), 2):
            characters[i] = REPLACED
    else:
        for i in range(1, len(start), 2):
            characters[i] = REPLACED

    i = 0
    while i < s_length - 1:
        chunk = characters[i:i + 3]

        if REPLACED in chunk:
            i += 1
            continue

        chunk_length = len(chunk)
        chunk_types = len(set(chunk))
        if chunk_length == 1:
            break
        elif chunk_length == 2:
            if chunk_types == 2:
                break
            else:
                characters[i + 1] = REPLACED
                break
        elif chunk_length == 3:
            if chunk_types == 3:
                i += 2
                continue
            elif chunk_types == 2:
                if chunk[0] == chunk[1]:
                    characters[i] = REPLACED
                    i += 2
                    continue
                elif chunk[1] == chunk[2]:
                    characters[i + 2] = REPLACED
                    i += 3
                    continue
                else:
                    i += 2
                    continue
            else:
                characters[i + 1] = REPLACED
                i += 2
                continue
        else:
            raise Exception

    return ''.join(characters)


def check(s, k):
    s_length = len(s)
    s_types = len(set(s))
    if (s_types == 1) or (s_length == 1):
        return s_length * k // 2
    elif s_types == s_length:
        return 0
    else:
        replaced_s = replace(s)
        replaced_count = replaced_s.count(REPLACED)
        if replaced_s[0] == replaced_s[-1] and replaced_s[0] != REPLACED:
            return (replaced_count * k) + (k - 1)
        else:
            return replaced_count * k


print(check(S, K))
