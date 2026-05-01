#Binary tree inorder traversal

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
 
#CODE HERE
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        curr = root

        while curr or stack:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process node
            curr = stack.pop()
            result.append(curr.val)
            
            # Move to right subtree
            curr = curr.right
        
        return result



"""
Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]


Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]


Example 3:

Input: root = []
Output: []

Example 4:

Input: root = [1]
Output: [1]
"""