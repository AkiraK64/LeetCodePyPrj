import heapq
import math

class DailySolution:
    def __init__(self):
        pass
    # 3432. Count Partitions with Even Sum Difference
    def countPartitions(self, nums: list[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        return len(nums) - 1 if sum % 2 == 0 else 0
    # 153. Find Minimum in Rotated Sorted Array
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while l <= r:
            mid = int((l + r) / 2)
            res = min(res, nums[mid])
            if nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                r = mid - 1
            elif nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                l = mid + 1
            else:
                res = min(res, nums[l])
                break
        return res
    # 33. Search in Rotated Sorted Array
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    # 3578. Count Partitions With Min-Max Difference At most K
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = int(1e9+7)
        n = len(nums)
        l=1
        res = [0 for i in range(n+1)]
        prefix = [0 for i in range(n+1)]
        res[0] = 1
        prefix[0] = 1
        d = {}
        for r in range(1,n+1):
            cur = nums[r-1]
            d[cur] = d.get(cur, 0) + 1
            while max(d) - min(d) > k:
                d[nums[l-1]] -= 1
                if(d[nums[l-1]] == 0):
                    d.pop(nums[l-1])
                l += 1
            res[r] = (prefix[r-1] - (0 if l < 2 else prefix[l-2])) % MOD
            res[r] = (res[r] + MOD) % MOD
            prefix[r] = (prefix[r-1] + res[r]) % MOD
        return res[-1]
    # 1925. Count Squares Sum Triples
    def countTriples(self, n: int) -> int:
        m = int(math.sqrt(n**2/2))
        max = n**2
        res = 0
        for i in range(1, m+1):
            for j in range(i+1, n):
                sum = i**2 + j**2
                if sum > max:
                    break
                sqrt = int(math.sqrt(sum))
                if sum == sqrt**2:
                    res += 2
        return res
