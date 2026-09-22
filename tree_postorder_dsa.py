import time

class SudhirTreeNode:
    def __init__(self, folder_name):
        self.data = folder_name
        self.left = None
        self.right = None

def perform_postorder_traversal(node):
    # Post-order algorithm: Left -> Right -> Root
    if node:
        perform_postorder_traversal(node.left)              # 1. Go left first.
        perform_postorder_traversal(node.right)             # 2. Then go right.
        print(f"🗑️ Processed [ROOT LAST / SAFE DELETE] -> {node.data}") # 3. Finally, work on the root.

def run_postorder_session():
    print("🚀 Starting Sudhir's Advanced Post-order Tree Traversal [Day 20]...\n")
    
    # 1. Construction of tree architecture
    root = SudhirTreeNode("Desktop_Vault")
    root.left = SudhirTreeNode("Ai_tech_Python")
    root.right = SudhirTreeNode("Upwork_Bidding")
    
    print("📊 Executing Post-order Traversal Pipeline (Left ➡️ Right ➡️ Root):")
    print("-" * 65)
    
    start_time = time.perf_counter()
    
    # 2. ALGORITHM EXECUTION
    perform_postorder_traversal(root)
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print("-" * 65)
    print(f"⚡ Post-order Traversal Duration: {duration:.4f} ms")
    print(f"📊 Computational Complexity: O(N) - Linear Node Visit")
    print("-" * 65)
    print("\n🎉 Post-order Tree Traversal executed successfully with 100% computational integrity!")

if __name__ == "__main__":
    run_postorder_session()