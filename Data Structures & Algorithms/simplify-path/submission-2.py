class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        idx = 0

        while idx < len(path):
            while idx < len(path) and path[idx] == '/':
                idx += 1
            
            if idx < len(path) and path[idx] != '/':
                miniStr = ''

                while idx < len(path) and path[idx] != '/':
                    miniStr += path[idx]
                    idx += 1

                if miniStr == '.':
                    continue
                elif miniStr == '..':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(miniStr)

        return '/' + '/'.join(stack)
