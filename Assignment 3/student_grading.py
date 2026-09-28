''' This program will calculate a student's grade based on scores from the user's input and the weights for each category. '''

# Weight values for exam, assignment, and quiz.
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# Input the value for the exams
midterm_exam_grade = float(input("Enter midterm exam grade (0 - 100): "))
final_exam_grade = float(input("Enter final exam grade (0 - 100): "))
exam_range = True if (midterm_exam_grade >= 0 and midterm_exam_grade <= 100) and (final_exam_grade >=0 and final_exam_grade <= 100) else False

# Calculatge exam grade average
exam_grade_average = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT

# Input the values for the assignments
assignment_one_grade = float(input("Enter assignment one grade (0 - 30): "))
assignment_two_grade = float(input("Enter assignment two grade (0 - 30): "))
assignment_range = True if (assignment_one_grade >= 0 and assignment_one_grade <= 30) and (assignment_two_grade >= 0 and assignment_two_grade <= 30) else False

# Calculate assignment grade average
assignment_grade_average = (((assignment_one_grade / 30 * 100) + (assignment_two_grade / 30 * 100)) / 2) * ASSIGNMENT_WEIGHT

# Input the values for the quizzes
quiz_one_grade = float(input("Enter quiz one grade (0 - 20): "))
quiz_two_grade = float(input("Enter quiz two grade (0 - 20): ")) 
quiz_range = True if (quiz_one_grade >= 0 and quiz_one_grade <= 20) and (quiz_two_grade >=0 and quiz_two_grade <= 20) else False

# Calculate quiz grade average
quiz_grade_average = (((quiz_one_grade / 20 * 100) + (quiz_two_grade / 20 * 100)) / 2) * QUIZ_WEIGHT

#  Check if each category was within range
if not exam_range:
    print("Invalid: Must enter exam value within 0 - 100 range")
if not assignment_range:
    print("Invalid: Must enter assignment grade value within 0 - 30 range.")
if not quiz_range:
    print("Invalid: Must enter quiz grade value within 0 - 20 range.")

# When all assigned categories are within range, calculate the final grade
if exam_range and assignment_range and quiz_range:
    # Calculate the final grade by adding the weighted averages and divided by 100.
    final_grade = (exam_grade_average + assignment_grade_average + quiz_grade_average) / 100
else:
    final_grade = 0

# Printing the final grade percentage with two decimal places.
print("The student's final grade is " + f'{final_grade:.2%}')