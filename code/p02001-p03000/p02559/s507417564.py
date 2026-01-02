#region bcf
# code section by Barry Fam
#
# pylint: disable= reimported
#region rangedata.py
#region hyperlist.py
import itertools

# def hyperlist(*dim, default_factory=None):
def hyperlist(*dim, **kwarg):
    default_factory = kwarg.pop("default_factory", None)

    ranges = [range(n) for n in dim]

    h = [None]*dim[0]
    for dd in range(1, len(dim)):
        for u in itertools.product(*ranges[:dd]):
            hyperlist_setitem(h, u, [None]*dim[dd])

    if default_factory:
        for u in itertools.product(*ranges):
            hyperlist_setitem(h, u, default_factory())

    return h

def hyperlist_setitem(h, u, a):
    ptr = h
    for i in u[:-1]: ptr = ptr[i]
    ptr[u[-1]] = a

def hyperlist_getitem(h, u):
    ptr = h
    for i in u: ptr = ptr[i]
    return ptr

#endregion hyperlist.py
###############################################################################
import operator
import collections
import itertools
import functools
import math as m
try: m.prod
except AttributeError:
    def _prod(iterable, start=1):
        for x in iterable: start *= x
        return start
    m.prod = _prod


# class RangeOperators:
class RangeOperators(object):  # pylint: disable= useless-object-inheritance
    '''
    Data class to define the behavior of a range data structure

    new() := factory for zero values, e.g. int()

    query(a, b) := the binary query function of the tree. e.g. operator.add() for a cumulative sum
    q_inverse(a, b) := the inverse of the query function, if it exists. required for a Fenwick tree

    update(t, x) := define how the tree will be updated: return the new value of t if updated with x
    u_distributive(t, x, w) := return the new value of t if its w leaves are updated by x. required for lazy propagation
    u_commutative: bool := True if the update operation is commutative. e.g. add() is; but "set to" is not
    '''

    __slots__ = [
        "new",
        "query",
        "q_inverse",
        "update",
        "u_distributive",
        "u_commutative",
    ]

    _defaults = dict(
        new= int,
        query= operator.add,
        q_inverse= operator.sub,
        update= operator.add,
        u_distributive= lambda t, x, w: t + x*w,
        u_commutative= True,
    )

    def __init__(self, **kwarg):
        d = kwarg or self._defaults
        for k, v in d.items():
            setattr(self, k, v)

MAXQUERY = RangeOperators(
    new= int,
    query= max,
    q_inverse= None,
    update= operator.add,
    u_distributive= lambda t, x, w: t + x,
    u_commutative= True,
)

MINQUERY = RangeOperators(
    new= int,
    query= min,
    q_inverse= None,
    update= operator.add,
    u_distributive= lambda t, x, w: t + x,
    u_commutative= True,
)

SETUPDATE = RangeOperators(
    new= int,
    query= operator.add,
    q_inverse= operator.sub,
    update= lambda t, x: x,
    u_distributive= lambda t, x, w: x*w,
    u_commutative= False,
)


