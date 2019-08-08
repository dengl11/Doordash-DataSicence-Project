from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        self._balance()
    
    def _balance(self):
        if abs(len(self.left) - len(self.right)) <= 1: return
        if len(self.left) > len(self.right):
            x = -heappop(self.left)
            heappush(self.right, x)
        else:
            x = heappop(self.right)
            heappush(self.left, -x)
        
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        if len(self.left) > len(self.right):
            return -self.left[0]
        return self.right[0]
