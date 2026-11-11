#PROJECT-University & Student Management System
class Person:
    def __init__(self, person_id, name, email):
        self.person_id = int(person_id)
        self.name = name
        self.email = email

    def get_basic_info(self):
        print(f"Name: {self.name} | Person ID: {self.person_id} | Email: {self.email}")


class Student(Person):
    def __init__(self, person_id, name, email):
        super().__init__(person_id, name, email)
        self.enrolled_courses = {}

    def calculate_gpa(self, all_courses):
        total_points = 0.0
        total_credits = 0.0

        for cid, grade in self.enrolled_courses.items():
            if grade is not None and cid in all_courses:
                course_credits = all_courses[cid].credits
                total_points += grade * course_credits
                total_credits += course_credits

        if total_credits == 0:
            return 0.0
        return round(total_points / total_credits, 2)


class Professor(Person):
    def __init__(self, person_id, name, email, department):
        super().__init__(person_id, name, email)
        self.department = department
        self.assigned_courses = []


class Course:
    def __init__(self, course_id, course_name, credits, max_seats):
        self.course_id = int(course_id)
        self.course_name = course_name
        self.credits = float(credits)
        self.max_seats = int(max_seats)
        self.enrolled_students = []
        self.professor_id = None

    def has_available_seats(self):
        return len(self.enrolled_students) < self.max_seats


class UniversityManager:
    def __init__(self):
        self.students = {}
        self.professors = {}
        self.courses = {}

    def add_student(self, student_obj):
        if student_obj.person_id in self.students:
            print("Error: Student ID already exists!")
            return False
        self.students[student_obj.person_id] = student_obj
        print(f"Student '{student_obj.name}' registered successfully.")
        return True

    def add_professor(self, prof_obj):
        if prof_obj.person_id in self.professors:
            print("Error: Professor ID already exists!")
            return False
        self.professors[prof_obj.person_id] = prof_obj
        print(f"Professor '{prof_obj.name}' registered successfully.")
        return True

    def create_course(self, course_obj):
        if course_obj.course_id in self.courses:
            print("Error: Course ID already exists!")
            return False
        self.courses[course_obj.course_id] = course_obj
        print(f"Course '{course_obj.course_name}' created successfully.")
        return True

    def assign_professor(self, prof_id, course_id):
        if prof_id not in self.professors or course_id not in self.courses:
            print("Error: Professor or Course not found.")
            return

        prof = self.professors[prof_id]
        course = self.courses[course_id]

        course.professor_id = prof_id

        if course_id not in prof.assigned_courses:
            prof.assigned_courses.append(course_id)
            print(f"Professor {prof.name} assigned to {course.course_name}.")
        else:
            print("Professor is already assigned to this course.")

    def enroll_student_in_course(self, student_id, course_id):
        if student_id not in self.students or course_id not in self.courses:
            print("Error: Student or Course ID does not exist.")
            return

        student = self.students[student_id]
        course = self.courses[course_id]

        if course_id in student.enrolled_courses:
            print("Error: Student is already enrolled in this course.")
            return

        if not course.has_available_seats():
            print("Enrollment Failed: No seats available in this course.")
            return

        student.enrolled_courses[course_id] = None
        course.enrolled_students.append(student_id)
        print(f"Student {student.name} enrolled in {course.course_name}.")

    def assign_grade(self, student_id, course_id, grade_point):
        if student_id not in self.students:
            print("Error: Student not found.")
            return

        student = self.students[student_id]

        if course_id not in student.enrolled_courses:
            print("Error: Student is not enrolled in this course.")
            return

        student.enrolled_courses[course_id] = float(grade_point)
        print(f"Grade {grade_point} assigned to {student.name} for Course ID {course_id}.")


def main():
    manager = UniversityManager()

    while True:
        print("\n" + "=" * 50)
        print("------- UNIVERSITY & STUDENT MANAGEMENT SYSTEM -------")
        print("=" * 50)
        print("1. Register New Student")
        print("2. Register New Professor")
        print("3. Create New Course")
        print("4. Assign Professor to Course")
        print("5. Enroll Student in Course")
        print("6. Assign Grade to Student")
        print("7. View Student Profile & GPA")
        print("8. Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            sid = int(input("Enter Student ID: ").strip())
            name = input("Enter Student Name: ").strip()
            email = input("Enter Student Email: ").strip()
            student = Student(sid, name, email)
            manager.add_student(student)

        elif choice == "2":
            pid = int(input("Enter Professor ID: ").strip())
            name = input("Enter Professor Name: ").strip()
            email = input("Enter Professor Email: ").strip()
            dept = input("Enter Department: ").strip()
            prof = Professor(pid, name, email, dept)
            manager.add_professor(prof)

        elif choice == "3":
            cid = int(input("Enter Course ID: ").strip())
            cname = input("Enter Course Name: ").strip()
            credits = float(input("Enter Course Credits: ").strip())
            seats = int(input("Enter Max Seats: ").strip())
            course = Course(cid, cname, credits, seats)
            manager.create_course(course)

        elif choice == "4":
            pid = int(input("Enter Professor ID: ").strip())
            cid = int(input("Enter Course ID: ").strip())
            manager.assign_professor(pid, cid)

        elif choice == "5":
            sid = int(input("Enter Student ID: ").strip())
            cid = int(input("Enter Course ID: ").strip())
            manager.enroll_student_in_course(sid, cid)

        elif choice == "6":
            sid = int(input("Enter Student ID: ").strip())
            cid = int(input("Enter Course ID: ").strip())
            grade = float(input("Enter Grade Point (0-10): ").strip())
            manager.assign_grade(sid, cid, grade)

        elif choice == "7":
            sid = int(input("Enter Student ID: ").strip())
            if sid in manager.students:
                student = manager.students[sid]
                print("\n--- STUDENT ACADEMIC REPORT ---")
                student.get_basic_info()
                if not student.enrolled_courses:
                    print("Enrolled Courses: None")
                else:
                    for cid, grade in student.enrolled_courses.items():
                        cname = manager.courses[cid].course_name
                        grade_str = grade if grade is not None else "Pending"
                        print(f"Course: {cname} (ID: {cid}) | Grade: {grade_str}")
                gpa = student.calculate_gpa(manager.courses)
                print(f"Current CGPA: {gpa}")
            else:
                print("Error: Student not found.")

        elif choice == "8":
            print("\nThank you for using the University Management System. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 8.")


if __name__ == "__main__":
    main()
