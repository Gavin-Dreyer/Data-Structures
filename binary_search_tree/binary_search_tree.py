from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('./queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if less than self.value = self.left
        # if greater than self.value = self.right
        # if self.right and self.left are None
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        while self.right is not None:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):

        # print(self.value)
        # if self.left is not None, cb
        # if self.right is not None, cb
        if self.right is None and self.left is None:
            return cb(self.value)

        cb(self.value)
        if self.left is not None and self.right is not None:
            return self.left.for_each(cb), self.right.for_each(cb)
        elif self.right is not None:
            return self.right.for_each(cb)
        elif self.left is not None:
            return self.left.for_each(cb)

    # DAY 2 Project -----------------------
    # DFT
    # Initialize a stack
    # Push root to stack
    # While stack not empty
    # Pop root out of stack into temp
    # If temp has right put into stack
    # If temp has left put into stack

    # BFT
    # Initialize a queue
    # Push root to queue
    # While queue not empty
    # Pop root out of queue into temp
    # If temp has right put into queue
    # If temp has left put into queue

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return

        else:
            self.in_order_print(node.left)
            print(node.value)

            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            temp = queue.dequeue()
            print(temp.value)

            if temp.left:
                queue.enqueue(temp.left)

            if temp.right:
                queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            stack.pop()
            print(node.value)
            if node.right and node.left:
                node.dft_print(node.right), node.dft_print(node.left)
            elif node.right:
                node.dft_print(node.right)
            elif node.left:
                node.dft_print(node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
