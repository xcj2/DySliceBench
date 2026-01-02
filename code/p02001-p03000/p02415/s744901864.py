def is_alphabet(s):
    if (0x41 <= ord(s) and ord(s) <= 0x5A) or (0x61 <= ord(s) and ord(s) <= 0x7A):
        return True
    else:
        return False


def is_upper(s):
    if 0x41 <= ord(s) and ord(s) <= 0x5A:
        return True
    else:
        return False


def is_lower(s):
    if 0x61 <= ord(s) and ord(s) <= 0x7A:
        return True
    else:
        return False


S = input().strip()
ans = ""

for s in S:
    if is_alphabet(s):
        if is_upper(s):
            ans += s.lower()
        else:
            ans += s.upper()
    else:
        ans += s

print(ans)

