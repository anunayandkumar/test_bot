import json
import datetime
import pytz

with open("elective.json", 'r') as file1:
    elective_data = json.load(file1)

with open("core.json", 'r') as file2:
    core_data = json.load(file2)

user_roll_number = int(input("Enter Roll Number: "))

roll_numbers_elective = []
roll_numbers_core = []
elective_sections = []
core_section = []

for entry in elective_data:
    if entry["Roll No"] == user_roll_number:
        roll_numbers_elective.append(entry["Roll No"])
        elective_sections.append(entry["Elective Section"])

for entry in core_data:
    if entry["Roll No"] == user_roll_number:
        roll_numbers_core.append(entry["Roll No"])
        core_section.append(entry["Core Section"])


if roll_numbers_elective:
    for i in range(len(roll_numbers_elective)):
        print(f"Roll Number: {roll_numbers_elective[i]}, Elective Section: {elective_sections[i]}")
    if roll_numbers_core:
        for i in range(len(roll_numbers_core)):
            print(f"Roll Number: {roll_numbers_core[i]}, Core Section: {core_section[i]}")






desired_timezone = pytz.timezone('Asia/Kolkata')

current_date = datetime.datetime.now(desired_timezone)

day_of_week = current_date.strftime("%A")

print(f"Today is {day_of_week}.")

