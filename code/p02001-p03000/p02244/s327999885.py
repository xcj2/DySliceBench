
def put_queen(field,r,c):
    return field | 1<<(r*8+c)

def check_queen(field,r,c):
    return field & 1<<(r*8+c)

def view_field(field):
    for i in range(8):
        for j in range(8):
            print('Q' if check_queen(field,i,j) else '.', end='')
        print()

def placeable(field,r,c):
    for i in range(8):
        if check_queen(field,r,i) or check_queen(field,i,c):
            return False
    if r>c:
        r1,c1 = r-c,0
    else:
        r1,c1 = 0,c-r

    if r>7-c:
        r2,c2 = r-(7-c),7
    else:
        r2,c2 = 0,c+r

    for i in range(8):
        if 0<=r1+i<8 and 0<=c1+i<8 and check_queen(field,r1+i,c1+i)     \
            or                                                          \
            0<=r2+i<8 and 0<=c2-i<8 and check_queen(field,r2+i,c2-i):
            return False

    return True


def make_field(field, queen_num):
    if queen_num==8:
        return field
    for i in range(8):
        for j in range(8):
            if placeable(field,i,j):
                solve_field = make_field(put_queen(field,i,j),queen_num+1)
                if not solve_field==2**64:
                    return solve_field
    return 2**64
    
k=int(input())
field=0
for i in range(k):
    r,c=map(int,input().split())
    field = put_queen(field,r,c)

view_field(make_field(field,k))




