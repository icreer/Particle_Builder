
from types import NoneType
import pyray


class KDT:
    """
    Implementation of the K-Dimensional Tree (KDT) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify KDT.Node
    """

    class Node:
        """
        Each node of the KDT will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty KDT.
        """
        self.root = None
    
    def get_root(self):
        return self.root

    def insert(self, data):
        """
        Insert 'data' into the KDT.  If the KDT
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = KDT.Node(data)
        else:
            self._insert(data, self.root, 0)  # Start at the root

    def _insert(self, data, node, axis):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data[axis] < node.data[axis]:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = KDT.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left, abs(axis - 1))
        elif data[axis] > node.data[axis]:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = KDT.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right, abs(axis - 1))
        

    def __contains__(self, data):
        """ 
        Checks if data is in the KDT.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_KDT:
            ("5 is in the KDT")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        #try/except for when the node is NoneType
        try:
            if data == node.data:
                # The tree contains the data
                return True
            if data < node.data:
                # The data belongs on the left side.
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
            elif data > node.data:
                # The data belongs on the right side.
                # Need to keep looking.  Call _contains
                # recursively on the right sub-tree.
                return self._contains(data, node.right)
        except:
            return False
        return False


    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the KDT.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_KDT:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def get_height(self):
        """
        Determine the height of the KDT.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the KDT.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else:
            if (1 + self._get_height(node.left)) > (1 + self._get_height(node.right)):
                return 1 + self._get_height(node.left)
            else:
                return 1 + self._get_height(node.right)


    #I hate this function specifically
    def distance_squared(self, data, point2):
        try:
            x1, y1 = data.data
        except:
            x1, y1 = data
        try:
            x2, y2 = point2

        except:
            x2 = point2
            y2 = point2           

        dx = x1 - x2
        dy = y1 - y2

        return dx * dx + dy * dy

    def closer_distance(self, data, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        d1 = self.distance_squared(data, p1)
        d2 = self.distance_squared(data, p2)

        if d1 < d2 and d1 is not 0:
            return p1
        elif d2 < d1 and d2 is not 0:
            return p2


    def closest_point(self,data):
        if self.root is None:
            return None
        else:
            return self._closest_point(self.root, data, 0)

    def _closest_point(self, node, data, axis):
        
        try:
            next_branch = None
            opposite_branch = None

            if data[axis] < node.data[axis]:
                next_branch = node.left
                opposite_branch = node.right
            else:
                next_branch = node.right
                opposite_branch = node.left

            axis = abs(axis - 1)
            best = self.closer_distance(data, self._closest_point(next_branch, data, axis), node.data)

            if self.distance_squared(data, best) > (data[axis] - node.data[axis]) ** 2:
                best = self.closer_distance(data, self._closest_point(opposite_branch, data, axis), best)

            return best
        except:
            return None
    


# NOTE: Functions below are not part of the KDT class above. 


def create_kdt_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced KDT.  If 
    the values in the sorted_list were inserted in order from left
    to right into the KDT, then it would resemble a linked list (unbalanced). 
    To get a balanced KDT, the _insert_middle function is called to 
    find the middle item in the list to add first to the KDT.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    kdt = KDT()  # Create an empty KDT to start with     
    #Make sure that the list has elements in it
    if len(sorted_list) > 0:
        _insert_middle(sorted_list, 0, kdt)
    return kdt

def _insert_middle(sorted_list, axis, kdt):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'KDT' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2 which is the middle) would be added 
    to the 'KDT' (the insert function above can be used to do this).   

    Subsequent recursive calls are made to insert the middle from the values 
    before 30 and the values after 30.  If done correctly, the order
    in which values are added (which results in a balanced KDT) will be:

    30, 10, 20, 50, 40, 60

    This function is intended to be called the first time by 
    create_KDT_from_sorted_list.

    The purpose for having the first and last parameters is so that we do 
    not need to create new sublists when we make recursive calls.  Avoid 
    using list slicing to create sublists to solve this problem.

    """

    #need to resort based on axis for every loop, but can only resort the half of the array that is being checked.

    #Finds the index of the middle value

    
    n = len(sorted_list)
    if n <= 0:
        return None
    sorted_list.sort(key = lambda sorted_list:sorted_list[axis])
    median = n // 2
    kdt.insert(sorted_list[median])


    
    axis = abs(axis - 1)
    #recursion
    #left branch
    _insert_middle(sorted_list[:median], axis, kdt)
    #right branch
    _insert_middle(sorted_list[median + 1:], axis, kdt)
    return kdt