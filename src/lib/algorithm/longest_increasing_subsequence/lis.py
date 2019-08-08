# Algorithm: Longest Increasing Subsequence
# ----------------------------------------------------------------------------
from bisect import bisect_left as bl

def lis(arr : [int]) -> [int]:
    """ O(N log N)
    - processes the sequence elements in order
    - maintain the longest increasing subsequence found so far

    Return the longest increasing subsequence
    """
    n = len(arr)
    dp = []
    pre = [-1] * n # pre[i]: the index of the previous number for number at index i
    for i, x in enumerate(arr):
        # binary search (bisect_left)
        lo, hi = 0, len(dp) - 1
        while lo <= hi: # we allow lo > hi, so continue while lo <= hi, not lo < hi
            mid = (lo + hi + 1) // 2
            if arr[dp[mid]] < x: lo += 1
            else: hi -= 1
        # now lo is the position in dp that x should be put in
        pre[i] = dp[lo - 1] if lo >= 1 else -1
        if lo >= len(dp):
            dp.append(i)
        else:
            dp[lo] = i
    # reconstruct the subsequence
    ans = []
    k = dp[-1]
    for _ in range(len(dp)):
        ans.append(arr[k])
        k = pre[k]
    return ans[::-1]


def lengthOfLIS(nums : [int]) -> int:
    """ O(N log N)
    Return the length of longest increasing subsequence
    """
    dp = [0] * len(nums)
    L = 0
    for i, x in enumerate(nums):
        j = bl(dp, x, lo=0, hi = max(L, 0))
        if j == L:
            L += 1
        dp[j] = x
    return L 
