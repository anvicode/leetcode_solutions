class Solution:
    def isValid(self, s: str) -> bool:
        arr = list(s)
        stack = []
        open_p = ["(", "[", "{"]
        close_p = [")", "]", "}"]
        if arr[0] in close_p:
            return False
        for i in arr:
            if i in open_p:
                stack.append(i)
            if stack == [] and i in close_p:
                return False
            lp = stack[-1]
            if i in close_p:
                if i == close_p[open_p.index(lp)]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
