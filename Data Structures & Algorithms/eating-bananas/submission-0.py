class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = h

        while low <= high:
            mid = low + (high - low) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            
            if hours > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        
        return res