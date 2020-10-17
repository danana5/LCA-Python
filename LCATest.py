import unittest
from LCA import LCA, Node

class testLCA (unittest.TestCase):
    def test_empty(self):
        root = None
        self.assertEqual (LCA(root, None, None), None, "Should return None for an empty tree")

    def test_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual (LCA(root, 4, 5).key, 2, "Key of LCA should be 2")
        self.assertEqual (LCA(root , 4, 6).key, 1, "Key of LCA should be 1")
        self.assertEqual (LCA(root, 3, 4).key, 1, "Key of LCA should be 1")
        self.assertEqual (LCA(root, 2, 4).key, 2, "Key of LCA should be 2")


if __name__ == '__main__':
    unittest.main()
    print("All Tests Passed Yup")