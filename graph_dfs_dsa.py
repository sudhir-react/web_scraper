import time

class SudhirDFSGraphEngine:
    def __init__(self):
        # Master Hash Map for managing our network structures
        self.network_grid = {}

    def add_hospital_node(self, name):
        if name not in self.network_grid:
            self.network_grid[name] = []

    def connect_nodes_bidirectional(self, node_A, node_B):
        if node_A in self.network_grid and node_B in self.network_grid:
            self.network_grid[node_A].append(node_B)
            self.network_grid[node_B].append(node_A)

    # 🚀 THE DFS ALGORITHM: Recursive Deep Scanning utilizing a LIFO Stack structure
    def execute_dfs_deep_scan(self, current_node, visited_set=None, path_log=None):
        if visited_set is None:
            visited_set = set()
        if path_log is None:
            path_log = []
            print(f"🕵️‍♂️ Initializing DFS Deep-Path Tracking from: '{current_node}'")

        # Mark the current hospital node as visited and log the execution path
        visited_set.add(current_node)
        path_log.append(current_node)

        # Deep-dive into unvisited branches completely before backtracking
        for neighbor in self.network_grid[current_node]:
            if neighbor not in visited_set:
                self.execute_dfs_deep_scan(neighbor, visited_set, path_log)
                
        return path_log

def run_dfs_production_test():
    print("🚀 Starting Sudhir's Advanced Graph DFS Routing Engine [Day 22]...\n")
    
    # 1. SETUP: Instantiating the graph infrastructure
    dfs_engine = SudhirDFSGraphEngine()
    
    # Register core strategic nodes
    dfs_engine.add_hospital_node("Raipur Central Hospital")
    dfs_engine.add_hospital_node("AIIMS Raipur Grid")
    dfs_engine.add_hospital_node("Bhilai Medical Outpost")
    dfs_engine.add_hospital_node("Durg Regional Vault")
    
    # Map deep connection matrix paths
    dfs_engine.connect_nodes_bidirectional("Raipur Central Hospital", "AIIMS Raipur Grid")
    dfs_engine.connect_nodes_bidirectional("AIIMS Raipur Grid", "Bhilai Medical Outpost")
    dfs_engine.connect_nodes_bidirectional("Bhilai Medical Outpost", "Durg Regional Vault")
    
    # 2. RUNTIME BENCHMARKING
    start_time = time.perf_counter()
    
    # Execute recursive deep tracking
    dfs_path = dfs_engine.execute_dfs_deep_scan("Raipur Central Hospital")
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. DISPLAY SUMMARY
    print("\n📊 Final Deep-Path Network Traversal Order (DFS Execution):")
    print(" ➡️ ".join(dfs_path))
    print("-" * 75)
    print(f"⚡ DFS Traversal Pipeline Speed : {duration:.4f} ms")
    print(f"📊 Algorithmic Scaling Complexity: O(V + E) - Linear Graph Time")
    print("-" * 75)
    print("\n🎉 Advanced Graph DFS routing engine executed successfully with 100% integrity!")

if __name__ == "__main__":
    run_dfs_production_test()