from lib.algorithm.longest_increasing_subsequence.lis import lis, lengthOfLIS

import unittest

class test_lis(unittest.TestCase):

    def test_lic(self):
        arr = [0, 8, 4, 12, 2]
        seq = lis(arr)
        self.assertEqual(seq, [0, 4, 12])
        self.assertEqual(lengthOfLIS(arr), 3)

        arr = [1, 3, 2, 4, 5]
        seq = lis(arr)
        self.assertEqual(seq, [1, 2, 4, 5])
        self.assertEqual(lengthOfLIS(arr), 4)
        
        arr = [10, 9, 2, 5, 3, 7, 101, 18]
        seq = lis(arr)
        self.assertEqual(seq, [2, 3, 7, 18])
        self.assertEqual(lengthOfLIS(arr), 4)


if __name__ == "__main__":
    unittest.main()
