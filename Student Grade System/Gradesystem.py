student_grade = {
    "MUSKAN": 90,
    "NITIN": 80,
 }

def add_student(name, grade):
    student_grade[name] = grade
    
    print(f"Added {name} with a {grade} ")
    
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f" {name} with marks are updated {grade} ")
        
    else:
        print(f"{name} is not in the list")
        
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been deleted successfully")
     
    else:
        print(f"{name} is not in the list")
        
def display_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name}: {grade}")
    else:
        print("No students in the list.")   
             
def main():
    while True:
        print("\n-----Welcome to Student Grade System-----")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("Enter your choice : ")
        
        if choice == '1':
            name = input("Enter student name =  ")
            grade = input("Enter student grade =  ")
            add_student(name, grade)
            
        elif choice == '2':
            name = input("Enter student name to update =  ")
            grade = input("Enter new grade =  ")
            update_student(name, grade)
            
        elif choice == '3':
            name = input("Enter student name to delete =  ")
            delete_student(name)
            
        elif choice == '4':
            display_all_students()
            
        elif choice == '5':
            print("CLosing the program...")
            break
            
        else:
            print("Invalid choice.")
    
    