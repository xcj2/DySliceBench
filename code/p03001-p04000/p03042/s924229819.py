def isMM(date):

    n_date= int(date)

    if 1 <= n_date <= 12:
        return True
    else:
        return False

def isYY(date):

    n_date = int(date)

    if 0 <= n_date <= 99:
        return True
    else:
        return False

def isYYMM(date):

    if isYY(date[0:2]) and isMM(date[2:4]):
        return True
    else:
        return False

def isMMYY(date):

    if isMM(date[0:2]) and isYY(date[2:4]):
        return True
    else:
        return False

def main(): 

    S = input()

    if isYYMM(S) and isMMYY(S):
        print('AMBIGUOUS')
    elif isYYMM(S):
        print('YYMM')
    elif isMMYY(S):
        print('MMYY')
    else:
        print('NA')

if __name__ == "__main__":
    main() 