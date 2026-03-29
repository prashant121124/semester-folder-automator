import os

def create_semester_folders():
    print("--- Semester Folder Automator ---")
    
    # 1. Get the main folder name from the user
    semester_name = input("Enter the semester name (e.g., VIT_Semester): ").strip()
    
    # Fallback just in case you hit Enter without typing anything
    if not semester_name:
        semester_name = "Semester_A"
        
    # 2. Get the list of subjects
    print("\nEnter your subjects separated by commas.")
    print("(Example: AI_ML, Data_Structures, Applied_Statistics)")
    subjects_input = input("Subjects: ").strip()
    
    if not subjects_input:
        print("No subjects entered. Exiting program.")
        return

    # Split the comma-separated text into a clean Python list
    subjects = [sub.strip() for sub in subjects_input.split(",")]
    
    # 3. Define the standard subfolders every class needs
    subfolders = ["Notes", "Assignments", "Projects", "Lab_Manuals"]
    
    # 4. Create the main semester directory
    # exist_ok=True prevents the program from crashing if the folder already exists
    os.makedirs(semester_name, exist_ok=True)
    print(f"\n[+] Created main folder: {semester_name}/")

    # 5. Loop through each subject and build out the directory tree
    for subject in subjects:
        subject_path = os.path.join(semester_name, subject)
        
        for sub in subfolders:
            # os.path.join automatically uses the correct slashes (\ or /) for your OS
            full_path = os.path.join(subject_path, sub)
            os.makedirs(full_path, exist_ok=True)
            
        print(f"  ├── Created structured folder for: {subject}")

    # 6. Automate a dedicated workspace for club activities
    club_path = os.path.join(semester_name, "Extracurriculars", "CLUB WORK")
    os.makedirs(os.path.join(club_path, "Posters_and_Designs"), exist_ok=True)
    os.makedirs(os.path.join(club_path, "Recruitment_Data"), exist_ok=True)
    print("  ├── Created structured folder for: Extracurriculars/STATS-O-LOCKED")

    print("\nSuccess! Your semester workspace is completely set up.")

if __name__ == "__main__":
    create_semester_folders()
    