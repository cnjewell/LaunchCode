# tree data type pattern
# heaps
# tree transversal

# value, left right

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_list(root):
    """ Returns list of tree values """
    
    if root.left is not None:
        left = get_list(root.left)
    else:
        left = []

    if root.right is not None:
        right = get_list(root.right)
    else:
        right = []

    return left + [root.val] + right


def insert(root, val):
    """ Insert val in root """ 
    
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


def tree_search(root, val):
    """ Returns True if val in is tree """
    if root.val == val:
        return True
    elif root.left is not None:
        tree_search(root.left, val)
    elif root.right is not None:
        tree_search(root.right, val)
    else:
        return False

    

def remove(root, val):
    pass


def main():

    root = TreeNode(5)
    print(root.val)

    root.left = TreeNode(3)
    root.right = TreeNode(7)

    print(get_list(root))

    insert(root, 9)
    print(get_list(root))
    insert(root, 1)
    print(get_list(root))
    insert(root, 6)
    print(get_list(root))
    insert(root, 8)
    print(get_list(root))
    insert(root, 2)
    print(get_list(root))
    insert(root, 4)
    print(get_list(root))

    print(tree_search(root, 2))
    print(tree_search(root, 10))

if __name__ == "__main__":
    main()