import time

class SudhirTreeNode:
    def __init__(self, folder_name):
        self.data = folder_name
        self.left = None
        self.right = None

def perform_preorder_traversal(node):
    # Pre-order algorithm: Root -> Left -> Right
    if node:
        print(f"📁 Processed [ROOT FIRST] -> {node.data}") # 1. Print the data for the first route.
        perform_preorder_traversal(node.left)             # 2.Then go left. 
        perform_preorder_traversal(node.right)            # 3. Finally, go right.

def run_preorder_session():
    print("🚀 Starting Sudhir's Advanced Pre-order Tree Traversal [Day 20]...\n")
    
    # 1. Building the Tree Architecture (Our Strong Foundation)
    root = SudhirTreeNode("Desktop_Vault")
    root.left = SudhirTreeNode("Ai_tech_Python")
    root.right = SudhirTreeNode("Upwork_Bidding")
    
    print("📊 Executing Pre-order Traversal Pipeline (Root ➡️ Left ➡️ Right):")
    print("-" * 65)
    
    start_time = time.perf_counter()
    
    # 2. ALGORITHM EXECUTION
    perform_preorder_traversal(root)
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print("-" * 65)
    print(f"⚡ Pre-order Traversal Duration: {duration:.4f} ms")
    print(f"📊 Computational Complexity: O(N) - Linear Node Visit")
    print("-" * 65)
    print("\n🎉 Pre-order Tree Traversal executed successfully with 100% computational integrity!")

if __name__ == "__main__":
    run_preorder_session()