# class SegmentTree:
class SegmentTree(object):  # pylint: disable= useless-object-inheritance
    """
    SegmentTree(n: int) -> new tree of size n
    SegmentTree(iterable) -> new tree, initialized

    Methods:

    update_point(i, value)
    update_range(start, stop, value)
    update_consecutive_points(start, stop, iterable)

    query_point(i)
    query_range(start, stop)
    """

    def __init__(self, arg, sparse=False, ops=RangeOperators(), **kwarg):
        # super().__init__(**kwarg)
        super(SegmentTree, self).__init__(**kwarg)

        try:
            init = list(arg)
            dim = len(init)
        except TypeError:
            init = None
            dim = arg

        self.dim = dim
        self.ops = ops

        self._lazy = self.ops.u_distributive is not None
        self._clean = True

        if sparse:
            self._tree = collections.defaultdict(ops.new)

            @functools.lru_cache(maxsize=dim)
            def seglen(u):
                if u >= self.dim: return 1
                return seglen(u<<1) + seglen(u<<1|1)

            self._seglen = seglen

            if self._lazy:
                self._pending = collections.defaultdict(lambda: None)

        else:
            self._tree = [ops.new() for _ in range(dim*2)]

            seglen_precomp = [1]*dim*2
            for u in reversed(range(1, dim)):
                seglen_precomp[u] = seglen_precomp[u<<1] + seglen_precomp[u<<1|1]

            self._seglen = seglen_precomp.__getitem__

            if self._lazy:
                self._pending = [None]*dim

        if init:
            self.update_consecutive_points(0, dim, init)


    # Iterators

    def _downward_path(self, i):
        """Iterate over tree indexes from root to just above raw index i"""
        u = self.dim + i
        for s in range(u.bit_length()-1, 0, -1):
            yield u >> s

    def _upward_path(self, i):
        """Iterate over tree indexes from just above raw index i to root"""
        u = self.dim + i
        while u > 1:
            u >>= 1
            yield u

    def _downward_fill(self, i, j):
        """Iterate over every tree index that is an ancestor of raw index range [i,j), from root downwards"""
        n = self.dim
        l = n+i
        r = n+j-1
        for s in range(l.bit_length()-1, 0, -1):
            for u in range(l>>s, (r>>s)+1):
                yield u

    def _upward_fill(self, i, j):
        """Iterate over every tree index that is an ancestor of raw index range [i,j), from just above leaves upwards"""
        n = self.dim
        l = n+i
        r = n+j-1
        while l > 1:
            l >>= 1
            r >>= 1
            for u in reversed(range(l, r+1)):
                yield u

    def _cover_nodes(self, i, j):
        """Iterate over the set of tree indexes whose segments optimally cover raw index range [i,j)"""
        n = self.dim
        l = n+i
        r = n+j
        while l < r:
            if l&1:
                yield l
                l += 1
            if r&1:
                r -= 1
                yield r
            l >>= 1
            r >>= 1


    # Node modification

    def _lazy_update(self, u, value):
        """Update tree index u as if its child leaves had been updated with value"""
        self._tree[u] = self.ops.u_distributive(self._tree[u], value, self._seglen(u))
        if u < self.dim:
            self._clean = False
            if self._pending[u] is None:
                self._pending[u] = value
            else:
                self._pending[u] = self.ops.update(self._pending[u], value)

    def _push1(self, u):
        """Apply any pending lazy update at tree index u to its two immediate children"""
        assert u < self.dim
        if self._clean: return

        value = self._pending[u]
        if value is not None:
            for v in (u<<1, u<<1|1):
                self._lazy_update(v, value)

            self._pending[u] = None

    def _build1(self, u):
        """Calculate the query function at tree index u from its two immediate children"""
        assert u < self.dim
        self._push1(u)
        self._tree[u] = self.ops.query(self._tree[u<<1], self._tree[u<<1|1])


    # Node-set modification

    def _push_path(self, i):
        """Push lazy updates from root to raw index i"""
        if self._clean: return
        for u in self._downward_path(i):
            self._push1(u)

    def _push_fill(self, i, j):
        """Push lazy updates from root to raw index range [i,j)"""
        if self._clean: return
        for u in self._downward_fill(i, j):
            self._push1(u)

        if j-i == self.dim: self._clean = True

    def _build_path(self, i):
        """Update tree nodes from raw index i to root"""
        for u in self._upward_path(i):
            self._build1(u)

    def _build_fill(self, i, j):
        """Update all tree ancestors of raw index range [i,j)"""
        for u in self._upward_fill(i, j):
            self._build1(u)

        if j-i == self.dim: self._clean = True


    # Interface

    def update_consecutive_points(self, start, stop, iterable):
        assert 0 <= start < stop <= self.dim

        # push if necessary
        if not self.ops.u_commutative:
            self._push_fill(start, stop-1)

        # write leaves
        for u, value in zip(range(self.dim + start, self.dim + stop), iterable):
            self._tree[u] = self.ops.update(self._tree[u], value)

        # build
        self._build_fill(start, stop-1)

    def query_range(self, start, stop):
        assert start < stop

        for i in {start, stop-1}:
            self._push_path(i)

        node_values = (self._tree[u] for u in self._cover_nodes(start, stop))
        return functools.reduce(self.ops.query, node_values)

    def update_range(self, start, stop, value):
        assert start < stop

        # if no lazy propagation, fall back to writing to leaves
        if not self._lazy:
            self.update_consecutive_points(start, stop, itertools.repeat(value))
            return

        # push if necessary
        if not self.ops.u_commutative:
            for i in {start, stop-1}:
                self._push_path(i)

        # write cover nodes
        for u in self._cover_nodes(start, stop):
            self._lazy_update(u, value)

        # build
        for i in {start, stop-1}:
            self._build_path(i)

    def query_point(self, i):
        return self.query_range(i, i+1)

    def update_point(self, i, value):
        self.update_range(i, i+1, value)


