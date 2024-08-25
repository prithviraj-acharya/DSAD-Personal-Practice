class TreeNode:
    def __init__(self, key) -> None:
        self.value = key
        self.right = None
        self.left = None

    def set_right_child(self, node):
        self.right = node

    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left
