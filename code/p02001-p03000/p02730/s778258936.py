def check_2(s):
    n = s.__len__()
    x = (n-1)/2
    x = abs(x)
    x = int(x)
    temp = s[0:x]
    if isPalindrome(temp) == 1:
        return 1
    else:
        return 0

def check_3(s):
    n = s.__len__()
    x = (n + 3) / 2
    x = abs(x)
    x = int(x)
    temp = s[n:x]
    if isPalindrome(temp) == 1:
        return 1
    else:
        return 0
def reverse(s):
    return s[::-1]


def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return 1
    return 0

if __name__ == "__main__":
    s = input()
    result = 0
    if isPalindrome(s) == 1:
        result = 1
        if check_2(s) == 1:
            result = 1
            if check_3(s) == 1:
                result = 1
            else:
                result = 0
        else:
            result = 0
    else:
        result = 0
    if result == 1:
        print("Yes")
    else:
        print("No")