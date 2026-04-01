class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use min heap instead
        res = nums[0:k]
        heapq.heapify(res)
        for i in range(k, len(nums)):
            if nums[i] > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, nums[i])
        return res[0]