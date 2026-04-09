class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n != 0 else 0

        t = [0, 1, 1]
        for i in range(3, n + 1):
            t[i % 3] = sum(t)
        
        return t[n % 3]
        