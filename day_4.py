#!/usr/bin/python3
"""program to calculate the grade of a student based on their score in an exam"""

def calculate_grade(score):
	# if condition
	if score < 0 or score > 100:  # Validate score
		return "Invalid score. Please enter a score between 0 and 100."
	
	# elif (other conditions)
	elif score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"

	# else condition
	else:
        return "F"


# Getting user input and validating it
while True:
    try:
        score = float(input("Enter the student's score: "))
        break  # Exits the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculating and displaying the grade
grade = calculate_grade(score)
print(f"The student's grade is: {grade}")
