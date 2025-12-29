class DailySolution:
    def __init__(self):
        pass
    def minSwaps(self, nums: list[int], forbidden: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for f in forbidden:
            count[f] = count.get(f, 0) + 1
        n = len(nums)
        for _,v in count.items():
            if v > n:
                return -1
        badCount = {}
        totalBadCount = 0
        for i in range(n):
            if nums[i] == forbidden[i]:
                badCount[nums[i]] = badCount.get(nums[i], 0) + 1
                totalBadCount += 1
        maxi = 0
        for _,v in badCount.items():
            maxi = max(v, maxi)
        return max(maxi, int((totalBadCount + 1) / 2))