class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0] * len(temperatures)
        
        i = 0
        while i < len(temperatures):
            temp = temperatures[i]
            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx;

            stack.append(i)
            i += 1

        return result

             