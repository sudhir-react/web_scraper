import time
from collections import deque

class EmergencyBloodBankQueue:
    def __init__(self):
        # Emergency Blood Buffer (FIFO Queue)
        self.blood_pipeline = deque()

    def register_patient_request(self, patient_name, blood_group):
        # Logging the patient's live request into the queue.
        print(f"🚨 ALERT: Incoming emergency request for [{blood_group}] -> Patient: '{patient_name}'")
        self.blood_pipeline.append({"name": patient_name, "blood": blood_group})

    def dispatch_blood_unit(self):
        # Issuing a blood unit to the first patient to arrive, in accordance with the FIFO rule.
        if len(self.blood_pipeline) == 0:
            return "🔒 SYSTEM STATUS: No pending critical requests in the pipeline."
        
        dispatched_payload = self.blood_pipeline.popleft() # FIFO: Pop from the left side
        return f"🩸 DISPATCHED SUCCESSFULLY -> Blood Unit Issued to: {dispatched_payload['name']} [{dispatched_payload['blood']}]"

    def get_pending_count(self):
        return len(self.blood_pipeline)

def run_blood_bank_simulation():
    print("🚀 Initiating Sudhir's Emergency Blood Bank FIFO Queue Engine [Day 21]...\n")
    
    # 1. INITIALIZE: Creation of blood bank queue
    blood_vault = EmergencyBloodBankQueue()
    
    # 2. ENQUEUE OPERATIONS: Registering 3 live emergency patients
    blood_vault.register_patient_request("Ramesh Kumar (Raipur)", "O-Negative")
    time.sleep(0.5) # Half a second simulation delay
    blood_vault.register_patient_request("Sita Mishra (Bhilai)", "AB-Positive")
    time.sleep(0.5)
    blood_vault.register_patient_request("John Dee (Durg)", "B-Positive")
    
    print("-" * 75)
    print(f"📊 Total critical patients currently waiting in queue: {blood_vault.get_pending_count()}")
    print("-" * 75)
    
    # 3. DEQUEUE OPERATIONS (FIFO Dispatch): Issuing blood units to patients from the queue.
    start_time = time.perf_counter()
    
    print("\n🎧 Processing Emergency Dispatches (FIFO Execution):")
    print(blood_vault.dispatch_blood_unit()) # Ramesh Kumar, who arrives first, will be served first.
    print(blood_vault.dispatch_blood_unit()) # Then Sita Mishra will get it.
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    print("-" * 75)
    print(f"🔢 Remaining patients in backup buffer: {blood_vault.get_pending_count()}")
    print(f"⚡ Queue Dispatch Processing Duration  : {duration:.4f} ms")
    print(f"📊 Computational Complexity            : O(1) - Constant Time Allocation")
    print("-" * 75)
    print("\n🎉 Emergency blood bank FIFO architecture executed with 100% operational safety!")

if __name__ == "__main__":
    run_blood_bank_simulation()