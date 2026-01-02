def pad(b,N):
    b = "0"*(N-len(b)) + b
    return b

def cal(A):
    N = len(A)
    for i in range(2**(N-1)):
        b = list(pad(bin(i)[2:],N-1))
        for j in range(N-1):
            if b[j] == "1":
                b[j] = "+"
            else:
                b[j] = "-"
        s = A[0]
        for j in range(N-1):
            if b[j] == "+":
                s += A[j+1]
            else:
                s -= A[j+1]
        if s == 7:
            output = str(A[0])
            for j in range(N-1):
                output += b[j]
                output += str(A[j+1])
            output += "=7"
            return output

def main():
    A = list(map(int,input()))
    print(cal(A))

if __name__ == "__main__":
    main()
