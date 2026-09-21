import time

class SudhirTreeNode:
    def __init__(self, folder_name):
        self.data = folder_name
        self.left = None
        self.right = None

def perform_inorder_traversal(node):
    # In-order algorithm: Left -> Root -> Right
    if node:
        perform_inorder_traversal(node.left)  # 1. Go left first.
        print(f"📁 Processed -> {node.data}")   # 2. Print the route data.
        perform_inorder_traversal(node.right) # 3. Then go right.

def run_traversal_session():
    print("🚀 Starting Sudhir's Advanced Tree Traversal Algorithm [Day 19]...\n")
    
    # 1. Construction of the tree architecture (yesterday's base)
    root = SudhirTreeNode("Desktop_Vault")
    root.left = SudhirTreeNode("Ai_tech_Python")
    root.right = SudhirTreeNode("Upwork_Bidding")
    
    print("📊 Executing In-order Traversal Pipeline (Left ➡️ Root ➡️ Right):")
    print("-" * 60)
    
    start_time = time.perf_counter()
    
    # 2. ALGORITHM EXECUTION
    perform_inorder_traversal(root)
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print("-" * 60)
    print(f"⚡ Traversal Execution Time: {duration:.4f} ms")
    print(f"📊 Worst-Case Complexity: O(N) - Linear Node Visit")
    print("\n🎉 Tree Traversal executed successfully with 100% computational integrity!")

if __name__ == "__main__":
    run_traversal_session()