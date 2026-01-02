#region bcf
# code section by Barry Fam
#
# pylint: disable= reimported
#region graph.py
#region heap.py
#region linkedlist.py
class LinkedListNodeBase:
    """A node; connected to others to form a doubly linked list

    The complete list should have head & tail sentinels, or be circular
    """
    __slots__ = [
        "prev",
        "next",
    ]

    def __init__(self):
        self.prev = None
        self.next = None

    def connect(self, node):
        self.next = node
        node.prev = self

    def splice(self, fragment):
        """Insert a fragment of 1 or more nodes between this and next node"""
        assert self.next, "splice onto unconnected node"

        # handle circular fragment
        if fragment.prev: fragment.prev.next = None

        u = self
        v = fragment
        w = self.next

        u.connect(v)
        while v.next: v = v.next
        v.connect(w)

    def splice1(self, node):
        """Insert a single node between this and next node"""
        assert self.next, "splice onto unconnected node"

        node.connect(self.next)
        self.connect(node)

    def eject(self):
        """Remove this node from its list by connecting its left and right nodes

        Note: This node's own next & prev pointers are NOT erased"""
        assert self.prev and self.next, "cannot eject unconnected node"

        self.prev.connect(self.next)

    def iterate(self):
        """Iterate through linked nodes, starting from self"""
        visited = set()
        u = self
        while u and u not in visited:
            yield u
            visited.add(u)
            u = u.next

class LinkedListNode(LinkedListNodeBase):
    __slots__ = ["__dict__"]

#endregion linkedlist.py
###############################################################################
import abc
import functools
import itertools
import math as m

# class AbstractHeap(abc.ABC):
class AbstractHeap:  # pylint: disable= metaclass-assignment
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, iterable=(), history=False, **kwarg):
        """
        Initialize self from an optional iterable of (key, value) pairs

        If history is True, maintain a record of popped values in .history
        """

        super().__init__(**kwarg)

        if history:
            self.history = set()

            def wrap_pop():
                wrapped = self.pop

                @functools.wraps(wrapped)
                def wrapper():
                    key, value = wrapped()
                    self.history.add(value)
                    return key, value

                self.pop = wrapper

            wrap_pop()
        else:
            self.history = []

    def add(self, key, value):
        """Add an item to the heap

        This convenience method automatically selects push() or decrease_key() as appropriate, and filters against the heap history if present. Returns True if the item was added, False if not
        """
        if value in self.history:
            return False
        elif value not in self:
            self.push(key, value)
            return True
        elif key < self[value]:
            self.decrease_key(value, key)
            return True
        else:
            return False

    @abc.abstractmethod
    def __bool__(self): pass

    @abc.abstractmethod
    def __len__(self): pass

    @abc.abstractmethod
    def __contains__(self, value): pass

    @abc.abstractmethod
    def __getitem__(self, value): pass

    @abc.abstractmethod
    def push(self, key, value): pass

    @abc.abstractmethod
    def pop(self): pass

    @abc.abstractmethod
    def decrease_key(self, value, key): pass

    @abc.abstractmethod
    def merge(self, other): pass


class _FibHeapNode(LinkedListNodeBase):
    __slots__ = [
        "key",
        "value",
        "parent",
        "child",
        "degree",
        "mark",
    ]

    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        self.parent = None
        self.child = None
        self.degree = 0
        self.mark = False

