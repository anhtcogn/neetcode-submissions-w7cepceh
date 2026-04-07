class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            h = (target - p) / s

            if not stack or h > stack[-1]:
                stack.append(h)
            else:
                continue

        return len(stack) 