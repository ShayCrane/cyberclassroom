# 08/2023
# Random Selection CLI App for Team Assignment
# This script allows users to input student names and randomly assign them to three teams. . 
# I used it for the purposes of engaging my students with the project from the very beginning. It prompts for input, providing a visual experience students can follow. The output is sent to a .txt file and saved to device files. 
# Acknowledgments: This curriculum project was assisted by Copilot for generating initial ideas and refining the project's learning objectives.


# randomSelectionCLIapp.py
import random
import time

# This script collects student names from the user and assigns them to three teams.
def get_names():
    print("\n👋 Welcome to the Team Assigner!")
    print("Please enter student names one at a time.")
    print("When you're done, just press Enter on an empty line.\n")


# Collect names from the user
    names = []
    while True:
        name = input("Enter student name: ").strip()
        if not name:
            break
        names.append(name)


# Check if the user has entered at least 3 names
    if len(names) < 3:
        print("\n⚠️ You need at least 3 names to form 3 teams.")
        exit(1)


# If the user has entered names, print the list
    return names

# Assign names to teams
# The function assigns students to three teams, ensuring each team has an equal number of members.
def assign_teams(names):
    total_names = len(names)
    base_team_size = total_names // 3
    remainder = total_names % 3

# Prepare output lines for display and file saving
    print("\n📊 Team Assignment Summary:\n")
    output_lines = []
    output_lines.append(f"🎯 Total students: {total_names}")
    output_lines.append(f"📦 Each team will have {base_team_size} members.")
    if remainder:
        output_lines.append(f"🧮 Remainder: {remainder} student(s) will not be assigned to a team.\n")

# Shuffle the names and assign them to teams
    print("\n🔀 Shuffling names and assigning to teams...\n")
    random.shuffle(names)
    teams = {1: [], 2: [], 3: []}

# Assign names to teams
    print("📋 Team Assignments:\n")
    index = 0
    for team_num in range(1, 4):
        output_lines.append(f"\n🚀 Assigning to Team #{team_num}...\n")
        
        for _ in range(base_team_size):
            name = names[index]
            teams[team_num].append(name)
            print(f"Team #{team_num} <- {name}")
            output_lines.append(f"Team #{team_num} <- {name}")
            time.sleep(0.5)
            index += 1
        print("-" * 40)
        output_lines.append("-" * 40)

# Assign any remaining students to the unassigned list
    print("\n🎒 Unassigned students (due to uneven count):")
    if remainder:
        print("\n🎒 Unassigned students (due to uneven count):")
        output_lines.append("\n🎒 Unassigned students (due to uneven count):")
        for i in range(remainder):
            print(f"- {names[index]}")
            output_lines.append(f"- {names[index]}")
            index += 1

    # Save to file
    with open("team_assignments.txt", "w") as f:
        f.write("\n".join(output_lines))

    print("\n✅ Team assignments saved to 'team_assignments.txt'.")

# Main function to run the script
# This function orchestrates the flow of the application.
if __name__ == "__main__":
    student_names = get_names()
    assign_teams(student_names)


exit
