class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[idx]:
                idx = mid
                r = mid - 1
            else:
                l = mid + 1
        l, r = 0, idx - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: return mid
        l, r = idx, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: return mid
        return -1