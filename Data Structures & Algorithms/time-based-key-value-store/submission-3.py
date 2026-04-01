class TimeMap:
    def __init__(self):
        self.dt = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dt:
            self.dt[key] = []
        self.dt[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dt.get(key, [])
        if arr == []: return ""
        l, r = 0, len(arr) - 1
        res = ""
        while (l <= r):
            mid = l + (r - l) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
                res = arr[mid][1]
            else:
                r = mid - 1
        return res
