def main():
    N = int(input())
    S = input()

    def make(S0, S1) -> str:
        rec = S0+S1
        for i in range(1, N-1):
            if S[i] == "o" and rec[i] == "S":
                rec = rec + rec[i-1]
            elif S[i] == "o" and rec[i] == "W":
                if rec[i-1] == "S":
                    rec = rec + "W"
                else:
                    rec = rec + "S"
            elif S[i] == "x" and rec[i] == "S":
                if rec[i-1] == "S":
                    rec = rec + "W"
                else:
                    rec = rec + "S"
            elif S[i] == "x" and rec[i] == "W":
                rec = rec + rec[i-1]

        return rec

    def checker(rec) -> bool:
        for i in range(N-1):
            if S[i] == "o" and rec[i] == "S":
                if rec[i-1] != rec[i+1]:
                    return False
            elif S[i] == "o" and rec[i] == "W":
                if rec[i-1] == rec[i+1]:
                    return False
            elif S[i] == "x" and rec[i] == "S":
                if rec[i-1] == rec[i+1]:
                    return False
            elif S[i] == "x" and rec[i] == "W":
                if rec[i-1] != rec[i+1]:
                    return False
        if S[N-1] == "o" and rec[N-1] == "S":
            return rec[N-2] == rec[0]
        elif S[N-1] == "o" and rec[N-1] == "W":
            return rec[N-2] != rec[0]
        elif S[N-1] == "x" and rec[N-1] == "S":
            return rec[N-2] != rec[0]
        elif S[N-1] == "x" and rec[N-1] == "W":
            return rec[N-2] == rec[0]

    for S0, S1 in (("S", "S"), ("S", "W"), ("W", "S"), ("W", "W")):
        rec = make(S0, S1)
        if checker(rec):
            print(rec)
            break
    else:
        print(-1)


if __name__ == '__main__':
    main()
