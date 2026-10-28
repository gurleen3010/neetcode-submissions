class Solution:
    def opr(self, val1: int, val2: int, operator: str) -> int:
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        else:
            return (int)(val1/val2)

    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                val1 = st.pop()
                val2 = st.pop()

                ans = self.opr(val2, val1, t)

                st.append(ans)
            else:
                st.append((int)(t))

        return st.pop()