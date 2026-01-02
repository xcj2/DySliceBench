#!/mnt/c/Users/moiki/bash/env/bin/python
s = input()

i_t = 0
text="keyence"
continue_ = False

def check1(s, text):
    if s.find(text) == 0:
        return True
    else:
        return False
def check3(s, text):
    rev_text = text[::-1]
    rev_s    =    s[::-1]

    if rev_s.find(rev_text) == 0:
        return True
    else:
        return False

def check2(s, text):
    is_ok = False
    for i in range(1, 7): # 1 to 6
        first  = text[:i]
        second = text[i:]
        # print("first: ", first)
        # print("second: ", second)
        if check1(s, first) and check3(s,second):
            is_ok = True
            break
    if is_ok:
        return True
    else:
        return False

    
    
# print(check1(s, text) , check2(s, text) , check3(s, text))

if check1(s, text) or check2(s, text) or check3(s, text):
    print("YES")
else:
    print("NO")
