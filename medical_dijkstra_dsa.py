import time
import heapq

class SudhirMedicalRouter:
    def __init__(self):
        # Master dictionary for storing the graph network (Adjacency List)
        self.graph = {}

    def add_hospital_node(self, name):
        if name not in self.graph:
            self.graph[name] = []

    def add_medical_route(self, h1, h2, distance_kms):
        # Connecting the route between the two hospitals with distance (weight)
        self.graph[h1].append((h2, distance_kms))
        self.graph[h2].append((h1, distance_kms))

    # 🚀 THE DIJKSTRA ALGORITHM: Priority Queue (Min-Heap) Finding the shortest path using...
    def calculate_shortest_path(self, start_node):
        print(f"🕵️‍♂️ Routing Engine: Calculating shortest paths from '{start_node}'...")
        
        # Setting the distance of all nodes to infinity initially.
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0
        
        # Priority Queue (Min-Heap) Allocation: (distance, node)
        priority_queue = [(0, start_node)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # If we have already found a shortcut, then skip it.
            if current_distance > distances[current_node]:
                continue
                
            # Auditing neighbors' access routes
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                
                # If the new path is shorter than the old path, update it.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    
        return distances

def run_dijkstra_pipeline():
    print("🚀 Initiating Sudhir's Enterprise Dijkstra Shortest Path Router [Day 23]...\n")
    
    # 1. SETUP: Creation of a medical network grid
    router = SudhirMedicalRouter()
    
    router.add_hospital_node("Raipur Central Hospital")
    router.add_hospital_node("AIIMS Raipur Grid")
    router.add_hospital_node("Bhilai Medical Outpost")
    
    # Adding the actual distance between routes (in km)
    router.add_medical_route("Raipur Central Hospital", "AIIMS Raipur Grid", 15) # AIIMS from Raipur = 15 KM
    router.add_medical_route("AIIMS Raipur Grid", "Bhilai Medical Outpost", 25)  # AIIMS to Bhilai = 25 KM
    router.add_medical_route("Raipur Central Hospital", "Bhilai Medical Outpost", 50) # Straight path = 50 KM
    
    # 2. RUNTIME ACCELERATION METRICS
    start_time = time.perf_counter()
    
    # Calculating the shortest distance from Raipur Central to all hospitals.
    shortest_distances = router.calculate_shortest_path("Raipur Central Hospital")
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. UI RENDERING DISPLAY
    print("\n📊 Optimized Shortest Distance Matrix from Raipur Central:")
    print("-" * 75)
    for hospital, dist in shortest_distances.items():
        print(f"🏥 Destination: {hospital:<25} ➡️ Minimum Distance: {dist} KM")
    print("-" * 75)
    
    print(f"⚡ Dijkstra Routing Pipeline Speed : {duration:.4f} ms")
    print(f"📊 Computational Complexity Matrix  : O((V + E) log V) - Logarithmic Grid Efficiency")
    print("-" * 75)
    print("\n🎉 Enterprise Dijkstra routing engine executed successfully with 100% integrity!")

if __name__ == "__main__":
    run_dijkstra_pipeline()
    