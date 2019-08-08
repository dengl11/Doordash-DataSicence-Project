from lib.algorithm.fisher_yates.fisher_yates_shuffle import fisher_yates_shuffle

import unittest

class test_fisher_yates(unittest.TestCase):

    def test_fisher_yates(self):
        words = ["apple", "app", "go", "google"]
        for _ in range(3):
            shuffled = words[:]
            fisher_yates_shuffle(shuffled)
            self.assertNotEqual(words, shuffled)
        


if __name__ == "__main__":
    unittest.main()
