def is_yy(st):
    st = int(st)
    if (0 <= st <= 99):
        return True
    return False
    
def is_mm(st):
    st = int(st)
    if (1 <= st <= 12):
        return True
    return False

def get_ans(head, tail):
    if (is_yy(head) and is_mm(tail)) and (is_yy(tail) and is_mm(head)):
        return 'AMBIGUOUS'
    elif (is_yy(head) and is_mm(tail)) and not (is_yy(tail) and is_mm(head)):
        return 'YYMM'
    elif not (is_yy(head) and is_mm(tail)) and (is_yy(tail) and is_mm(head)):
        return 'MMYY'
    else:
        return 'NA'

s = input()
head = s[0:2]
tail = s[2:]
print(get_ans(head, tail))
    