class DisjointSparseTable:
    def __init__(self, a, op=lambda a, b: max(a, b), e=0):
        # Operator
        self.op = op
        # Identity element
        self.e = e
        self.n = len(a)
        self.level = (self.n - 1).bit_length()
        self.size = 2 ** self.level
        self.table = [[self.e] * self.size for _ in range(self.level)]
        # Set bottom first
        for i, item in enumerate(a):
            self.table[-1][i] = item
        self.build()

    def build(self):
        for i in range(1, self.level):
            step = 2 ** i
            lv = self.level - 1 - i
            for mid in range(step, self.n + step, step * 2):
                # Forward
                val = self.e
                for j in range(step):
                    val = self.op(val, self.table[-1][mid + j])
                    self.table[lv][mid + j] = val
                # Backward
                val = self.e
                for j in range(step):
                    val = self.op(self.table[-1][mid - 1 - j], val)
                    self.table[lv][mid - 1 - j] = val

    # Returns f[l:r)
    def fold(self, l, r):
        if l == r:
            return self.e
        elif l == r - 1:
            return self.table[-1][l]
        lv = self.level - (l ^ r - 1).bit_length()
        return self.op(self.table[lv][l], self.table[lv][r - 1])


class SuffixArray:
    def __init__(self, S):
        ord_base = ord("a") - 1
        a = [ord(ch) - ord_base for ch in S]
        self.a = a + [0]
        self.k = max(self.a) + 1
        self.n = len(self.a)
        self.sa = self.SA_IS(self.a, self.n, self.k)
        # Construct LCP disjoint sparse table
        self.rank = [0] * self.n
        for i, item in enumerate(self.sa):
            self.rank[item] = i
        self.lcp = self.build_LCP(self.a, self.sa, self.rank)
        self.lcp_dst = DisjointSparseTable(self.lcp, op=lambda a, b: min(a, b), e=10 ** 9)

    # Find the start or end of each bucket
    def get_buckets(self, a, k, end=True):
        bucket = [0] * k
        for item in a:
            bucket[item] += 1
        sumation = 0
        for i in range(k):
            sumation += bucket[i]
            if end:
                bucket[i] = sumation
            else:
                bucket[i] = sumation - bucket[i]
        return bucket

    def induce_SAl(self, a, sa, n, k, lstype):
        bucket = self.get_buckets(a, k, end=False)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not lstype & (1 << j + 1)):
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_SAs(self, a, sa, n, k, lstype):
        bucket = self.get_buckets(a, k, end=True)
        for i in range(n - 1, -1, -1):
            j = sa[i] - 1
            if j >= 0 and lstype & (1 << j + 1):
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j

    def is_LMS(self, index, lstype):
        return lstype >> (index + 1) & 1 and not (lstype >> index & 1)

    def is_stype(self, index, lstype):
        return lstype >> (index + 1) & 1

    def SA_IS(self, a, n, k):
        # L-type or S-type
        # LS-type array in bits, 1-indexed, initialized with S-type first
        lstype = 1
        prev_type = 0
        prev_item = self.k
        for i, item in enumerate(a[::-1]):
            shift = n - i
            if item == prev_item:
                lstype |= prev_type << shift
            elif item < prev_item:
                lstype |= 1 << shift
                prev_type = 1
            else:
                prev_type = 0
            prev_item = item
        # Bucket array
        bucket = self.get_buckets(a, k)
        # Find ends of buckets
        sa = [-1] * n
        for i in range(n - 1, 0, -1):
            if self.is_LMS(i, lstype):
                bucket[a[i]] -= 1
                sa[bucket[a[i]]] = i
        self.induce_SAl(a, sa, n, k, lstype)
        self.induce_SAs(a, sa, n, k, lstype)

        lcm_cnt = 0
        for i in range(n):
            if self.is_LMS(sa[i], lstype):
                sa[lcm_cnt] = sa[i]
                lcm_cnt += 1
        for i in range(lcm_cnt, n):
            sa[i] = -1

        # Rename LCM strings
        name = 1;
        prev = sa[0]
        sa[lcm_cnt + sa[0] // 2] = 0
        for pos in sa[1: lcm_cnt]:
            diff = False
            for d in range(n):
                if a[pos + d] != a[prev + d] or (self.is_stype(pos + d, lstype) != self.is_stype(prev + d, lstype)):
                    diff = True
                    break
                elif d > 0 and (self.is_LMS(pos + d, lstype) or self.is_LMS(prev + d, lstype)):
                    break
            if diff:
                name += 1;
                prev = pos
            pos //= 2
            sa[lcm_cnt + pos] = name - 1
        sub_a = []
        for i in range(lcm_cnt, n):
            if sa[i] >= 0:
                sub_a.append(sa[i])

        # Recursively sort LMS sub strings
        if name < lcm_cnt:
            sub_sa = self.SA_IS(sub_a, len(sub_a), name + 1)
        else:
            sub_sa = sa[:lcm_cnt]
            for i in range(lcm_cnt):
                sub_sa[sub_a[i]] = i
        bucket = self.get_buckets(a, k, end=True)
        j = 0
        for i in range(1, n):
            if self.is_LMS(i, lstype):
                sub_a[j] = i
                j += 1
        # Earn correctly sorted LCMs
        for i in range(lcm_cnt):
            sa[i] = sub_a[sub_sa[i]]
        for i in range(lcm_cnt, n):
            sa[i] = -1
        for i in range(lcm_cnt - 1, -1, -1):
            j = sa[i];
            sa[i] = -1
            bucket[a[j]] -= 1
            sa[bucket[a[j]]] = j

        # Correct induced sorting
        self.induce_SAl(a, sa, n, k, lstype)
        self.induce_SAs(a, sa, n, k, lstype)
        return sa

    def build_LCP(self, a, sa, rank):
        # Add sentinel
        sa.append(-1)
        lcp = [0] * len(a)
        same_cnt = 0
        for index1 in range(len(a)):
            if same_cnt != 0:
                same_cnt -= 1
            index2 = sa[rank[index1] + 1]
            while a[index1 + same_cnt] == a[index2 + same_cnt]:
                same_cnt += 1
            lcp[rank[index1]] = same_cnt
        # Remove sentinel
        sa.pop()
        return lcp

    def get_lcp(self, l, r):
        rank_l = self.rank[l]
        rank_r = self.rank[r]
        if rank_l > rank_r:
            rank_l, rank_r = rank_r, rank_l
        return self.lcp_dst.fold(rank_l, rank_r)

    def search(self, b):
        m = len(b)
        l = 0;
        r = self.n + 1
        matched = 0
        while r - l > 1:
            mid = (l + r) // 2
            lm_lcp = self.get_lcp(l, mid)
            if matched < lm_lcp:
                l = mid
            elif matched > lm_lcp:
                r = mid
            else:
                a_itr = self.sa[mid] + matched;
                b_itr = matched
                diff = 0
                while b_itr < m and a_itr < self.n:
                    if b[b_itr] != self.a[a_itr]:
                        diff = b[b_itr] - self.a[a_itr]
                        break
                    a_itr += 1;
                    b_itr += 1
                if diff >= 0:
                    l = mid
                    matched = b_itr
                else:
                    r = mid
        return matched, l

def max2(x,y):
    return x if x > y else y

def min2(x,y):
    return x if x < y else y

res = 0
N = int(input())
S = input()
SA = SuffixArray(S)
for i in range(N + 1):
    for j in range(i + 1, N + 1):
        lcp = SA.get_lcp(i, j)
        temp = min2(lcp, j-i)
        res = max2(res, temp)
print(res)
