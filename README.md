# Doodle

Just for casual scripting

Type bash in terminal to start WSL

Type anything below for copy:


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to map the original node to its corresponding cloned (deep copied) node.
        # This is crucial for handling cycles and avoiding infinite loops.
        oldToNew = {}

        def dfs(node):
            # Base Case: If the node has already been cloned, 
            # return its existing clone from the hash map.
            if node in oldToNew:
                return oldToNew[node]

            # Create a shallow copy of the current node (just the value for now).
            copy = Node(node.val)
            
            # Immediately store the mapping *before* visiting neighbors.
            # This ensures that if a neighbor points back to this node, 
            # the DFS can hit the base case above instead of recursing infinitely.
            oldToNew[node] = copy
            
            # Recursively clone all the neighbors of the current node.
            for nei in node.neighbors:
                # dfs(nei) will return the cloned neighbor, which we then 
                # append to our current copy's neighbors list.
                copy.neighbors.append(dfs(nei))
                
            return copy

        # Kick off the DFS if the input graph is not empty.
        # If the input is None, safely return None.
        return dfs(node) if node else None
