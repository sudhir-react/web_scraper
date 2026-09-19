class NodeBlueprint:
    # Creating an independent node using OOPs.
    def __init__(self, data_value):
        self.data = data_value     # Container data
        self.next = None           # Next box address (initially empty)

def display_linked_list(head_node):
    print("📊 Traversing Linked List Architecture:")
    print("-" * 50)
    current = head_node
    
    # Keep moving forward as long as train coaches keep coming along.
    while current is not None:
        print(f"📦 [Data: {current.data}]", end=" ➡️ ")
        current = current.next  # Leaping to the next episode
        
    print("🔒 [End of Memory Chain (None)]")
    print("-" * 50)

def run_linked_list_session():
    print("🚀 Starting Sudhir's Advanced Linked List Node Simulation [Day 17]...\n")
    
    # 1.OBJECT CREATION: Creating 3 independent train carriages (nodes)
    first_node = NodeBlueprint("Upwork Job #1 ($50)")
    second_node = NodeBlueprint("GitHub Push Success")
    third_node = NodeBlueprint("SQLite Database Active")
    
    # 2. LINKING OPERATIONS: Connecting the containers to each other with links.
    # Connected the first box to the second, and the second to the third.
    first_node.next = second_node
    second_node.next = third_node
    
    # 3. EXECUTION: Scanning the entire chain starting from the head node (train engine)
    display_linked_list(first_node)
    
    print("\n🎉 Linked List memory train executed successfully with 100% computational integrity!")

if __name__ == "__main__":
    run_linked_list_session()