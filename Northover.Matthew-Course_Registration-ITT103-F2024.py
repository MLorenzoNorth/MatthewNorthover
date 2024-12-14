"""""
Student Course Registration System

This program implements a simple course registration system that allows administrators to manage courses and student enrollments.
It provides functionalities to add courses, register students, enroll students in courses, process payments, and check student balances.

Classes:
- Course: Represents a course with an ID, name, and fee.
- Student: Represents a student with an ID, name, email, a list of enrolled courses, and a balance.
- RegistrationSystem: Manages the overall registration process, including adding courses, registering students, enrolling students in courses,
  calculating payments, and displaying information about courses and students.

Methods:
- add_course(course_id, name, fee): Adds a new course to the system.
- register_student(student_id, name, email): Registers a new student in the system.
- enroll_in_course(student_id, course_id): Enrolls a student in a specified course.
- calculate_payment(student_id, payment_amount): Processes a payment for a student.
- check_student_balance(student_id): Displays the current balance for a student.
- show_courses(): Displays all available courses.
- show_registered_students(): Displays all registered students.
- show_students_in_course(course_id): Displays all students enrolled in a specified course.

Usage:
1. Run the program.
2. Follow the on-screen menu to perform various operations related to course and student management.
"""

class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0.0

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.fee
            print(f"Enrolled in {course.name}. Total balance is now {self.balance:.2f}.")
        else:
            print("Already enrolled in this course.")

    def get_total_fee(self):
        return sum(course.fee for course in self.courses)


class RegistrationSystem:
    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course_id, name, fee):
        if course_id in self.courses:
            raise ValueError("Course with this ID already exists.")
        self.courses[course_id] = Course(course_id, name, fee)
        print(f"Course {name} added successfully.")

    def register_student(self, student_id, name, email):
        if student_id in self.students:
            raise ValueError("Student with this ID already exists.")
        self.students[student_id] = Student(student_id, name, email)
        print(f"Student {name} registered successfully.")

    def enroll_in_course(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_id not in self.courses:
            raise ValueError("Course not found.")
        self.students[student_id].enroll(self.courses[course_id])

    def calculate_payment(self, student_id, payment_amount):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        if payment_amount < 0.4 * student.balance:
            raise ValueError("Minimum payment is 40% of the balance.")
        student.balance -= payment_amount
        print(f"Payment of {payment_amount:.2f} received. Outstanding balance is now {student.balance:.2f}.")

    def check_student_balance(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        print(f"Balance for {student.name}: {student.balance:.2f}")

    def show_courses(self):
        print("Available Courses:")
        for course in self.courses.values():
            print(f"ID: {course.course_id}, Name: {course.name}, Fee: {course.fee:.2f}")

    def show_registered_students(self):
        print("Registered Students:")
        for student in self.students.values():
            print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

    def show_students_in_course(self, course_id):
        if course_id not in self.courses:
            raise ValueError("Course not found.")
        print(f"Students enrolled in {self.courses[course_id].name}:")
        for student in self.students.values():
            if self.courses[course_id] in student.courses:
                print(f"ID: {student.student_id}, Name: {student.name}")


def main():
    system = RegistrationSystem()

    while True:
        print("\n--- Registration System Menu ---")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll in Course")
        print("4. Make Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in Course")
        print("9. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == '1':
                course_id = input("Enter Course ID: ")
                name = input("Enter Course Name: ")
                fee = float(input("Enter Course Fee: "))
                system.add_course(course_id, name, fee)
            elif choice == '2':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                email = input("Enter Student Email: ")
                system.register_student(student_id, name, email)
            elif choice == '3':
                student_id = input("Enter Student ID: ")
                course_id = input("Enter Course ID: ")
                system.enroll_in_course(student_id, course_id)
            elif choice == '4':
                student_id = input("Enter Student ID: ")
                payment_amount = float(input("Enter Payment Amount: "))
                system.calculate_payment(student_id, payment_amount)
            elif choice == '5':
                student_id = input("Enter Student ID: ")
                system.check_student_balance(student_id)
            elif choice == '6':
                system.show_courses()
            elif choice == '7':
                system.show_registered_students()
            elif choice == '8':
                course_id = input("Enter Course ID: ")
                system.show_students_in_course(course_id)
            elif choice == '9':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()