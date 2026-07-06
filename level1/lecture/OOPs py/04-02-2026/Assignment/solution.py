class UltimateDataScienceBatch:
    
    def __init__(self, batch_id):
        self.batch_id = batch_id
        self.students = []

    def add_student(self, name, email):
        # Store student details in a dictionary
        details = {"name": name, "email": email}
        self.students.append(details)
        print("Added " + name + " to " + self.batch_id)

    def print_student_names(self):
        print("Student list for " + self.batch_id + ":")
        for student in self.students:
            print("- " + student["name"])

# --- Using the Objects ---

# Create Batch 1.0
b1 = UltimateDataScienceBatch("Batch 1.0")
b1.add_student("krish", "krish@123.com")
b1.add_student("adarsh", "adarsh@123.com")

# Create Batch 2.0
b2 = UltimateDataScienceBatch("Batch 2.0")
b2.add_student("ziad", "z@gmail.com")

b1.print_student_names()
b2.print_student_names()