def add_student(students, name):
    students[name] = set()

def print_student(students, name):
    if name not in students:
        print(f"{name}: does not exist in the database")
    else:
        print(f"{name}:")
        total_score = 0
        for course in students[name]:
            print(f" {course[0]} ({course[1]}) ")
            total_score += course[1]
        try:
            average_grade = total_score/len(students[name])
            print(f" average grade : {average_grade:.2f}")
        except ZeroDivisionError:
            print(" no completed courses")

def add_course(students, name, course:tuple):
    if course[1] == 0:
        return 0
    students[name].add(course)

def summary(students):
    print(f"students {len(students)}")
    most_courses = 0
    most_courses_students = []
    best_average = 0
    best_average_students = []
    for name in students:
        total_score = 0
        for course in students[name]:
            total_score += course[1]
        if len(students[name]) > most_courses:
            most_courses_students = [name]
            most_courses = len(students[name])
        elif len(students[name]) == most_courses:
            most_courses_students.append(name)
        try:
            average_grade = total_score/len(students[name])
            if average_grade > best_average:
                best_average_students = [name]
                best_average = average_grade
            elif average_grade == best_average:
                best_average_students.append(name)
        except ZeroDivisionError:
            pass
    print(f"most courses completed: {most_courses}, students: {most_courses_students}")
    print(f"best average grade: {best_average:.2f}, students: {best_average_students}")


if __name__ == "__main__":
    students = {}
    add_student(students,"Peter")
    add_student(students,"Eliza")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Introduction to Art", 5))
    add_course(students, "Peter", ("Introduction to Music", 2))
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Andy")
    summary(students)
    
    
    




    

    
    
    
    
