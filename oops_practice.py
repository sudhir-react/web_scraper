class BankAccountBlueprint:
    def __init__(self, owner_name, initial_balance):
        self.owner = owner_name
        self.balance = initial_balance

    # The magical money-depositing function
    def deposit_money(self, amount):
        self.balance += amount
        print(f"💰 ${amount:,.2f} deposited successfully to {self.owner}'s safe.")

    def display_balance(self):
        print(f"👤 Account Holder: {self.owner}")
        print(f"💳 Current Vault Balance: ${self.balance:,.2f}")
        print("-" * 45)

def run_bank_simulation():
    print("🚀 Starting Sudhir's Advanced OOPs Practice Session...\n")
    
    # 1. OBJECT CREATION: Creating a live account for Sudhir-ji
    sudhir_account = BankAccountBlueprint("Sudhir Kumar Mishra", 1500)
    
    # 2. DISPLAY INITIAL STATE
    sudhir_account.display_balance()
    
    # 3. TRANSACTION EXECUTION: Crediting a $695 live bonus to the account.
    sudhir_account.deposit_money(695)
    
    # 4. FINAL VALIDATION
    print("\n📊 Updated Financial Status:")
    sudhir_account.display_balance()
    
    print("🎉 OOPs practice variation executed successfully with 100% computational integrity!")

if __name__ == "__main__":
    run_bank_simulation()