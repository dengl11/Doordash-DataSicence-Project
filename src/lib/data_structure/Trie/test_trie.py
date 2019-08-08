from lib.data_structure.Trie.trie import *

import unittest

class test_trie(unittest.TestCase):

    def test_trie_construction(self):
        words = ["apple", "app", "go", "google"]
        trie = words_to_trie(words)
        pretty_print_trie(trie)
        


if __name__ == "__main__":
    unittest.main()
