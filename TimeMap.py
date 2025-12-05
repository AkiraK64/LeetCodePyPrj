# 981. Time Based Key-Value Store
class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            arr = self.timeMap[key]
            l = 0
            r = len(arr) - 1
            res = -1
            while l <= r:
                mid = int((l + r) / 2)
                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                elif arr[mid][0] < timestamp:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return "" if res == -1 else arr[res][1]
        return ""

