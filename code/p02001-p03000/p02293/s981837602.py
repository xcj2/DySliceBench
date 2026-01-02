import sys
 
 
def get_line(line_info):
    for line_pair in line_info:
        line_axis = tuple(map(int, line_pair))
        p0, p1, p2, p3 = (x + y * 1j for x, y in zip(line_axis[::2], line_axis[1::2]))
        # print(p0, p1, p2, p3)
        if dot(p1 - p0, p3 - p2) == 0:
            print('1')
        elif cross(p1 - p0, p3 - p2) == 0:
            print('2')
        else:
            print('0')
    return line_info
 
 
def cross(a, b):
    return a.real * b.imag - a.imag * b.real
 
 
def dot(a, b):
    return a.real * b.real + a.imag * b.imag
 
 
if __name__ == '__main__':
    _input = sys.stdin.readlines()
    questions = int(_input[0])
    lines = map(lambda x: x.split(), _input[1:])
    ans = get_line(lines)