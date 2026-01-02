# coding: utf-8

C = []
for i in range(3):
    _c = list(map(int, input().split()))
    C.append(_c)

#print(C)

a = [0, 0, 0]
b = [0, 0, 0]

ans_flag = 'No'
a1_flag = False
a2_flag = False
a3_flag = False

def check_b(_b):
    b_count = 0
    for i_b in _b:
        if i_b >= 0 and i_b <= 100:
            b_count += 1
    
    if b_count >= 3:
        return True
    else:
        return False

def check_succes(a_val,b, c):
    b_count2 = 0
    i = 0
    for i_b in b:
        if i_b == c[i] - a_val:
            b_count2 += 1
        i += 1
    if b_count2 >= 3:
        return True
    else:
        return False

main_count = 0

for a_1 in range(101):
    a[0] = a_1
    for x in range(len(b)):
        b[x] = C[0][x] - a[0]
    #main_count += 1
    #if main_count == 1:
        #print("b = {0}".format(b))

    if check_b(b):
        a1_flag = True
        for a_2 in range(101):
            a[1] = a_2
            if check_succes(a[1], b, C[1]):
                a2_flag = True
                for a_3 in range(101):
                    a[2]= a_3
                    if check_succes(a[2], b, C[2]):
                        a3_flag = True
                        ans_flag = 'Yes'



print(ans_flag)


#print('--debug--')
#print(a1_flag)
#print(a2_flag)
#print(a3_flag)


def check_succes(a_val,b, c):
    b_count2 = 0
    i = 0
    for i_b in _b:
        if i_b == c[i] - a_val:
            b_count2 += 1
        i += 1
    if b_count2 >= 3:
        return True
    else:
        return False

