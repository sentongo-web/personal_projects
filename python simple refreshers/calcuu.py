print("STUDENTS GRADE CALCULATOR")
# Function to calculate the average grade for a student
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

# Function to display the average grade for each student and the overall average grade for the class
def display_results(average_grades):
    print("\n=== Student Grade Calculator ===")
    for i, avg_grade in enumerate(average_grades):
        print(f"\nStudent {i + 1}:")
        print(f"Average grade: {avg_grade:.2f}")
    overall_average = sum(average_grades) / len(average_grades)
    print(f"\nOverall Average Grade for the class: {overall_average:.2f}")

# Main function
def main():
    num_students = int(input("Enter the number of students: "))
    average_grades = []

    for i in range(num_students):
        grades = input(f"\nEnter grades for Student {i + 1} separated by spaces: ").split()
        grades = [int(grade) for grade in grades]  # Convert grades to integers
        avg_grade = calculate_average(grades)
        average_grades.append(avg_grade)
        print(f"Average grade for Student {i + 1}: {avg_grade:.2f}")

    display_results(average_grades)

if __name__ == "__main__":
    main()
