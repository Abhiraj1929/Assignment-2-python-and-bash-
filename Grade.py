def check_grade():
    try:
        score = int(input("Enter the student's score: "))

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"The grade for a score of {score} is: {grade}")

    except ValueError:
        print("Invalid input. Please enter a numerical score.")

if __name__ == "__main__":
    check_grade()