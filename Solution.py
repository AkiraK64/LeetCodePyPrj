import heapq
import math
from ListNode import ListNode
from TreeNode import TreeNode
from collections import deque

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
    # 143. Reorder List
    def reorderList(self, head: ListNode | None) -> None:
        mid = head
        prevMid = ListNode(0, mid)
        tail = head
        while tail.next != None:
            prevMid = prevMid.next
            mid = mid.next
            tail = tail.next
            if tail.next != None:
                tail = tail.next
        curMid = mid
        nextMid = mid.next
        while nextMid != None:
            prevMid = curMid
            curMid = nextMid
            nextMid = nextMid.next
            curMid.next = prevMid
        cur = head
        curNext = head
        prevTail = tail
        while mid != tail:
            curNext = cur.next
            prevTail = tail.next
            cur.next = tail
            tail.next = curNext
            cur = curNext
            tail = prevTail
        if cur != mid:
            cur.next = mid
        tail.next = None
    # 287. Find the Duplicate Numbers
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
    # 235. Lowest Common Ancestor Of Binary Search Tree
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or p == None or q == None:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    # 621. Task Schedule
    def leastInterval(self, tasks: list[str], n: int) -> int:
        fTask = {}
        for t in tasks:
            fTask[t] = fTask.get(t, 0) + 1
        maxHeap = []
        for t in fTask:
            heapq.heappush(maxHeap, -fTask[t])
        q = deque()
        time = 0
        while len(maxHeap) > 0 or len(q) > 0:
            time += 1
            if len(maxHeap) == 0:
                nextTask = q.popleft()
                time = nextTask[1]
                heapq.heappush(maxHeap, -nextTask[0])
            elif len(q) > 0 and q[0][1] == time:
                heapq.heappush(maxHeap, -q.popleft()[0])
            curTask = heapq.heappop(maxHeap)
            if -curTask > 1:
                q.append([-curTask-1, time + n + 1])
        return time
    # 199. Binary Tree Right Side View
    def rightSideView(self, root: TreeNode | None) -> list[int]: 
        res = []
        if root == None:
            return res
        dq = deque([root])
        while len(dq) > 0:
            res.append(dq[-1].val)
            size = len(dq)
            while size > 0:
                curNode = dq.popleft()
                if curNode != None:
                    if curNode.left != None:
                        dq.append(curNode.left)
                    if curNode.right != None:
                        dq.append(curNode.right)
                size -= 1
        return res  
    # 1448. Count Good Nodes In Binary Tree
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs_goodNodes(root, root.val)
    def dfs_goodNodes(self, root: TreeNode | None, maxVal: int) -> int:
        if root == None:
            return 0
        res = 0
        if root.val >= maxVal:
            res += 1
        newMaxVal = max(maxVal, root.val)
        res += self.dfs_goodNodes(root.left, newMaxVal)
        res += self.dfs_goodNodes(root.right, newMaxVal)
        return res
    # 98. Validate Binary Search Tree
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.dfs_isValidBST(root, None, None)
    def dfs_isValidBST(self, root:TreeNode | None, ancestorL: TreeNode | None, ancestorR: TreeNode | None) -> bool:
        if root == None:
            return True
        if ancestorL != None and root.val >= ancestorL.val:
            return False
        if ancestorR != None and root.val <= ancestorR.val:
            return False
        return self.dfs_isValidBST(root.left, root, ancestorR) and self.dfs_isValidBST(root.right, ancestorL, root)