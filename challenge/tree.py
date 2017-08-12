# tree data type pattern
# heaps
# tree transversal

# value, left right

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_list(self):
        """ Returns list of tree values """
        # use recursion
        if self.left is not None:
            left = self.get_list(self.left)
        else:
            left = []

        if self.right is not None:
            right = self.get_list(self.right)
        else:
            right = []

        return left + [self.val] + right


    def insert(self, val):
        # Insert node in tree where 
        if val > root.val:
            if root.right is not None:
                insert(root.right, val)
            else:
                root.right = TreeNode(val)
        elif val < root.val:
            if root.left is not None:
                insert(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val == root.val:
            return None

    def remove():
        pass

def main():

    root = TreeNode(5)
    print(root.val)

    root.left = TreeNode(3)
    root.right = TreeNode(7)

    # print(root.get_list())

if __name__ == "__main__":
    main()