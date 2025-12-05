class Solution:
    def __init__(self):
        pass
    # 128. Longest Consecutive Sequence
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            length = 1
            while num + length in numSet:
                length += 1
            res = max(res, length)
        return res