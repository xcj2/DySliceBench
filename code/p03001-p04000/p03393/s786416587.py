import string

S = input()

alphabet = string.ascii_lowercase

def least_char_notin(s):
    for c in alphabet:
        if c not in s:
            return c
    return None

def next_char(c):
    return chr(ord(c)+1)

def is_diverse(s):
    if len(s) == len(set(s)):
        return True
    return False

def next_diverse(s):
    if len(s) < 26:
        return s + least_char_notin(s)
    else:
        for i in range(1,len(s)+1):
            c = s[-i]
            prefix = s[:-i]
            d = next_char(c)
            while d in alphabet:
                if is_diverse(prefix + d):
                    return prefix + d
                d = next_char(d)
        return -1

print(next_diverse(S))