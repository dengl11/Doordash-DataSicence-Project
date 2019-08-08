# Data Structure: trie
# ---------------------------------------------------------------------------
from collections import defaultdict

# marker of terminal node
END = '$'

def words_to_trie(words):
    """construct a trie from an arry of words
    Args:
        words: [word1, word2, ...]

    Return: {c1: {c2: {..., END: index of word in words}
    """
    # sort for better formatting in pretty_print_trie
    words.sort(key = lambda w: len(w))
    TrieNode = lambda: defaultdict(TrieNode)
    trie = TrieNode()
    for i, w in enumerate(words):
        curr_node = trie
        for j, c in enumerate(w):
            curr_node = curr_node[c]
            if j == len(w) - 1:
                curr_node[END] = i
    return trie
    

def pretty_print_trie(trie, depth = 0):
    """pretty print a trie in the form of multi-level dictionary
    Args:
        trie: 

    Return:  {c1: {c2: {..., END: index of word in words} 
    """
    for ch, child in trie.items():
        line = "{}{}".format(" "*depth, ch)
        if ch == END:
            line += ": " + str(child)
            print(line)
        else:
            print(line)
            pretty_print_trie(child, depth + 1)
