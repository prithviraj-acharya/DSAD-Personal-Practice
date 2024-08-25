from PrintTree import PrintTree
from TreeNode import TreeNode


class BinarySearchTree:

    def __init__(self, arr) -> None:
        self.root = TreeNode(arr[0])

        for i in arr[1:]:
            self.find_and_add_position(self.root, i)

        print("-----------")
        printTree = PrintTree(self.root)
        printTree.print_tree()
        print("-----------")

    def find_and_add_position(self, node, key):
        if key < node.value:
            if node.get_left_child() is None:
                node.set_left_child(TreeNode(key))
            else:
                self.find_and_add_position(node.get_left_child(), key)
        else:
            if node.get_right_child() is None:
                node.set_right_child(TreeNode(key))
            else:
                self.find_and_add_position(node.get_right_child(), key)

    def getRoot(self):
        return self.root

    def doesLeftChildExist(self, node):
        return node.get_left_child() is not None

    def doesRightChildExist(self, node):
        return node.get_right_child() is not None

    def getLeftChild(self, node):
        return node.get_left_child()

    def getRightChild(self, node):
        return node.get_right_child()


if __name__ == "__main__":
    arr = [6, 2, 9, 1, 4, 8]
    bst = BinarySearchTree(arr)
