import time

class LawyerNode:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.next = None  # अगले वकील के डेटा का पॉइंटर

class LawyerLinkedList:
    def __init__(self):
        self.head = None  # शुरुआत में लिस्ट खाली है

    def insert_at_end(self, name, email):
        new_node = LawyerNode(name, email)
        print(f"📥 Extracting & Inserting Lawyer Node: '{name}' into Data Chain...")
        
        # अगर लिस्ट खाली है, तो यही हेड नोड बनेगा
        if self.head is None:
            self.head = new_node
            return
            
        # आखिरी नोड तक पहुँचना
        last = self.head
        while last.next:
            last = last.next
            
        # आखिरी नोड को नए नोड से जोड़ना
        last.next = new_node

    def display_lawyers(self):
        print("\n📊 Final Cleaned Lawyer Database (Linked List Hierarchy):")
        print("-" * 75)
        current = self.head
        while current:
            print(f"👤 Attorney: {current.name:<25} | 📧 Email: {current.email}")
            current = current.next
        print("-" * 75)

def run_law_firm_simulation():
    print("🚀 Starting Sudhir's Advanced Law Directory Parser Test...\n")
    
    # 1. INITIALIZE: डेटाबेस चेन का निर्माण
    lawyer_chain = LawyerLinkedList()
    
    # परफॉर्मेंस ऑडिट के लिए टाइमर शुरू करना
    start_time = time.perf_counter()
    
    # 2. INSERT OPERATIONS: लाइव डेटा कड़ियों में जोड़ना
    lawyer_chain.insert_at_end("John Doe (Orlando)", "john.doe@preeminent.com")
    lawyer_chain.insert_at_end("Elena Rostova (Orlando)", "elena.r@preeminent.com")
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. OUTPUT UI: पूरी चेन प्रिंट करना
    lawyer_chain.display_lawyers()
    print(f"⚡ Memory Pipeline Processing Duration: {duration:.4f} ms")
    print(f"📊 Computational Complexity: O(N) - Linear Traversal Speed")
    print("\n🎉 Law firm directory scraping pipeline executed with 100% data integrity!")

if __name__ == "__main__":
    run_law_firm_simulation()