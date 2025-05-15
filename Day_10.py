# Step 1: Try reading existing journal entries (if any)
try:
    with open("journal.txt", "r") as file:
        print("📖 Previous Journal Entries:")
        print("----------------------------")
        print(file.read())
except FileNotFoundError:
    print("📁 No previous journal found. Create a new one...")

# Step 2: Write a new journal entry
new_entry = input("\n🖊️ Write today's journal entry: ")

with open("journal.txt", "a") as file:
    file.write(new_entry + "\n")
    print("✅ Your entry has been saved.")

# Step 3: Display only the first line using readline
with open("journal.txt", "r") as file:
    first_line = file.readline()
    print("\n🔹 First Entry in Journal:")
    print(first_line)

with open("journal.txt", "r") as file:
    print(file.read())

def create_journal():
    with open("diary.txt", "a") as file:
        line = input("write your journal entry: ")
        file.write(line + "\n")
        print("new entry added")
        
def read_journal():
    with open("diary.txt", "r") as file:
        print(file.read())
        print("all entries read")
if create_journal():
    print("journal created")
else:
    print("journal not created")
create_journal()
print("journal need to be read")
read_journal()



import csv

try:
    # Try to open the file in read mode
    with open("stats.csv", newline='') as file:
        reader = csv.reader(file)
        print("📄 Reading existing file:")
        for row in reader:
            print(row)

except FileNotFoundError:
    # If the file doesn't exist, create it
    print("⚠️ File not found. Creating 'stats.csv'...")
    with open("stats.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])
        writer.writerow(["Amit", 95])
        writer.writerow(["Neha", 89])
        writer.writerow(["Raj", 92])
        writer.writerow(["Priya", 88])
    print("✅ File created and data written.")



import json
data = {"name": "Hero", "level": 5, "score": 300}
data = {"name": "villan", "level": 9, "score": 900}
with open("player.json", "w") as file:
    json.dump(data, file)

with open("player.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"],[loaded_data["level"]], loaded_data["score"])

