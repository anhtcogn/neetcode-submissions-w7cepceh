class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.countNumberOfBitOne(i) for i in range(n + 1)]

    def countNumberOfBitOne(self, n: int):
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count