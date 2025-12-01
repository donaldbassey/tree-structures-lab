"""
Experimental Analysis of Tree Structures
Generates the 3 required graphs for the laboratory work
"""

import random
import matplotlib.pyplot as plt
import math
import os
from .trees import BST, AVLTree, RedBlackTree


def ensure_graphs_directory():
    """Create graphs directory if it doesn't exist"""
    if not os.path.exists('../graphs'):
        os.makedirs('../graphs')


def experiment_bst_height():
    """Experiment 4: BST height with thousands of keys"""
    print("Running Experiment 4: BST height analysis...")
    sizes = [1000, 5000, 10000, 20000, 50000]
    heights = []
    log_heights = []
    
    for size in sizes:
        print(f"  Testing n = {size:,} keys...")
        temp_heights = []
        
        # 2 trials for each size
        for _ in range(2):
            keys = random.sample(range(size * 3), size)
            bst = BST()
            for key in keys:
                bst.insert(key)
            temp_heights.append(bst.get_height())
        
        avg_height = sum(temp_heights) / len(temp_heights)
        heights.append(avg_height)
        log_heights.append(math.log2(size))
    
    return sizes, heights, log_heights


def experiment_avl_rb_random():
    """Experiment 5: AVL and Red-Black with random keys"""
    print("\nRunning Experiment 5: AVL and Red-Black (random keys)...")
    sizes = [1000, 5000, 10000, 20000]
    avl_heights = []
    rb_heights = []
    avl_bounds = []
    rb_bounds = []
    
    for size in sizes:
        print(f"  Testing balanced trees with n = {size:,} keys...")
        
        keys = random.sample(range(size * 3), size)
        
        avl = AVLTree()
        rb = RedBlackTree()
        
        for key in keys:
            avl.insert(key)
            rb.insert(key)
        
        avl_heights.append(avl.get_height())
        rb_heights.append(rb.get_height())
        avl_bounds.append(1.44 * math.log2(size))
        rb_bounds.append(2 * math.log2(size))
    
    return sizes, avl_heights, rb_heights, avl_bounds, rb_bounds


def experiment_avl_rb_sorted():
    """Experiment 6: AVL and Red-Black with sorted keys"""
    print("\nRunning Experiment 6: AVL and Red-Black (sorted keys)...")
    sizes = [1000, 5000, 10000, 20000]
    avl_heights = []
    rb_heights = []
    avl_bounds = []
    rb_bounds = []
    
    for size in sizes:
        print(f"  Testing with sorted keys, n = {size:,}...")
        
        keys = list(range(size))  # Sorted keys
        
        avl = AVLTree()
        rb = RedBlackTree()
        
        for key in keys:
            avl.insert(key)
            rb.insert(key)
        
        avl_heights.append(avl.get_height())
        rb_heights.append(rb.get_height())
        avl_bounds.append(1.44 * math.log2(size))
        rb_bounds.append(2 * math.log2(size))
    
    return sizes, avl_heights, rb_heights, avl_bounds, rb_bounds


def generate_all_graphs():
    """Generate all 3 required graphs"""
    ensure_graphs_directory()
    
    print("\n" + "="*60)
    print("GENERATING 3 EXPERIMENTAL GRAPHS")
    print("="*60)
    
    # Graph 1: Experiment 4 - BST height
    print("\nCreating Graph 1: BST Height Analysis...")
    sizes_bst, heights_bst, log_h = experiment_bst_height()
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_bst, heights_bst, 'bo-', label='BST Height (Experimental)', linewidth=2, markersize=8)
    plt.plot(sizes_bst, log_h, 'r--', label='log₂(n) (Theoretical O(log n))', linewidth=2)
    plt.plot(sizes_bst, sizes_bst, 'g:', label='n (Theoretical O(n))', linewidth=1, alpha=0.3)
    plt.xlabel('Number of Keys (n)', fontsize=12)
    plt.ylabel('Tree Height', fontsize=12)
    plt.title('Experiment 4: BST Height vs Number of Keys\n(Random Keys, Thousands of Elements)', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('../graphs/experiment4_bst_height.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Graph 1 saved: experiment4_bst_height.png")
    
    # Graph 2: Experiment 5 - AVL and Red-Black with random keys
    print("\nCreating Graph 2: AVL and Red-Black (Random Keys)...")
    sizes, avl_h, rb_h, avl_u, rb_u = experiment_avl_rb_random()
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, avl_h, 'go-', label='AVL Height (Experimental)', linewidth=2, markersize=8)
    plt.plot(sizes, rb_h, 'bo-', label='Red-Black Height (Experimental)', linewidth=2, markersize=8)
    plt.plot(sizes, avl_u, 'g--', label='Upper Bound: 1.44·log₂(n)', linewidth=1.5, alpha=0.7)
    plt.plot(sizes, rb_u, 'b--', label='Upper Bound: 2·log₂(n)', linewidth=1.5, alpha=0.7)
    plt.plot(sizes, [math.log2(s) for s in sizes], 'k:', label='Lower Bound: log₂(n)', linewidth=1.5, alpha=0.5)
    plt.xlabel('Number of Keys (n)', fontsize=12)
    plt.ylabel('Tree Height', fontsize=12)
    plt.title('Experiment 5: AVL and Red-Black Trees\n(Random Keys, Thousands of Elements)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('../graphs/experiment5_avl_rb_random.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Graph 2 saved: experiment5_avl_rb_random.png")
    
    # Graph 3: Experiment 6 - AVL and Red-Black with sorted keys
    print("\nCreating Graph 3: AVL and Red-Black (Sorted Keys)...")
    sizes_sorted, avl_h_s, rb_h_s, avl_u_s, rb_u_s = experiment_avl_rb_sorted()
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_sorted, avl_h_s, 'go-', label='AVL Height (Sorted Keys)', linewidth=2, markersize=8)
    plt.plot(sizes_sorted, rb_h_s, 'bo-', label='Red-Black Height (Sorted Keys)', linewidth=2, markersize=8)
    plt.plot(sizes_sorted, avl_u_s, 'g--', label='Upper Bound: 1.44·log₂(n)', linewidth=1.5, alpha=0.7)
    plt.plot(sizes_sorted, rb_u_s, 'b--', label='Upper Bound: 2·log₂(n)', linewidth=1.5, alpha=0.7)
    plt.plot(sizes_sorted, [math.log2(s) for s in sizes_sorted], 'k:', label='Lower Bound: log₂(n)', linewidth=1.5, alpha=0.5)
    plt.xlabel('Number of Keys (n)', fontsize=12)
    plt.ylabel('Tree Height', fontsize=12)
    plt.title('Experiment 6: AVL and Red-Black Trees\n(Worst Case: Sorted Keys, Thousands of Elements)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('../graphs/experiment6_avl_rb_sorted.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Graph 3 saved: experiment6_avl_rb_sorted.png")
    
    print("\n" + "="*60)
    print("ALL 3 GRAPHS GENERATED SUCCESSFULLY!")
    print("="*60)
    
    # Print summary
    print("\nSUMMARY:")
    print("-" * 40)
    print(f"BST (n=50,000): height = {heights_bst[-1]:.1f}")
    print(f"AVL (random, n=20,000): height = {avl_h[-1]:.1f}")
    print(f"Red-Black (random, n=20,000): height = {rb_h[-1]:.1f}")
    print(f"AVL (sorted, n=20,000): height = {avl_h_s[-1]:.1f}")
    print(f"Red-Black (sorted, n=20,000): height = {rb_h_s[-1]:.1f}")


if __name__ == "__main__":
    generate_all_graphs()
