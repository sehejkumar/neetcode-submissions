# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue = deque([root])

        res = []

        while queue:
            numNodesInLevel = len(queue)
            nodes = []

            for _ in range(numNodesInLevel):
                currNode = queue.popleft()
                nodes.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(nodes)

        return res
                    


        
        