import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = collections.defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        res = []
        for email in graph:
            if email not in visited:
                component = []
                stack = [email]
                visited.add(email)
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                res.append([email_to_name[email]] + sorted(component))
        return res
