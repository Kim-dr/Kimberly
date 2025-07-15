class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def total_marks(self):
        return sum(self.subjects.values())

    def average_marks(self):
        return self.total_marks() / len(self.subjects) if self.subjects else 0

    def show_report(self):
        print(f"\nReport Card for {self.name}")
        for subject, marks in self.subjects.items():
            print(f"{subject}: {marks}")
        print(f"Total: {self.total_marks()}")
        print(f"Average: {self.average_marks():.2f}")

def main():
    print("📘 Student Results System")
    name = input("Enter student's name: ")
    student = Student(name)

    while True:
        subject = input("Enter subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            student.add_subject(subject, marks)
        except ValueError:
            print("Please enter a valid number for marks.")

    student.show_report()

main()