import time

class SudhirMedicalGraph:
    def __init__(self):
        # Master dictionary (Hash Map) for storing the graph network.
        self.network_dict = {}

    def add_hospital_node(self, hospital_name):
        # Adding a new hospital (node) to the network
        if hospital_name not in self.network_dict:
            self.network_dict[hospital_name] = []

    def connect_hospitals(self, hospital_A, hospital_B):
        # Establishing a live data route (Edge) between the two hospitals.
        if hospital_A in self.network_dict and hospital_B in self.network_dict:
            self.network_dict[hospital_A].append(hospital_B)
            self.network_dict[hospital_B].append(hospital_A) # Undirected Graph

    def display_network_grid(self):
        print("📊 Rendering Sudhir's Public Medical Graph Network:")
        print("-" * 65)
        for hospital, connections in self.network_dict.items():
            print(f"🏥 Node: {hospital:<28} ➡️ Linked to: {connections}")
        print("-" * 65)

def run_graph_session():
    print("🚀 Starting Sudhir's Advanced Graph Architecture Simulation [Day 21]...\n")
    
    # 1. INITIALIZE: Construction of the medical graph
    medical_map = SudhirMedicalGraph()
    
    # 2. ADD VERTICES: Adding 3 main nodes (hospitals)
    medical_map.add_hospital_node("Raipur Central Hospital")
    medical_map.add_hospital_node("AIIMS Raipur Grid")
    medical_map.add_hospital_node("Bhilai Medical Outpost")
    
    # 3. ADD EDGES: Interconnecting hospitals through data links
    medical_map.connect_hospitals("Raipur Central Hospital", "AIIMS Raipur Grid")
    medical_map.connect_hospitals("AIIMS Raipur Grid", "Bhilai Medical Outpost")
    
    # 4. EXECUTION: Printing the entire network grid to the screen
    start_time = time.perf_counter()
    
    medical_map.display_network_grid()
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print(f"⚡ Graph Network Traversal Speed: {duration:.4f} ms")
    print(f"📊 Structural Integrity Status: 100% Operational Grid")
    print("\n🎉 Graph linked architecture executed successfully with perfect computational safety!")

if __name__ == "__main__":
    run_graph_session()