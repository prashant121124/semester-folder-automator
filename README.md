# semester-folder-automator
SEMESTER FOLDER AUTOMATOR & WORKSPACE SETUP GUIDE
OVERVIEW AND PURPOSE
Welcome to the Semester Folder Automator. As a university student, balancing a heavy academic course load with demanding extracurricular responsibilities can make digital organization incredibly difficult. When a new term starts, your computer desktop often becomes cluttered with random documents, stray assignments, and miscellaneous club files.

This lightweight Python script is designed to solve that problem instantly. Instead of spending your valuable time right-clicking, creating a "New Folder," renaming it, and then repeating that process dozens of times for every single subject, lab, and club project, this script does all the heavy lifting in less than a second. It sets up a perfectly standardized, highly organized digital workspace so you can start your semester off right.

HOW THE SCRIPT WORKS BEHIND THE SCENES
This program uses Python's built-in "os" (operating system) module. This means the script communicates directly with your computer's file system.

It uses a special command called "os.makedirs". The best part about this command is that it includes a safety feature called "exist_ok=True". This means that if you accidentally run the program twice, or if you already have a folder with the same name, the script will simply skip it. It will never overwrite your existing work, delete your files, or crash the program. It only creates what is missing.

OPENING YOUR COMMAND LINE
If you are on Windows, press the Windows key, type "cmd", and hit Enter to open the Command Prompt. If you are on a Mac, open the "Terminal" application.

RUNNING THE AUTOMATOR
Now, simply tell Python to run your file by typing:
python semester_setup.py
Then press Enter. The script will wake up and start asking you questions.

UNDERSTANDING THE PROMPTS
When the script runs, it will pause and ask you for two pieces of information:

"Enter the semester name:"
This is the master folder where everything else will live. You can name it something like "VIT_Semester_6" or "Fall_2026". If you are in a rush and just press Enter without typing anything, the script won't break; it will simply name the folder "Semester_A" by default.

"Enter your subjects separated by commas:"
This is where you list all the classes you are taking. The commas are very important because they tell the script where one class ends and the next one begins.
Example input: Machine Learning, Data Structures, Applied Statistics

THE FINAL FOLDER STRUCTURE
Once you press Enter after typing your subjects, the script will instantly build out your entire workspace. Here is exactly what it will look like on your computer:

[Your Main Semester Folder]
|
|-- [Your First Subject]
|     |-- Assignments
|     |-- Lab_Manuals
|     |-- Notes
|     |-- Projects
|
|-- [Your Second Subject]
|     |-- Assignments
|     |-- Lab_Manuals
|     |-- Notes
|     |-- Projects
|
|-- Extracurriculars
|-- CLUB WORK
|-- Posters_and_Designs
|-- Recruitment_Data

HOW TO CUSTOMIZE THE SCRIPT FOR YOUR EXACT NEEDS
The best part about having this code in Notepad is that you can easily edit it to fit your personal workflow.

CUSTOMIZING YOUR ACADEMIC FOLDERS:
Scroll down in the code until you find this line:
subfolders = ["Notes", "Assignments", "Projects", "Lab_Manuals"]
If you want a folder for past exams, simply add it to the list inside the brackets with quotation marks, like this:
subfolders = ["Notes", "Assignments", "Projects", "Lab_Manuals", "Past_Papers"]

CUSTOMIZING YOUR CLUB WORKSPACE:
The script automatically builds a dedicated area for your extracurriculars. Keeping your academic coursework completely separated from your club management is highly recommended.

If you want to tailor this section, find the lines at the bottom of the code that mention "Extracurriculars" and "CLUB WORK". You can rename "CLUB WORK" directly to your specific club's name, such as "PHOTOGRAPHY CLUB".
