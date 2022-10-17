class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    #write your code here
    if not root:
        root = BinaryTreeNode(new_value)
        return root
    if new_value < root.data:
         if root.left_child:
            insert(root.left_child,new_value)
         else:
            root.left_child = BinaryTreeNode(new_value)
    else:
        if root.right_child:
            insert(root.right_child,new_value)
        else:
            root.right_child = BinaryTreeNode(new_value)


def inorder(root) -> None:
    if root is None:
        return
    inorder(root.left_child)
    print(root.data, end = " ")
    inorder(root.right_child)
