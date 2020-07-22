class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, level=0):
        if self.data:
            self.print_tree(self.left, level + 1)
            # TODO: fix this, not python3 comaptible
            print(' ' * 4 * level + '->', self.data)
            self.print_tree(self.right, level + 1)

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def main():
    root = BinaryTree(15)
    root.insert(3)
    root.insert(19)
    root.insert(32)
    root.insert(10333)
    root.insert(-5)

    root.print_tree(root)


if __name__ == '__main__':
    main()
