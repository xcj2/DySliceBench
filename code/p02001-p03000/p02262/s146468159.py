def insetion_sort(A, n, g, cnt) :
        cnt = 0
        for i in range(g, n) :
            v = A[i]
            j = i - g
            while j >= 0 and A[j] > v :
                A[j+g] = A[j]
                j = j -g
                cnt += 1
            A[j+g] = v
        return cnt


def shell_sort(A, n) :
        cnt = 0
        count = 0
        G_sub = []
        h = 1
        while h <= n :
                G_sub.append(h)
                h = 3 * h + 1
        m = len(G_sub)
        G = G_sub[::-1]

        for i in range(m) :
                count += insetion_sort(A, n, G[i], cnt)

        print(m)
        if len(G) == 1 :
                print(G[0])
        else :
                print(" ".join(map(str, G)))
        print(count)


def main() :
        n = int(input())
        nums = []
        for i in range(n) :
                nums.append(int(input()))

        shell_sort(nums, n)
        for i in range(n) :
                print(nums[i])

if __name__ == '__main__' :
        main()