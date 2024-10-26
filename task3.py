class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.count = 0

    def __str__(self, level=0, prefix="Root: "):
        ret = "    " * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")

        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def sum_preorder_traversal(root, number_list=[]):
    if root:
        number_list.append(root.val)

        sum_preorder_traversal(root.left, number_list)
        sum_preorder_traversal(root.right, number_list)

    return sum(number_list)

# Додаємо умову виконання тільки при запуску цього файлу
if __name__ == "__main__":
    # Test
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = delete(root, 7)
    print(root)

    # Викликаємо функції та відображаємо їх результат
    min_node = min_value_node(root)
    max_node = max_value_node(root)
    print(f"Min value node: {min_node.val}")
    print(f"Max value node: {max_node.val}")

    res = sum_preorder_traversal(root)
    print(f"Sum value node: {res}")