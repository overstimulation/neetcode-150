class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for segment in path.split("/"):
            if segment == "" or segment == ".":
                continue
            if segment == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(segment)

        return "/" + "/".join(stack)
