# Step 1: Creating a blueprint (Class) for the laptop.
class LaptopBlueprint:
    # __init__ means that whenever a new laptop is created, it will have specific features.
    def __init__(self, brand_name, ram_size, storage_size):
        self.brand = brand_name      # Laptop brand
        self.ram = ram_size          # The power of RAM
        self.storage = storage_size  # Storage capacity

    # Function (method) to display laptop details on the screen
    def display_specifications(self):
        print(f"💻 Machine Brand: {self.brand}")
        print(f"⚡ RAM Speed     : {self.ram} GB")
        print(f"💾 Storage Capacity: {self.storage} GB")
        print("---------------------------------------")

# Step 2: Creating real objects (real laptops) using the map.
def run_oops_test():
    print("🚀 Starting Sudhir's Real-World OOPs Simulation...\n")

    # Sudhir-ji's real laptop (Object 1)
    sudhir_laptop = LaptopBlueprint("HP EliteBook", 16, 512)
    
    # Client's laptop (Object 2)
    client_laptop = LaptopBlueprint("MacBook Pro", 8, 256)

    # Step 3: Running both objects live to observe them.
    print("📊 Sudhir's Laptop Specifications:")
    sudhir_laptop.display_specifications()

    print("📊 Client's Laptop Specifications:")
    client_laptop.display_specifications()
    
    print("🎉 OOPs core concepts mapped and executed with 100% clarity!")

if __name__ == "__main__":
    run_oops_test()