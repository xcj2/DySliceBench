import re


def code_shift(c, n_shift):
    return ord('a') + (ord(c) + n_shift - ord('a')) % 26


def get_candidate_plain(cipher, sym_ids, n_shift):
    plain = []
    for i, c in enumerate(cipher):
        if i not in sym_ids:
            plain.append(chr(code_shift(c, n_shift)))
        else:
            plain.append(c)
    plain = ''.join(plain)
    return plain


def decrypt(cipher):
    sym_ids = [m.start() for m in re.finditer(r'[\.\n\s]', cipher)]
    keyword = ['the', 'this', 'that']

    n_shift = 0
    while True:
        plain = get_candidate_plain(cipher, sym_ids, n_shift)
        for k in keyword:
            if plain.find(k) != -1:
                return plain
        n_shift += 1


if __name__ == '__main__':
    while True:
        try:
            cipher = input()
            print(decrypt(cipher))
        except:
            break
