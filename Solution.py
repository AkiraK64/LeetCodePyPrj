import heapq
import math

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
    # 11. Container With Most Water
    def maxArea(self, height: list[int]) -> int:
        length = len(height)
        l = 0
        r = length - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res 
    # 853. Car Fleet
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        amount = len(position)
        for i in range(0, amount):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: -x[0])
        stack = []
        for i in range(0, amount):
            time = 1.0 * (target - cars[i][0]) / cars[i][1]
            if len(stack) == 0:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)
    # 215. Kth Largest Element in an Array
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) == k:
                heapq.heappushpop(pq, num)
            else:
                heapq.heappush(pq, num)
        return pq[0]
    # 973. K Closest Points to Origin
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            if len(heap) == k:
                heapq.heappushpop(heap, (-dist, point))
            else:
                heapq.heappush(heap, (-dist, point))
        return [p for _,p in heap]

