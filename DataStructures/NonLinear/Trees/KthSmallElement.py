from BinarySearchTree import BinarySearchTree


class KthSmallElement:
    def __init__(self, arr, position) -> None:
        self.position = position
        self.result = []
        self.bst = BinarySearchTree(arr)
        self.inOrderTraversal()

    def inOrderTraversal(self):
        self._inOrderTraversal(self.bst.root, self.result)
        print("In-order:", self.result)
        print("Kth Small element: ", self.result[self.position - 1])

    def _inOrderTraversal(self, node, result):

        if node is not None:
            self._inOrderTraversal(node.left, result)
            result.append(node.value)
            self._inOrderTraversal(node.right, result)


if __name__ == "__main__":
    arr = [6, 2, 9, 1, 4, 8]
    KthSmallElement(arr, 3)
