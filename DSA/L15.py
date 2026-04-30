#Remove Duplicate from sorted list

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
"""

#CODE HERE
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next
                
        return head



"""
Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""