class FibonacciHeap(AbstractHeap):
    def __init__(self, iterable=(), **kwarg):
        super().__init__(**kwarg)
        self._n = 0
        self._root = None
        self._index = {}

        for k, v in iterable: self.push(k, v)

    def __bool__(self):
        return bool(self._n)

    def __len__(self):
        return self._n

    def __contains__(self, value):
        return value in self._index

    def __getitem__(self, value):
        return self._index[value].key

    def __str__(self):
        def chain_str(c):
            ls = []
            for x in c.iterate():
                s = str(x.key)
                if x.child: s += " ({})".format(chain_str(x.child))
                ls.append(s)
            return ", ".join(ls)

        return "[{}]".format(chain_str(self._root) if self else '')

    def push(self, key, value):
        assert value not in self._index

        node = _FibHeapNode(key, value)
        self._index[value] = node

        if self._root is None:
            node.connect(node)
            self._root = node
            self._n = 1
        else:
            self._root.splice1(node)
            if key < self._root.key: self._root = node
            self._n += 1

    def pop(self):
        assert self._n > 0

        z = self._root

        if z.child:
            for c in z.child.iterate(): c.parent = None
            z.splice(z.child)

        if z.next == z:
            self._root = None
        else:
            self._root = z.next
            z.eject()
            self._consolidate()

        self._n -= 1
        del self._index[z.value]
        return z.key, z.value

    def _consolidate(self):
        assert self._n > 0

        A = {}
        for x in list(self._root.iterate()):
            d = x.degree
            while d in A:
                y = A[d]
                if x.key > y.key: x, y = y, x
                self._link(y, x)
                del A[d]
                d += 1
            A[d] = x

        i = iter(A.values())
        self._root = next(i)
        self._root.connect(self._root)
        for x in i:
            self._root.splice1(x)
            if x.key < self._root.key: self._root = x

    @staticmethod
    def _link(y, x):
        assert y.degree == x.degree

        y.eject()
        y.parent = x
        if x.child:
            x.child.splice1(y)
        else:
            x.child = y
            y.connect(y)
        x.degree += 1
        y.mark = False

    def decrease_key(self, value, key):
        x = self._index[value]
        assert key < x.key

        x.key = key
        del self._index[value]
        self._index[value] = x

        y = x.parent
        if y and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)

        if x.key < self._root.key: self._root = x

    def _cut(self, x, y):
        if x.next == x:
            y.child = None
        else:
            y.child = x.next
        x.parent = None
        x.eject()
        y.degree -= 1

        self._root.splice1(x)
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def merge(self, other):
        assert isinstance(other, FibonacciHeap)
        if not other: return

        if self:
            self._root.splice(other._root)
            if other._root.key < self._root.key: self._root = other._root
            self._index.update(other._index)
            assert len(self._index) == self._n + other._n, "merge error: duplicate values"
        else:
            self._root = other._root
            self._index = other._index

        self._n += other._n
        other._root = None
        other._n = 0
        other._index = {}


class _PairingHeapNode:
    __slots__ = [
        "key",
        "value",
        "parent",
        "left",
        "right",
    ]

    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def link(self, other):
        if other.key < self.key: self, other = other, self
        if not self.left:
            self.left = other
            other.parent = self
        else:
            r = self.left
            while r.right: r = r.right
            r.right = other
            other.parent = r

        return self

class PairingHeap(AbstractHeap):
    def __init__(self, iterable=(), **kwarg):
        super().__init__(**kwarg)
        self._root = None
        self._index = {}

        for k, v in iterable: self.push(k, v)

    def __bool__(self):
        return self._root is not None

    def __len__(self):
        return len(self._index)

    def __contains__(self, value):
        return value in self._index

    def __getitem__(self, value):
        return self._index[value].key

    def __str__(self):
        def tree_str(t):
            i = t
            ls = []
            while i:
                ls.append(str(i.key))
                i = i.right
            s = ", ".join(ls)

            if t.left: s += " ({})".format(tree_str(t.left))
            return s

        return "[{}]".format(tree_str(self._root) if self else '')

    def push(self, key, value):
        assert value not in self._index

        node = _PairingHeapNode(key, value)
        self._index[value] = node

        if self._root is None:
            self._root = node
        else:
            self._root = self._root.link(node)

    def decrease_key(self, value, key):
        x = self._index[value]
        assert key < x.key

        x.key = key
        del self._index[value]
        self._index[value] = x
        if x.parent is None: return

        if x.parent.left == x:
            x.parent.left = x.right
        else:
            x.parent.right = x.right
        if x.right: x.right.parent = x.parent

        x.parent = x.right = None
        self._root = self._root.link(x)

    def pop(self):
        assert self._root is not None

        z = self._root
        if z.left is None:
            self._root = None
        else:
            pass0 = []
            i = z.left
            while i:
                j = i.right
                i.parent = i.right = None
                pass0.append(i)
                i = j

            pass1 = []
            for i, j in zip(pass0[:-1:2], pass0[1::2]):
                pass1.append(i.link(j))
            if len(pass0)%2 == 1: pass1.append(pass0[-1])

            y = pass1.pop()
            while pass1:
                y = y.link(pass1.pop())

            self._root = y

        del self._index[z.value]
        return z.key, z.value

    def merge(self, other):
        assert isinstance(other, PairingHeap)
        if not other: return

        if self:
            self._root = self._root.link(other._root)
            self._index.update(other._index)
        else:
            self._root = other._root
            self._index = other._index

        other._root = None
        other._index = {}


