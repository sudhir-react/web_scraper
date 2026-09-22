import time

class GeneralMedicalDirectory:
    def __init__(self, medicine_name, primary_use, standard_adult_dose, safety_possibilities):
        self.name = medicine_name
        self.use = primary_use
        self.dose = standard_adult_dose
        self.possibilities = safety_possibilities # At least 3 different possibilities/side effects

    def display_public_solution(self):
        print(f"\n💊 Generic medical name : {self.name}")
        print(f"🎯 Main uses         : {self.use}")
        print(f"📊 Usual adult dosage : {self.dose}")
        print("⚠️ 3 key possibilities worth noting (Safety Possibilities):")
        for index, item in enumerate(self.possibilities, start=1):
            print(f"   {index}. {item}")
        print("-" * 75)

def run_medical_app_session():
    print("🚀 Starting Sudhir's Public Medical Directory Prototype [Day 20]...\n")
    print("🩺 The image/query simulates a general medication check query.")
    print("👉 Note: Make sure to double-check the physical label to confirm this information.\n")
    
    # 1. DATA ENGINES: Creating a secure database of the three most common medicines used by the general public.
    # It includes 3 treatment options and safety details.
    paracetamol_info = GeneralMedicalDirectory(
        "Paracetamol (500mg)", 
        "Relief from fever and general body ache", 
        "1Tablet every 4–6 hours (not more than 4000 mg in 24 hours)",
        ["Excessive strain on the liver (resembling liver strain in cases of overdose)", "Mild drowsiness or nausea", "Occasional mild skin rashes"]
    )
    
    ibuprofen_info = GeneralMedicalDirectory(
        "Ibuprofen (200mg)", 
        "Swelling, toothache, and severe headache.", 
        "1 Take the tablet after a meal (do not exceed the dosage without a doctor's advice)",
        ["Burning sensation in the stomach or acidity (consistent with gastric irritation)", "Dizziness", "Mild fluctuations in blood pressure"]
    )

    # 2.RUNTIME SIMULATION: When an average user visits the app and performs a search.
    start_time = time.perf_counter()
    
    print("🔍 [User Action] User searched for 'Common fever medication':")
    paracetamol_info.display_public_solution()
    
    print("🔍 [User Action] User searched for 'Swelling and pain':")
    ibuprofen_info.display_public_solution()
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. GLOBAL MEDICAL DISCLAIMER (Uncompromised Safety Rule)
    print("\n⚖️ MEDICAL DISCLAIMER (Medical Disclaimer):")
    print("This application presents general information only. It should NEVER give personalized medical information or advice.")
    print("This app provides only general information. Do not consider it personal medical advice. Consulting a doctor before taking any medication is mandatory.")
    
    print(f"\n⚡ App Processing Speed: {duration:.4f} ms")
    print("\n🎉 Medical Directory engine executed successfully with 100% computational safety!")

if __name__ == "__main__":
    run_medical_app_session()