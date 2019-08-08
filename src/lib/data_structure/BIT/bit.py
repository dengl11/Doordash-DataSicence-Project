# Data Structure: Binary Index Tree (Fenwick Tree)
# ---------------------------------------------------------------------------

class BIT(object):

    """Binary index tree"""

    def __init__(self, sz : int):
        """
        Args:
            sz: size of the tree, i.e. number of elements to hold
        """
        self.eles = [0] * (sz + 1)
        
    def greater_or_equal(self, x : int) -> int :
        """ Return the number of elements >= x
        Time complexity: O(log(N))
        """
        ans = 0
        while x < len(self.eles):
            ans += self.eles[x]
            x += (x & -x) # x & -x: the LSB of x
        return ans

    def greater(self, x : int) -> int :
        """ Return the number of elements > x
        Time complexity: O(log(N))
        """
        return self.greater_or_equal(x) - 1

    def insert(self, x : int):
        """ Insert x to self.eles
        Time complexity: O(log(N))
        """
        while x > 0:
            self.eles[x] += 1
            x -= (x & -x) # x & -x: the LSB of x
