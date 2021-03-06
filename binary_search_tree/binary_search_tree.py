"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# Root: The topmost node in the tree
# Child: A node directly connected to another node when moving away from the root node
# Parent: A node directly connected to another node when moving towards the root node.
# Siblings: Nodes that share the same parent are considered siblings.
# Leaf: A node that does not have any children of its own.

# For any given node, all values in the left subtree are less than the value at the given node. 
# Conversely, all values in the right subtree are greater than or equal to the value at the given node.

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        

        # left case?
        # check if the value is less than the root value?
            # move to the left and check if it is none?
                # insert node here
            # otherwise
                # call insert on the root's left node
        # right case?
        # otherwise
            # move to the right and check if it is none?
                # insert the node here
            # otherwise
                # call insert on the root's right node
                

        # other / base case

        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        # base case?
        # check the root node value against target
        # if the root node's value and the target are the same 
            #return true
        
        # left case 
        # check if the target is less than the root
            # check if there is no child to the left
                # return false
            # otherwise
                # call contains on the left child
        
        # right case
        # otherwise
            # check if there is no child to the right
                #return false
            # otherwise
                #call contains on the right child

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if the tree is empty return none
        if not self:
            return None

        # while there is a right child
        while self.right:
            # move to the right
            self = self.right
        
        # once there are no more children to traverse we can return the value
        return self.value

    # return the minimum value found in a tree
    def get_min(self):
        # base case
        # if the tree is empty return none
        if not self:
            return None

        # while there is a left child
        while self.left:
            # move to the left
            self = self.left
        
        # once there are no more child

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call foreach on the root node
        fn(self.value)

        # if left exists
        if self.left:
            # call for each on the left child
            self.left.for_each(fn)

        # if right exists
        if self.right:
            # call for each on the right child
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # instantiate a queue

        # enqueue our starting node (self)

        # while the queue is not empty
            # dequeue the current node
            # print the nodes value

            # check if left child exists
                # enqueue left child

            # check if right child exists
                # enqueue right child
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # instantiate a stack

        # push our starting node (self)

        # while the stack is not empty
            # pop the current node
            # print the nodes value

            # check if left child exists
                # push left child

            # check if right child exists
                # push right child
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  

# Should have the methods insert, contains, get_max
# insert adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
# contains searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
# get_max returns the maximum value in the binary search tree.
# for_each performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value.
# There is a myriad of ways to perform tree traversal; in this case any of them should work.