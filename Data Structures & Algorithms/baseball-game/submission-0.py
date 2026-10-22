class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for opr in operations:
            if opr == '+':
                stack.append(stack[-1] + stack[-2])
            elif opr == 'D':
                stack.append(stack[-1] * 2)
            elif opr == 'C':
                stack.pop()
            else:
                stack.append(int(opr))

        ans = 0
        while len(stack) > 0:
            ans += stack.pop()

        return ans