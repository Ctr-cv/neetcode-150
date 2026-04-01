class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hq , res = [], []
        for i in range(k):
            hq.append((-nums[i], i))
        heapq.heapify(hq)
        curmax = -hq[0][0]
        res.append(-hq[0][0])
        for i in range(k, len(nums)):
            while len(hq) != 0 and hq[0][1] <= i - k:
                heapq.heappop(hq)
            heapq.heappush(hq, (-nums[i], i))
            curmax = -hq[0][0]
            res.append(curmax)
        return res