"""
Tree Structures Implementation
Complete implementation of BST, AVL, and Red-Black trees
Laboratory Work for Data Structures and Algorithms
"""

import sys
sys.setrecursionlimit(10000)


class Node:
    """Node class for all tree types"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # For AVL trees
        self.color = 1   # 1=red, 0=black (for Red-Black trees)
        self.parent = None  # For Red-Black trees


class BST:
    """Binary Search Tree Implementation"""
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Insert a key into BST"""
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    def search(self, key):
        """Search for a key in BST"""
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def delete(self, key):
        """Delete a key from BST"""
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_min(self):
        """Find minimum key in BST"""
        return self._find_min(self.root)
    
    def _find_min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.key
    
    def find_max(self):
        """Find maximum key in BST"""
        return self._find_max(self.root)
    
    def _find_max(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.key
    
    def preorder(self):
        """Preorder traversal (Root-Left-Right)"""
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def inorder(self):
        """Inorder traversal (Left-Root-Right) - returns sorted order"""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
    
    def postorder(self):
        """Postorder traversal (Left-Right-Root)"""
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)
    
    def level_order(self):
        """Level-order traversal (Breadth-First Search)"""
        result = []
        if self.root is None:
            return result
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    
    def get_height(self):
        """Get height of the tree"""
        return self._get_height(self.root)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))


class AVLTree(BST):
    """AVL Tree Implementation (Self-balancing BST)"""
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._get_height(node.left), 
                                self._get_height(node.right))
    
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # Duplicates not allowed
        
        self._update_height(node)
        
        balance = self._get_balance(node)
        
        # LL Case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        
        # RR Case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        
        # LR Case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # RL Case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node


class RedBlackTree:
    """Red-Black Tree Implementation"""
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 0  # black
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL
    
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.NIL
        node.right = self.NIL
        node.color = 1  # new node is red
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        
        if node.parent is None:
            node.color = 0
            return
        
        if node.parent.parent is None:
            return
        
        self._fix_insert(node)
    
    def _fix_insert(self, k):
        while k.parent and k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
    
    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node == self.NIL or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def get_height(self):
        """Get height of Red-Black tree"""
        return self._get_height(self.root)
    
    def _get_height(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def inorder(self):
        """Inorder traversal of Red-Black tree"""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node != self.NIL:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# Export classes for use in other files
__all__ = ['BST', 'AVLTree', 'RedBlackTree']
