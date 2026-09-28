''' This program will calculate a student's grade based on scores from the user's input and the weights for each category. '''

# Weight values for exam, assignment, and quiz.
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# Input the value for each score.
midterm_exam_grade = float(input("Enter midterm exam grade: "))
final_exam_grade = float(input("Enter final exam grade: "))
assignment_one_grade = float(input("Enter assignment one grade: "))
assignment_two_grade = float(input("Enter assignment two grade: "))
quiz_one_grade = float(input("Enter quiz one grade: "))
quiz_two_grade = float(input("Enter quiz two grade: "))

# Calculate the averages of each category multiplied by the weight value of that category.
exam_grade_average = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT
assignment_grade_average = ((assignment_one_grade + assignment_two_grade) / 2) * ASSIGNMENT_WEIGHT
quiz_grade_average = ((quiz_one_grade + quiz_two_grade) / 2) * QUIZ_WEIGHT

# Calculate the final grade by adding the weighted averages and divided by 100.
final_grade = (exam_grade_average + assignment_grade_average + quiz_grade_average) / 100

# Printing the final grade percentage with two decimal places.
print("The student's final grade is " + f'{final_grade:.2%}')