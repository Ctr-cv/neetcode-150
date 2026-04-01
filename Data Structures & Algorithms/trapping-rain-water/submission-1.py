class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        water = [0] * len(height)
        l, r = 0, len(height) - 1
        lh, rh = 0, 0
        while (l <= r):
            if height[l] > height[r]:
                water[r] = max(0, rh - height[r])
                if height[r] > rh:
                    rh = height[r]
                r -= 1
            else:
                water[l] = max(0, lh - height[l])
                if height[l] > lh:
                    lh = height[l]
                l += 1
        return sum(water)
            
            