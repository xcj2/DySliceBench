class BIT:

    def __init__(self, x):
        """
        Args:
            x (list)
        """
        len_array = len(x)
        self.tree = [0] * (len_array + 1)
        
        # update BIT
        for i, _x in enumerate(x, 1):
            while i <= len_array:
                self.tree[i] += _x
                i += i&-i

    def __call__(self, i, j):
        """
        return the sum from i to j including i and j.
        """
        ret = self.cumsum(j) - self.cumsum(i-1)
        return ret

    def cumsum(self, i):
        """
        cumulative sum from 1 to i.
        """
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i&-i
        return ret


def main():
    # count first
    # calc the combinations
    # create three BIT and count the num
    # if S[0] == 'R', S[1] == 'G', then I have to count the number of 'B' in S[3:].
    # O(4000 * 4000 * log4000) = O(10^8). it's gonna be a realistic choice.
    N = int(input())
    S = input()

    BIT_R = [0] * N
    BIT_G = [0] * N
    BIT_B = [0] * N
    for i, s in enumerate(S):
        if s == 'R':
            BIT_R[i] = 1
        elif s == 'G':
            BIT_G[i] = 1
        else:
            BIT_B[i] = 1
    BIT_R = BIT(BIT_R)
    BIT_G = BIT(BIT_G)
    BIT_B = BIT(BIT_B)

    count = 0
    for i in range(N):
        first = S[i]
        for j in range(i+1, N):
            second = S[j]
            if first == second:
                continue
            else:
                exclude_i = 2 * j - i
                if {first, second} == {'R', 'G'}:
                    _count = BIT_B(j+1, N)
                    if (exclude_i < N 
                        and S[exclude_i] == 'B'):
                        _count -= 1
                    
                elif {first, second} == {'R', 'B'}:
                    _count = BIT_G(j+1, N)
                    if (exclude_i < N 
                        and S[exclude_i] == 'G'):
                        _count -= 1

                else:
                    _count = BIT_R(j+1, N)
                    if (exclude_i < N 
                        and S[exclude_i] == 'R'):
                        _count -= 1
                
                count += _count

    print(count)


if __name__=='__main__':
    main()