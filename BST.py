class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # Search a node
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Find minimum value node(Inorder Sucssesor)
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # Display (Inorder Traversal)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# ------------------ MAIN PROGRAM ------------------
bst = BST()
root = None

while True:
    print("\n====== Binary Search Tree Menu ======")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display (Inorder)")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter element to insert: "))
        root = bst.insert(root, key)
        print(f"{key} inserted successfully!")

    elif choice == 2:
        key = int(input("Enter element to delete: "))
        root = bst.delete(root, key)
        print(f"{key} deleted successfully (if existed).")

    elif choice == 3:
        key = int(input("Enter element to search: "))
        found = bst.search(root, key)
        if found:
            print(f"{key} found in BST.")
        else:
            print(f"{key} not found in BST.")

    elif choice == 4:
        print("Inorder Traversal of BST:")
        bst.inorder(root)
        print()

    elif choice == 5:
        print("Exiting program... ✅")
        break

    else:
        print("Invalid choice! Please try again.")
