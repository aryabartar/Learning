class Tree(object):

    def __init__(self, value):
        self.value = value
        self.right_node = None
        self.left_node = None

    def insertLeft(self, value):
        current_left_node = self.left_node
        self.left_node = Tree(value)

        if current_left_node is not None:
            self.left_node.left_node = current_left_node

    def insertRight(self, value):
        current_right_node = self.right_node
        self.right_node = Tree(value)

        if current_right_node is not None:
            self.right_node.right_node = current_right_node

    def getRightChild(self):
        return self.right_node

    def getLeftChild(self):
        return self.left_node

    def setRootVal(self, obj):
        self.value = obj

    def getRootVal(self):
        return self.value


previous_value = None
is_bst = True

def check_bst(root):
    global is_bst
    _check_bst(root)
    return is_bst


def _check_bst(node):
    global previous_value

    if node is None:
        return

    _check_bst(node.left_node)

    if previous_value is not None and node.value < previous_value:
        global is_bst
        is_bst = False

    previous_value = node.value

    _check_bst(node.right_node)




root = Tree(12)
left = Tree(5)
right = Tree(14)
left_left = Tree(1)
left_right = Tree(20)
root.left_node = left
root.right_node = right
left.left_node = left_left
left.right_node = left_right

print(check_bst(root))