# class FenwickTree:
class FenwickTree(object):  # pylint: disable= useless-object-inheritance
    """
    ft1d = FenwickTree(dim)
    ft3d = FenwickTree(dim1, dim2, dim3)
    etc.

    Methods:

    ft1d.iadd(i, update_value)
    ft3d.iadd((i,j,k), update_value)

    ft1d[i] = set_value
    fr3d[i,j,k] = set_value

    query = ft1d[i1:i2]
    query = ft3d[i1:i2, j1:j2, k1:k2]
    """

    # def __init__(self, *dim, sparse=False, **kwarg):
    def __init__(self, *dim, **kwarg):
        sparse = kwarg.pop("sparse", False)

        # super().__init__(**kwarg)
        super(FenwickTree, self).__init__(**kwarg)

        self.dim = dim
        self.d = len(dim)

        if sparse:
            self._tree = collections.defaultdict(int)
            if self.d > 1:
                self._tree_setitem = self._tree.__setitem__
                self._tree_getitem = self._tree.__getitem__
        else:
            self._tree = hyperlist(*dim, default_factory=int)
            if self.d > 1:
                self._tree_setitem = functools.partial(hyperlist_setitem, self._tree)
                self._tree_getitem = functools.partial(hyperlist_getitem, self._tree)

        if self.d == 1:
            self.iadd = self._iadd_1d
            self._getitem = self._getitem_1d
        else:
            self.iadd = self._iadd_dd
            self._getitem = self._getitem_dd

    def __setitem__(self, key, value):
        self.iadd(key, value-self[key])

    def __getitem__(self, key):
        return self._getitem(key)

    @staticmethod
    def _set_index_iter(i, n):
        """Iterate over the tree indices < n which are affected when setting raw index i"""
        if i == 0:
            yield 0
            return

        while True:
            yield i
            i += i & -i  # increment LSB
            if i >= n: return

    @staticmethod
    def _get_index_iter(i, j):
        """
        Iterate over the tree indices whose sum equals the sum over the raw range (j,i] -- note that i > j
        Each index is returned as (index, sign) where sign is +1 or -1 for inclusion-exclusion
        """
        if i < 0: return
        if j < 0:
            yield 0, +1
            j = 0

        while i > j:
            yield i, +1
            i &= i-1  # decrement LSB
        while j > i:
            yield j, -1
            j &= j-1  # decrement LSB

    def _iadd_1d(self, key, value):
        assert 0 <= key < self.dim[0]

        for i in self._set_index_iter(key, self.dim[0]):
            self._tree[i] += value

    def _iadd_dd(self, key, value):
        assert len(key) == self.d
        assert all(0 <= i < self.dim[dd] for dd, i in enumerate(key)), "index out of range"

        index_iters = [self._set_index_iter(i, self.dim[dd]) for dd, i in enumerate(key)]
        for u in itertools.product(*index_iters):
            g = self._tree_getitem(u)
            self._tree_setitem(u, g+value)

    def _getitem_1d(self, key):
        if isinstance(key, slice):
            assert key.step is None
            start, stop, _ = key.indices(self.dim[0])
            if stop < start: stop = start
            i, j = stop-1, start-1
        else:
            i, j = key, key-1

        assert -1 <= j <= i < self.dim[0], "index out of range"

        sigma = 0
        for k, sign in self._get_index_iter(i, j):
            sigma += sign * self._tree[k]

        return sigma

    def _getitem_dd(self, key):
        index_iters = []
        for dd, k in enumerate(key):
            if isinstance(k, slice):
                assert k.step is None
                start, stop, _ = k.indices(self.dim[dd])
                if stop < start: stop = start
                itr = self._get_index_iter(stop-1, start-1)
            else:
                assert 0 <= k < self.dim[dd], "index out of range"
                itr = self._get_index_iter(k, k-1)

            index_iters.append(itr)

        assert len(index_iters) == self.d, "mismatched key dimensions"

        sigma = 0
        for i_sign_pairs in itertools.product(*index_iters):
            u, signs = zip(*i_sign_pairs)
            sign = m.prod(signs)

            sigma += sign * self._tree_getitem(u)

        return sigma

#endregion rangedata.py
#endregion bcf
###############################################################################

import sys
def input(itr=iter(sys.stdin.readlines())):  # pylint: disable= redefined-builtin
    return next(itr).rstrip('\n\r')
###############################################################################

N, Q = map(int, input().split())
a = list(map(int, input().split()))

ft = FenwickTree(N)
for i, x in enumerate(a):
    ft[i] = x

responses = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        (_, p, x) = q
        ft.iadd(p, x)
    else:
        (_, l, r) = q
        responses.append(ft[l:r])

print(*responses, sep='\n')
