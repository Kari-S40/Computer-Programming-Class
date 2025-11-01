# Lesson 6 – Student Information 

def main():
    # 1) create an empty dictionary to store all students
    student_information = {}

    # 2) add students: use the student's name as the key
    #    each student has: id, gpa, credits-completed, and a list of grades
    student_information["Jim"] = {
        "id": "d1",
        "gpa": 3.0,
        "credits-completed": 27,
        "grades": [80, 90, 100, 90]
    }

    student_information["Sarah"] = {
        "id": "d2",
        "gpa": 3.8,
        "credits-completed": 48,
        "grades": [88, 90, 100]
    }

    student_information["Kari"] = {
        "id": "d3",
        "gpa": 3.2,
        "credits-completed": 30,
        "grades": [100, 80, 90]
    }

    # 3) print a heading announcing the student names
    print("\nList of Students")
    for name in student_information.keys():
        print("-", name)

    # 4) print a heading announcing the accessing of student information
    print("\nStudent Information Using the items() Loop")
    # use \t to space the columns
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    for name, info in student_information.items():
        print(name, "\t", info["id"], "\t", info["gpa"], "\t",
              info["credits-completed"], "\t\t", info["grades"])

    # 5) print a heading announcing removing a student
    print("\nA student has dropped, removing from student registry")
    # use pop() with a default so we avoid KeyError if the name isn’t found
    removed = student_information.pop("Jim", None)
    if removed is not None:
        print("Removed:", "Jim")
    # show the updated dictionary
    print(student_information)

    # 6) print a heading announcing the accessing of GPA information
    print("\nGetting GPA information")
    # use get() to read the GPA for one or more students
    check_names = ["Jim", "Sarah", "Kari"]
    for who in check_names:
        info = student_information.get(who)  # returns the inner dict or None
        if info is not None:
            print("GPA for", who + ":", info.get("gpa", "none"))
        else:
            print("There is no", who, "in the student registry")

    # 7) print a heading announcing clearing the student registry
    print("\nStudents have graduated, clearing the student registry")
    student_information.clear()  # remove all items
    print(student_information)   # should print {}

    # 8) required completion line
    print("\nCompleted by, Kari Shaddinger")


if __name__ == "__main__":
    main()

