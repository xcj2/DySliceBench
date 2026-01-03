def indexIsValid(S, ni):
    for i in range(len(S)):
        if ni[i] >= len(S[i]):
            return False

    return True

def goToNextCharacterIndex(S, ni, current_c):
    for i in range(len(S)):
        while S[i][ni[i]] == current_c:
            ni[i] += 1

            # end of search
            if ni[i] >= len(S[i]):
                return False

    return True

def allSameCharacter(S, ni):
    result = True
    for i in range(len(S) - 1):
        result = result and (S[i][ni[i]] == S[i+1][ni[i+1]])

    return result


if __name__ == "__main__":
    n = int(input())
    S = [input() for i in range(n)]

    # list of sorted characters list (2D array)
    S_sorted = [sorted(list(S[i])) for i in range(n)]

    # character index for S[i]
    ni = [0 for i in range(n)]

    result = ""
    continue_search = True
    for c in "abcdefghijklmnopqrstuvwxyz":
        if not continue_search:
            break
        
        while allSameCharacter(S_sorted, ni):
            result += S_sorted[0][ni[0]]
            ni = list(map(lambda x : x + 1, ni))

            if not indexIsValid(S_sorted, ni):
                continue_search = False
                break

        if not continue_search:
            break
            
        continue_search = goToNextCharacterIndex(S_sorted, ni, c)

    print(result)
