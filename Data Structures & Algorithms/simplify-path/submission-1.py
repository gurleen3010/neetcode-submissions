class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        idx = 0

        while idx < len(path):
            if path[idx] == '/':
                idx += 1
                continue
            else:
                miniStr = ''
                countDots, countChar = 0, 0
                while idx < len(path) and path[idx] != '/':
                    if path[idx] == '.':
                        countDots += 1
                    else:
                        countChar += 1

                    miniStr += path[idx]
                    idx += 1

                if countChar == 0:
                    if countDots > 2:
                        stack.append(miniStr)
                    elif len(stack) > 0 and countDots == 2:
                        stack.pop()
                else:
                    stack.append(miniStr)

        
        if len(stack) == 0:
            return '/'

        stack.reverse()

        Str = ''
        while len(stack) > 0:
            Str += '/' + stack.pop()    

        return Str
