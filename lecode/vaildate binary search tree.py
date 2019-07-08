class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        print(root)
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == '__main__':
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)

    print(Solution().isValidBST(t))
