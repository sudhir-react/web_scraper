import time

class AdvancedMedicalGraph:
    def __init__(self):
        # Master dictionary (Hash Map) for storing the graph network.
        self.network = {}

    def add_hospital(self, name):
        if name not in self.network:
            self.network[name] = set() # Using a Set to prevent duplicates (O(1) efficiency)

    def link_hospitals(self, h1, h2):
        if h1 in self.network and h2 in self.network:
            self.network[h1].add(h2)
            self.network[h2].add(h1)

    # Magical search function: Is the direct route between two hospitals active?
    def is_directly_connected(self, source_hospital, target_hospital):
        if source_hospital in self.network:
            # Set lookup provides O(1) instantaneous efficiency!
            return target_hospital in self.network[source_hospital]
        return False

def run_medical_lookup_pipeline():
    print("🚀 Initiating Sudhir's Live Hospital Connectivity Lookup Engine [Day 21]...\n")
    
    # 1. INITIALIZE: Creation of the graph database
    geo_grid = AdvancedMedicalGraph()
    
    # Adding nodes
    geo_grid.add_hospital("Raipur Central Hospital")
    geo_grid.add_hospital("AIIMS Raipur Grid")
    geo_grid.add_hospital("Bhilai Medical Outpost")
    
    # Establishing Edges
    geo_grid.link_hospitals("Raipur Central Hospital", "AIIMS Raipur Grid")
    geo_grid.link_hospitals("AIIMS Raipur Grid", "Bhilai Medical Outpost")
    
    # 2. RUNTIME SIMULATION: When an average user checks connectivity on the app.
    start_time = time.perf_counter()
    
    # Test Case 1: Are Raipur Central and AIIMS directly connected?
    check_1 = geo_grid.is_directly_connected("Raipur Central Hospital", "AIIMS Raipur Grid")
    
    # Test Case 2: Are Raipur Central and Bhilai Outpost directly connected? (They are not directly connected; they are connected via AIIMS.)
    check_2 = geo_grid.is_directly_connected("Raipur Central Hospital", "Bhilai Medical Outpost")
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. UI OUTPUT DISPLAY
    print("-" * 75)
    print(f"🔍 [User Inquiry 1]: Raipur Central ➡️ AIIMS Raipur direct connection?")
    print(f"🟢 STATUS: {'✅ Active Connection Enabled' if check_1 else '❌ No Direct Path'}")
    print("-" * 75)
    print(f"🔍 [User Inquiry 2]: Raipur Central ➡️ Bhilai Outpost: Direct connection?")
    print(f"🔴 STATUS: {'✅ Active Connection Enabled' if check_2 else '❌ No Direct Path / Out of Range'}")
    print("-" * 75)
    
    print(f"\n⚡ Search Execution Time : {duration:.4f} ms")
    print(f"📊 Computational Complexity: O(1) - Instant Hash Table Lookup Speed")
    print("\n🎉 Hospital connectivity network lookup completed with 100% operational safety!")

if __name__ == "__main__":
    run_medical_lookup_pipeline()