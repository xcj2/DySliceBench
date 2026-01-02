import sys
write = sys.stdout.write

def chooseop(a, b, cmd):
    if cmd == 0:
        return a+b
    elif cmd == 1:
        return a-b

def calc(nums, ops):
    ans = nums[0]
    for i in range(1, 4):
        ans = chooseop(ans, nums[i], ops[i-1])
    return ans

def printresult(n, ops):
    op = ["+", "-", "*", "/"]
    write(n[0] + op[ops[0]] + n[1] + op[ops[1]] + n[2] + op[ops[2]] + n[3] + "=7\n")

n = input()
nums = []
if len(n) != 4:
    write("error\n")
    sys.exit()
for i in range(4):
    nums.append(int(n[i]))

zenbu = 2**3
for i in range(zenbu):
    ops = []
    bit = i
    for j in range(3):
        ops.append(bit % 2)
        bit //= 2
    res = calc(nums, ops)
    if res == 7:
        printresult(n, ops)
        break