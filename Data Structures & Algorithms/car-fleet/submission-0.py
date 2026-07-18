class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        points = sorted(zip(position, speed), reverse=True)
        stack = []
        # we want montonically increasing stack

        for p, s in points:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 
