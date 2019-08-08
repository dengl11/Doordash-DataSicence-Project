from lib.data_structure.BIT.bit import BIT

import unittest

class test_bit(unittest.TestCase):

    def test_bit_construction(self):
        data = [1, 5, 2, 4, 3]
        greater = [4, 0, 3, 1, 2]
        bit = BIT(len(data))
        for x in data:
            bit.insert(x)
        for x, g in zip(data, greater):
            self.assertEqual(bit.greater_or_equal(x), g + 1)
            self.assertEqual(bit.greater(x), g)
        


if __name__ == "__main__":
    unittest.main()