class _InfKey:
    __gt__ = __ge__ = lambda *_: True
    __lt__ = __le__ = lambda *_: False
_inf_key = _InfKey()

def _iter_skip1(iterable):
    itr = iter(iterable)
    next(itr)
    return itr

class Implicit2Heap(AbstractHeap):
    def __init__(self, iterable=(), **kwarg):
        super().__init__(**kwarg)
        self._build_heap(iterable)

    def __bool__(self):
        return len(self._tree) > 1

    def __len__(self):
        return len(self._tree)-1

    def __contains__(self, value):
        return value in self._index

    def __getitem__(self, value):
        return self._tree[self._index[value]][0]

    def __str__(self):
        ls = []
        for i, x in enumerate(_iter_skip1(self._tree), start=1):
            s = '[' if m.log2(i)%1 == 0 else ''
            s += str(x[0])
            s += ']' if m.log2(i+1)%1 == 0 else ''
            ls.append(s)

        return ', '.join(ls)

    def _build_heap(self, iterable):
        self._tree = tree = list(itertools.chain([None], iterable))
        size = len(self)

        self._index = {tree[i][1]: i for i in range(size//2+1, size+1)}
        for i in range(size//2, 0, -1):
            self._heapify(i)

        assert len(self._index) == size

    def _heapify(self, i):
        tree = self._tree
        size = len(self)
        left = i*2
        right = i*2 + 1

        if left <= size and tree[left] < tree[i]:
            z = left
        else:
            z = i
        if right <= size and tree[right] < tree[z]:
            z = right

        if z != i:
            tree[i], tree[z] = tree[z], tree[i]
            self._heapify(z)

        self._index[tree[i][1]] = i

    def decrease_key(self, value, key):
        tree = self._tree
        i = self._index[value]
        assert key < tree[i][0]

        while i > 1:
            p = i//2
            if not key < tree[p][0]: break
            tree[i] = tree[p]
            self._index[tree[i][1]] = i
            i = p

        tree[i] = (key, value)
        self._index[value] = i

    def push(self, key, value):
        assert value not in self._index

        self._index[value] = len(self._tree)
        self._tree.append((_inf_key, value))
        self.decrease_key(value, key)

    def pop(self):
        assert self

        tree = self._tree
        z = tree[1]
        tree[1] = tree[-1]
        del tree[-1]
        if self: self._heapify(1)

        del self._index[z[1]]
        return z

    def merge(self, other):
        assert isinstance(other, Implicit2Heap)
        if not other: return

        self._build_heap(itertools.chain(_iter_skip1(self._tree), _iter_skip1(other._tree)))

        other._tree = [None]
        other._index = {}

#endregion heap.py
###############################################################################
import math as m
import collections
import copy

class Graph:
    def __init__(self, maxV, isflow=False, sparse=False, **kwarg):
        super().__init__(**kwarg)

        self.maxV = maxV
        self.isflow = isflow
        self.sparse = sparse

        self._V = []
        self._V_index = {}

        non_edge = 0 if isflow else m.inf
        if sparse:
            df = lambda: non_edge
            self._E = [collections.defaultdict(df) for _ in range(maxV)]
        else:
            self._E = [[non_edge]*maxV for _ in range(maxV)]

        self._adj = [set() for _ in range(maxV)]  # if isflow, adj includes 0 weight back-edges
        self._levels = {}

    def __contains__(self, label):
        return label in self._V_index

    def __iter__(self):
        return iter(self._V)

    @property
    def nV(self):
        return len(self._V)

    @property
    def nE(self):
        n = sum(len(a) for a in self._adj)
        if self.isflow: n //= 2
        return n

    def adj(self, u_label, filter_empty_edges=True):
        if filter_empty_edges:
            if self.isflow: reject = 0
            else: reject = m.inf
        else:
            reject = None

        u = self._V_index[u_label]
        return {self._V[v]: self._E[u][v] for v in self._adj[u] if self._E[u][v] != reject}

    def add_vertex(self, label):
        assert label not in self
        assert self.nV < self.maxV

        self._V_index[label] = self.nV
        self._V.append(label)
        assert len(self._V_index) == self.nV

    def add_vertexes(self, labels):
        for u_label in labels:
            self.add_vertex(u_label)

    add_vertices = add_vertexes

    def _add_edge(self, u, v, w):
        if self.isflow:
            self._E[u][v] += w
            self._adj[u].add(v)
            self._adj[v].add(u)
        else:
            assert v not in self._adj[u]
            self._E[u][v] = w
            self._adj[u].add(v)

    def add_edge(self, u_label, v_label, w=1):
        self._add_edge(self._V_index[u_label], self._V_index[v_label], w)

    def add_edges(self, edges):
        """Add multiple edges

        edges := an iterable of (u_label, v_label, [w]) tuples
        """
        for edge in edges:
            self.add_edge(*edge)

    def copy(self, reverse=False):
        if reverse:
            h = Graph(self.maxV, isflow=self.isflow, sparse=self.sparse)
            h.add_vertexes(self._V)
            for u in range(self.nV):
                for v in self._adj[u]:
                    h.add_edge(self._V[v], self._V[u], self._E[u][v])

            return h
        else:
            return copy.deepcopy(self)

    def trim(self, u_label):
        """Remove all outgoing edges from u_label"""
        assert not self.isflow

        u = self._V_index[u_label]

        self._adj[u] = set()
        if self.sparse:
            self._E[u].clear()
        else:
            self._E[u] = [m.inf]*self.maxV

    def _bfs_levels(self, s, t):
        self._levels[s] = [m.inf]*self.maxV
        self._levels[s][s] = 0

        queue = collections.deque([s])
        while queue:
            u = queue.popleft()
            for v in self._adj[u]:
                if self._E[u][v] > 0 and self._levels[s][v] == m.inf:
                    self._levels[s][v] = self._levels[s][u]+1
                    queue.append(v)

        return self._levels[s][t]

    def _push_blocking_flow(self, s, t):
        assert s in self._levels

        pointers = [self._adj[i].copy() for i in range(self.nV)]

        def dfs_push(u, t, inflow):
            if u == t: return inflow
            u_outflow = 0
            while pointers[u]:
                v = pointers[u].pop()
                if self._levels[s][v] == self._levels[s][u]+1 and self._E[u][v] > 0:
                    v_flow = dfs_push(v, t, min(inflow, self._E[u][v]))
                    self._E[u][v] -= v_flow
                    self._E[v][u] += v_flow
                    inflow -= v_flow
                    u_outflow += v_flow
                    if inflow == 0:
                        pointers[u].add(v)
                        break

            return u_outflow

        blocking_flow = dfs_push(s, t, m.inf)
        self._levels = {}
        return blocking_flow

    def max_flow(self, s_label, t_label, total_only=True, preserve=False):
        """Dinitz (Dinic) maximum flow

        If total_only is True, return the quantity of the maximum flow
        Otherwise, return a Graph-like object containing a maximal flow, with an additional attribute:
        .total_flow := the quantity of the maximum flow

        If preserve is True, restore the graph to its original state after the calculation
        Otherwise, the graph will contain the residual flow
        """
        assert self.isflow

        if preserve or not total_only: E_orig = copy.deepcopy(self._E)
        s = self._V_index[s_label]
        t = self._V_index[t_label]

        mf = 0
        while self._bfs_levels(s, t) != m.inf:
            mf += self._push_blocking_flow(s, t)

        if total_only:
            ret = mf
        else:
            class MaxFlowObject(Graph):
                __slots__ = ["total_flow"]
            ret = MaxFlowObject(self.nV, isflow=True, sparse=self.sparse)
            ret.total_flow = mf  # pylint: disable= attribute-defined-outside-init
            ret.add_vertexes(self._V)
            for u in range(self.nV):
                for v in self._adj[u]:
                    uv_flow = E_orig[u][v] - self._E[u][v]
                    if uv_flow > 0:
                        ret.add_edge(self._V[u], self._V[v], uv_flow)

        if preserve: self._E = E_orig
        return ret

    def all_pairs_spaths(self):
        """Floyd-Warshall"""
        assert not self.isflow

        fw = self._E
        for k in range(self.nV):
            next_fw = []
            for i in range(self.nV):
                next_fw.append([])
                for j in range(self.nV):
                    next_fw[i].append(min(fw[i][j], fw[i][k]+fw[k][j]))

            fw = next_fw

        fw_labeled = {self._V[u]: {self._V[v]: fw[u][v] for v in range(self.nV)} for u in range(self.nV)}
        return fw_labeled

    def single_source_spaths(self, s_label, t_labels=None, d_limit=m.inf, Heap=FibonacciHeap):
        """
        Dijkstra algorithm from s_label until all t_labels reached, and/or limited to less than d_limit distance.

        Return a dict-like object of {vertex: distance} for all vertices visited
        The object has additional attributes:
        .parents := dict of {vertex: predecessor vertex}. source vertex has parent None
        .found := ordered list of reached destinations in t_labels
        .stop := the distance where the search stopped (all destinations found, or d_limit reached) or infinite if the(sub)graph was completely explored
        """
        assert not self.isflow

        # pylint: disable= attribute-defined-outside-init
        class SPathsObject(dict):
            __slots__ = [
                "parents",
                "found",
                "stop",
            ]
        ret = SPathsObject()

        s = self._V_index[s_label]
        if t_labels is None:
            t_set = set(range(self.nV))
        else:
            t_set = set(self._V_index[t_label] for t_label in t_labels)

        queue = Heap([(0, s)], history=True)
        spaths = {}
        parents = {}
        t_found = []
        while queue:
            su, u = queue.pop()
            if su >= d_limit:
                ret.stop = d_limit
                break

            spaths[u] = su
            if u in t_set:
                t_set.remove(u)
                t_found.append(u)
                if not t_set:
                    ret.stop = su
                    break

            for v in self._adj[u]:
                sv = su + self._E[u][v]
                if queue.add(sv, v):
                    parents[v] = u
        else:
            ret.stop = m.inf

        ret.update((self._V[v], d) for v, d in spaths.items())
        ret.parents = {self._V[v]: self._V[p] for v, p in parents.items()}
        ret.parents[s_label] = None
        ret.found = [self._V[t] for t in t_found]
        return ret

    def shortest_path(self, s_label, t_label, **kwarg):
        spaths = self.single_source_spaths(s_label, [t_label], **kwarg)
        return spaths.get(t_label, m.inf)

    def is_bipartite(self):
        # make undirected graph
        if self.isflow:
            adj = self._adj
        else:
            adj = [set() for _ in range(self.nV)]
            for u in range(self.nV):
                for v in self._adj[u]:
                    adj[u].add(v)
                    adj[v].add(u)

        # color undirected graph
        colors = {}
        def bfs_bicolor(s):
            if s in colors: return True
            colors[s] = True
            queue = collections.deque([s])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in colors:
                        colors[v] = not colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False

            return True

        return all(map(bfs_bicolor, range(self.nV)))


def bipartite_matching(left_set, right_set, edges, total_only=True):
    """Maximum bipartite matching

    If total_only is True, return the edge count (cardinality) of the maximum matching
    Otherwise, return a dict of {left_node: right_node} pairs of a maximum matching
    """

    G = Graph(len(left_set)+len(right_set)+2, isflow=True)
    s = object()
    t = object()
    G.add_vertexes([s, t])
    G.add_vertexes(left_set)
    G.add_vertexes(right_set)
    G.add_edges((s, u) for u in left_set)
    G.add_edges((v, t) for v in right_set)
    G.add_edges(edges)

    if total_only:
        return G.max_flow(s, t, total_only=True)
    else:
        flow = G.max_flow(s, t, total_only=False)
        ret = {}
        for u in left_set:
            n = flow.adj(u)
            if n:
                assert len(n) == 1
                ret[u] = n.popitem()[0]

        return ret

#endregion graph.py
#endregion bcf
###############################################################################

import sys
def input(itr=iter(sys.stdin.readlines())):  # pylint: disable= redefined-builtin
    return next(itr).rstrip('\n\r')
###############################################################################

import collections

N,M = map(int, input().split())
Passage = collections.namedtuple("Passage", "A B")
passages = {Passage(*map(int, input().split())) for _ in range(M)}

G = Graph(N, sparse=True)
G.add_vertexes(range(1,N+1))
G.add_edges(passages | {(v, u) for u, v in passages})

spaths = G.single_source_spaths(1)
if len(spaths) == N:
    output = ["Yes"]
    for i in range(2,N+1):
        output.append(spaths.parents[i])
else:
    output = ["No"]

print(*output, sep='\n')
