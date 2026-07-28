import json

FILE_NAME = "student_directory.json"


# -----------------------------
# Load Data
# -----------------------------

try:
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = {"students": []}


# -----------------------------
# Save Data
# -----------------------------

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# Input Validation
# -----------------------------

def get_name():
    while True:
        name = input("\nEnter Student Name: ").strip()

        if not name:
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name cannot contain numbers or special characters.")
        else:
            return name


def get_mark():
    while True:
        try:
            mark = int(input("\nEnter Student Mark: "))

            if 0 <= mark <= 100:
                return mark

            print("Mark must be between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")


def get_yes_no(message):
    while True:
        choice = input(message).strip().lower()

        if choice in ("y", "n"):
            return choice

        print("Please enter only y or n.")


# -----------------------------
# Main Menu
# -----------------------------

def main_menu():
    print("\n======== Student Grade Manager ========\n")
    print("1. Add Student")
    print("2. View Student Record")
    print("3. Search Student")
    print("4. Find Highest Mark")
    print("5. Delete Student Record")
    print("6. Exit\n")


# -----------------------------
# Add Student
# -----------------------------

def add_student():
    while True:
        name = get_name()

        # Prevent duplicate names
        duplicate = False

        for student in data["students"]:
            if student["name"].lower() == name.lower():
                duplicate = True
                break

        if duplicate:
            print("Student already exists.")

        else:
            mark = get_mark()

            data["students"].append({
                "name": name,
                "mark": mark
            })

            save_data()
            print("\nStudent added successfully.")

        if get_yes_no("\nAdd another student? (y/n): ") == "n":
            return

# -----------------------------
# View Student Records
# -----------------------------

def student_record():
    if not data["students"]:
        print("\nNo student records available.")
        return

    print("\n======= Student Records =======\n")
    print(f"{'Name':<20}{'Mark'}")
    print("-" * 25)

    for student in data["students"]:
        print(f"{student['name']:<20}{student['mark']}")


# -----------------------------
# Search By Name
# -----------------------------

def search_by_name():
    while True:
        if not data["students"]:
            print("\nNo student records available.")
            return

        searched_name = get_name()

        found_students = []

        for student in data["students"]:
            if searched_name.lower() == student["name"].lower():
                found_students.append(student)

        if found_students:
            print("\nStudents Found:\n")
            print(f"{'Name':<20}{'Mark'}")
            print("-" * 25)

            for student in found_students:
                print(f"{student['name']:<20}{student['mark']}")

        else:
            print("\nNo student found.")

        if get_yes_no("\nSearch again? (y/n): ") == "n":
            return


# -----------------------------
# Search By Mark
# -----------------------------

def search_by_mark():
    while True:
        if not data["students"]:
            print("\nNo student records available.")
            return

        searched_mark = get_mark()

        found_students = []

        for student in data["students"]:
            if searched_mark == student["mark"]:
                found_students.append(student)

        if found_students:
            print("\nStudents Found:\n")
            print(f"{'Name':<20}{'Mark'}")
            print("-" * 25)

            for student in found_students:
                print(f"{student['name']:<20}{student['mark']}")

        else:
            print("\nNo student found.")

        if get_yes_no("\nSearch again? (y/n): ") == "n":
            return


# -----------------------------
# Search Menu
# -----------------------------

def search_student():
    while True:
        print("\n======= Search Student =======")
        print("1. Search By Name")
        print("2. Search By Mark")
        print("3. Back To Main Menu")

        try:
            selected_option = int(
                input("\nSelect an option: ")
            )

            if selected_option == 1:
                search_by_name()

            elif selected_option == 2:
                search_by_mark()

            elif selected_option == 3:
                return

            else:
                print("Input is not within range.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# -----------------------------
# Find Highest Mark
# -----------------------------

def find_highest_mark():
    if not data["students"]:
        print("\nNo student records available.")
        return

    highest_mark = max(student["mark"] for student in data["students"])

    highest_students = [
        student
        for student in data["students"]
        if student["mark"] == highest_mark
    ]

    print(f"\nHighest Mark: {highest_mark}\n")
    print(f"{'Name':<20}{'Mark'}")
    print("-" * 25)

    for student in highest_students:
        print(f"{student['name']:<20}{student['mark']}")


# -----------------------------
# Delete By Name
# -----------------------------

def delete_by_name():
    while True:
        if not data["students"]:
            print("\nNo student records available.")
            return

        name = get_name()

        deleted = False

        for student in data["students"][:]:
            if student["name"].lower() == name.lower():
                data["students"].remove(student)
                deleted = True

        if deleted:
            save_data()
            print("\nStudent deleted successfully.")
        else:
            print("\nNo student found.")

        if get_yes_no("\nDelete another student? (y/n): ") == "n":
            return


# -----------------------------
# Delete By Mark
# -----------------------------

def delete_by_mark():
    while True:
        if not data["students"]:
            print("\nNo student records available.")
            return

        mark = get_mark()

        matched_students = [
            student
            for student in data["students"]
            if student["mark"] == mark
        ]

        if not matched_students:
            print("\nNo student found.")

        else:
            print("\nStudents with this mark:\n")
            print(f"{'No.':<5}{'Name':<20}{'Mark'}")
            print("-" * 30)

            for i, student in enumerate(matched_students, start=1):
                print(f"{i:<5}{student['name']:<20}{student['mark']}")

            while True:
                try:
                    choice = int(
                        input("\nEnter serial number to delete: ")
                    )

                    if 1 <= choice <= len(matched_students):
                        data["students"].remove(
                            matched_students[choice - 1]
                        )
                        save_data()
                        print("\nStudent deleted successfully.")
                        break

                    print("Invalid range.")

                except ValueError:
                    print("Please enter numbers only.")

        if get_yes_no("\nDelete another student? (y/n): ") == "n":
            return


# -----------------------------
# Delete Menu
# -----------------------------

def delete_student_record():
    while True:
        print("\n======= Delete Student =======")
        print("1. Delete By Name")
        print("2. Delete By Mark")
        print("3. Back To Main Menu")

        try:
            selected_option = int(
                input("\nSelect an option: ")
            )

            if selected_option == 1:
                delete_by_name()

            elif selected_option == 2:
                delete_by_mark()

            elif selected_option == 3:
                return

            else:
                print("Input is not within range.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# -----------------------------
# Main Function
# -----------------------------

def main():
    while True:
        main_menu()

        try:
            selected_option = int(input("Select an option: "))

            if selected_option == 1:
                add_student()

            elif selected_option == 2:
                student_record()

            elif selected_option == 3:
                search_student()

            elif selected_option == 4:
                find_highest_mark()

            elif selected_option == 5:
                delete_student_record()

            elif selected_option == 6:
                print("\nThank you for using Student Grade Manager!")
                break

            else:
                print("Input is not within range.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()