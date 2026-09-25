import time

class EmergencyOxygenStackBuffer:
    def __init__(self):
        # Emergency Oxygen Slot Buffer (LIFO Stack)
        self.oxygen_pipeline = []

    def admit_critical_patient(self, patient_name, oxygen_saturation):
        # Immediately registering a critical patient at the top of the stack.
        print(f"🚨 ALERT: Incoming Critical Patient -> '{patient_name}' (SpO2: {oxygen_saturation}%)")
        self.oxygen_pipeline.append({"name": patient_name, "spo2": oxygen_saturation})

    def allocate_immediate_cylinder(self):
        # Immediately issuing a cylinder to the last-arrived (most critical) patient under the LIFO rule.
        if len(self.oxygen_pipeline) == 0:
            return "🔒 SYSTEM STATUS: All oxygen slots are empty and secure."
        
        allocated_payload = self.oxygen_pipeline.pop() # LIFO: Pop from the absolute top/end
        return f"💨 ALLOCATED IMMEDIATELY -> Oxygen Cylinder Issued to: {allocated_payload['name']} (SpO2: {allocated_payload['spo2']}% Check)"

    def get_waiting_count(self):
        return len(self.oxygen_pipeline)

def run_oxygen_vault_simulation():
    print("🚀 Initiating Sudhir's Emergency Oxygen LIFO Stack Engine [Day 23]...\n")
    
    # 1. INITIALIZE: Creation of the oxygen stack buffer
    oxygen_vault = EmergencyOxygenStackBuffer()
    
    # 2. PUSH OPERATIONS: 3 live patients arriving in a queue, one after another.
    oxygen_vault.admit_critical_patient("Rahul Sharma (Mova)", 88)
    time.sleep(0.3) # Network Delay Simulation
    oxygen_vault.admit_critical_patient("Pooja Mishra (Tatibandh)", 85)
    time.sleep(0.3)
    oxygen_vault.admit_critical_patient("Amit Khan (Amleshwar)", 79) # This is the very last and the most serious one!
    
    print("-" * 75)
    print(f"📊 Total critical patients waiting in LIFO buffer: {oxygen_vault.get_waiting_count()}")
    print("-" * 75)
    
    # 3. POP OPERATIONS (LIFO Allocation): The person at the very end getting the life-saving slot first.
    start_time = time.perf_counter()
    
    print("\n🎧 Processing Immediate Life-Saving Dispatches (LIFO Stack Execution):")
    print(oxygen_vault.allocate_immediate_cylinder()) # Amit Khan, who arrived last, will get the first cylinder!
    print(oxygen_vault.allocate_immediate_cylinder()) # Then Pooja Mishra will get it.
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print("-" * 75)
    print(f"🔢 Remaining patients in backup buffer: {oxygen_vault.get_waiting_count()}")
    print(f"⚡ Stack Allocation Processing Duration: {duration:.4f} ms")
    print(f"📊 Computational Complexity Matrix    : O(1) - Constant Time Speed")
    print("-" * 75)
    print("\n🎉 Emergency oxygen LIFO stack engine executed with 100% computational safety!")

if __name__ == "__main__":
    run_oxygen_vault_simulation()