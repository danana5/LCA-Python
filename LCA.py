class Node():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

def LCA(root, n1, n2):

    if root == None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    lcaLeft = LCA(root.left, n1, n2)
    lcaRight = LCA(root.right, n1, n2)

    if lcaLeft and lcaRight:
        return root

    return lcaLeft if lcaLeft is not None else lcaRight