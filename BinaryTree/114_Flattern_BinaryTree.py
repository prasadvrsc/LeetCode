class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    #O(n) Time | O(n) space

    def flatten_recursion(self, root):
        if root is None:
            return
        self.prev = root
        self.flatten_recursion(root.left)

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten_recursion(temp)
    
    
    #O(n) Time | O(1) Space
    def flatten_no_space(self,root):
        if root is None:
            return
        while root is not None:
            if root.left is None:
                root = root.right
            else:
                temp = root.right
                root.right = root.left
                root.left = None
                #Move the root to the right 
                root = root.right
                #Check for right most leaf node
                right_node = root
                while right_node.right is not None:
                    right_node  = right_node.right
                #assign temp node to right most leaf node
                right_node.right = temp


# Test Case

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)







                









