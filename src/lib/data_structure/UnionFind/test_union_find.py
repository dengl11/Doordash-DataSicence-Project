from lib.data_structure.UnionFind.union_find import UnionFind, UnionFindByRank

import unittest

class test_union_find(unittest.TestCase):

    def test_union_find_path_compression(self):
        uf = UnionFind()
        uf.union(1, 2)
        uf.union(1, 3)
        self.assertEqual(uf.find(1), uf.find(1))
        self.assertEqual(uf.clusters(), 1)
        
    def test_union_find_by_rank(self):
        uf = UnionFindByRank()
        uf.union(1, 2)
        uf.union(1, 3)
        self.assertEqual(uf.find(1), uf.find(1))
        self.assertEqual(uf.clusters(), 1)


if __name__ == "__main__":
    unittest.main()
