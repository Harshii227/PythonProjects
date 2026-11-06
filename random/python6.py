# Save notes
with open("student_notes.txt", "w") as file:
    file.write("Python Day 13\n")
    file.write("Learning File Handling")

# Read notes
with open("student_notes.txt", "r") as file:
    content = file.read()
    print(content)