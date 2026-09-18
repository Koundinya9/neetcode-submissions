"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = {}

        
        d[node] = Node(node.val)
        q = deque()
        q.append(node)

        while q:
            n = q.popleft()

            for nei in n.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    q.append(nei)

                d[n].neighbors.append(d[nei])

        return d[node]

        
        