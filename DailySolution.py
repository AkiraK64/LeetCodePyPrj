class DailySolution:
    def __init__(self):
        pass
    # 3432. Count Partitions with Even Sum Difference
    def countPartitions(self, nums: list[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        return len(nums) - 1 if sum % 2 == 0 else 0