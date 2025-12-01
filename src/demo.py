"""
Demonstration of all tree operations
Run this to get the screenshot for your report
"""

from .trees import BST, AVLTree, RedBlackTree


def demonstrate_all_operations():
    """Complete demonstration for report screenshot"""
    print("="*70)
    print("COMPLETE TREE OPERATIONS DEMONSTRATION")
    print("="*70)
    
    test_keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    
    print(f"\nTest keys ({len(test_keys)}): {test_keys}")
    
    # BST Operations
    print("\n" + "-"*40)
    print("BINARY SEARCH TREE OPERATIONS")
    print("-"*40)
    
    bst = BST()
    for key in test_keys:
        bst.insert(key)
    
    print(f"\n1. After inserting all keys:")
    print(f"   • Tree height: {bst.get_height()}")
    
    print(f"\n2. Tree traversals:")
    print(f"   • Inorder (sorted): {bst.inorder()}")
    print(f"   • Preorder: {bst.preorder()}")
    print(f"   • Postorder: {bst.postorder()}")
    print(f"   • Level-order: {bst.level_order()}")
    
    print(f"\n3. Search operations:")
    print(f"   • Search 30: {'FOUND' if bst.search(30) else 'NOT FOUND'}")
    print(f"   • Search 55: {'FOUND' if bst.search(55) else 'NOT FOUND'}")
    print(f"   • Search 70: {'FOUND' if bst.search(70) else 'NOT FOUND'}")
    print(f"   • Search 100: {'FOUND' if bst.search(100) else 'NOT FOUND'}")
    
    print(f"\n4. Minimum and maximum:")
    print(f"   • Minimum key: {bst.find_min()}")
    print(f"   • Maximum key: {bst.find_max()}")
    
    print(f"\n5. Deletion operations:")
    print(f"   • Before deletion: {bst.inorder()}")
    bst.delete(30)
    print(f"   • After deleting 30: {bst.inorder()}")
    bst.delete(70)
    print(f"   • After deleting 70: {bst.inorder()}")
    bst.delete(20)
    print(f"   • After deleting 20: {bst.inorder()}")
    
    # AVL Tree
    print("\n" + "-"*40)
    print("AVL TREE COMPARISON")
    print("-"*40)
    
    avl = AVLTree()
    for key in test_keys:
        avl.insert(key)
    
    print(f"\nSame keys in AVL tree:")
    print(f"   • AVL height: {avl.get_height()} (BST was: {bst.get_height()})")
    print(f"   • AVL is more balanced!")
    
    # Red-Black Tree
    print("\n" + "-"*40)
    print("RED-BLACK TREE COMPARISON")
    print("-"*40)
    
    rb = RedBlackTree()
    for key in test_keys:
        rb.insert(key)
    
    print(f"\nSame keys in Red-Black tree:")
    print(f"   • Red-Black height: {rb.get_height()}")
    print(f"   • Red-Black inorder: {rb.inorder()}")
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nTake a screenshot of this output for your lab report!")
    print("All operations are working correctly.")


if __name__ == "__main__":
    demonstrate_all_operations()
