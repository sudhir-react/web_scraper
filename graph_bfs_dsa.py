import time
from collections import deque

class SudhirBFSGraphEngine:
    def __init__(self):
        # Relational Hash Map representing our structural node adjacencies
        self.adjacency_matrix = {}

    def add_medical_node(self, node_name):
        if node_name not in self.adjacency_matrix:
            self.adjacency_matrix[node_name] = []

    def establish_bidirectional_route(self, node_A, node_B):
        if node_A in self.adjacency_matrix and node_B in self.adjacency_matrix:
            self.adjacency_matrix[node_A].append(node_B)
            self.adjacency_matrix[node_B].append(node_A)

    # 🚀 THE BFS ALGORITHM: Scanning layer-by-layer utilizing a FIFO Queue
    def execute_bfs_network_scan(self, start_node):
        print(f"🕵️‍♂️ Initializing BFS Radial Scan starting from: '{start_node}'")
        
        # Track nodes already visited to prevent infinite loop traps
        visited_set = set()
        # FIFO Queue allocation for layer processing tracking
        scan_queue = deque()
        
        # Setup initial parameters
        visited_set.add(start_node)
        scan_queue.append(start_node)
        
        traversal_path = []
        
        while scan_queue:
            # FIFO Pop from the left side (Layer by Layer execution)
            current_node = scan_queue.popleft()
            traversal_path.append(current_node)
            
            # Audit and extract all adjacent neighbors
            for neighbor in self.adjacency_matrix[current_node]:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    scan_queue.append(neighbor)
                    
        return traversal_path

def run_bfs_production_simulation():
    print("🚀 Starting Sudhir's Advanced Graph BFS Routing Engine [Day 22]...\n")
    
    # 1. SETUP: Instantiating our multi-layered grid map
    network = SudhirBFSGraphEngine()
    
    # Register 4 distinct strategic grid nodes
    network.add_medical_node("Raipur Central Hospital")
    network.add_medical_node("AIIMS Raipur Grid")
    network.add_medical_node("Bhilai Medical Outpost")
    network.add_medical_node("Durg Regional Vault")
    
    # Establish network layer relationships
    network.establish_bidirectional_route("Raipur Central Hospital", "AIIMS Raipur Grid")
    network.establish_bidirectional_route("AIIMS Raipur Grid", "Bhilai Medical Outpost")
    network.establish_bidirectional_route("Bhilai Medical Outpost", "Durg Regional Vault")
    
    # 2. RUNTIME ACCELERATION METRICS
    start_time = time.perf_counter()
    
    # Fire the BFS radial engine tracking outwards from Raipur Central
    final_scan_order = network.execute_bfs_network_scan("Raipur Central Hospital")
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. UI RENDERING DISPLAY
    print("\n📊 Final Layer-by-Layer Network Routing Path:")
    print(" ➡️ ".join(final_scan_order))
    print("-" * 75)
    print(f"⚡ BFS Traversal Pipeline Speed : {duration:.4f} ms")
    print(f"📊 Computational Complexity Matrix: O(V + E) - Optimized Graph Flow")
    print("-" * 75)
    print("\n🎉 Advanced Graph BFS routing engine executed successfully with 100% integrity!")

if __name__ == "__main__":
    run_bfs_production_simulation()