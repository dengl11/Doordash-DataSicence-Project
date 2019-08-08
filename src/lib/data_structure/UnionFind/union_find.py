# Data Structure: Union Find
# ---------------------------------------------------------------------------

from collections import defaultdict


class UnionFind(object):

    """ Uninon Find with Path Compression """

    def __init__(self):
        self.roots = dict()

    def find(self, x):
        """
        Amoritzed O(log N)
        """
        if self.roots.get(x, x) != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots.get(x, x)

    def union(self, x, y):
        """
        Amoritzed O(log N)
        """
        self.roots[self.find(x)] = self.find(y)

    def clusters(self) -> int:
        """
        """
        return len(set(self.roots.values()))

        
class UnionFindByRank(UnionFind):

    """ Uninon Find with Path Compression """

    def __init__(self):
        self.roots = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        """
        Amoritzed O(inverse_ackermann(N)) ~= O(1)
        """
        if self.roots.get(x, x) != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots.get(x, x)

    def union(self, x, y):
        """
        Amoritzed O(inverse_ackermann(N)) ~= O(1)
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] == self.rank[root_y]:
            self.roots[root_x] = root_y
            self.rank[root_y] += 1
        elif self.rank[root_x] < self.rank[root_y]:
            self.roots[root_x] = root_y
        else:
            self.roots[root_y] = root_x 
