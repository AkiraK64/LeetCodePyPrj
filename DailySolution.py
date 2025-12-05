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
    