class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + '/'
        stack = []
        temp = ""

        for i in range(len(path)):
            if path[i] == '/':
                if temp == "..":
                    if stack:
                        stack.pop()
                elif temp != "" and temp != '.':
                    stack.append(temp)
                temp = ""
            else:
                temp += path[i]
        
        ans = '/' + '/'.join(stack)
        return ans

            
        