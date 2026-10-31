from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent /"grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.

    # TODO - Read GRADES_FILE and build a list of each student's
    #        weighted final grade (skip the header row, and use
    #        process_row() to do the per-student work).
    # TODO - Pass that list to analyze_grade() to print the summary.
    # TODO - Use try/except to handle a missing file and any other
    #        errors that can occur while reading or processing it.
    """

    # Empty lists that will be used for student grades and weighted grades. 
    student_grade_list = []
    weighted_grade_list = []

    try:
        with open(GRADES_FILE, 'r') as grades:
            # Skipping the header row and starting on the row of the first student.
            line = grades.readline()
            line = grades.readlines()

            for l in line:
                # Splitting the commas in the string.
                s = l.split(',')

                # Appending each student's grade scores to list, bypassing name and student ID as both aren't needed.
                grades = s[2:]
                student_grade_list.append(grades)

        # Once finished with the CSV file, calculate each student's average grades and weighted grades.
        for i in range(len(student_grade_list)):
            # Getting each student's average scores of the test, exam, discussion, and project.
            test_avg_score, exam_avg_score, discussion_avg_score, project_avg_score = process_row(student_grade_list[i])
  
            # Calculating the weighted final score before adding the score to weighted grade list.
            weight_final_grade = weight_final(test_avg_score, exam_avg_score, discussion_avg_score, project_avg_score)
            weighted_grade_list.append(weight_final_grade)

        # Calculating the average of the scores by adding all the students' weighted grades together.
        average_scores = average_subject(weighted_grade_list)
        print(f"The average of the scores is: {average_scores}")

        # Calculating how many students fall into each grade range.
        analyze_grade(weighted_grade_list)

    except FileNotFoundError as file_error:
        print(file_error)

def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # TODO - Implement this function.

    # Constant variables inside this function. Based on the CSV file, the total number of each subject of tests, exams, and discussions.
    TOTAL_TEST_SCORES = 4
    TOTAL_EXAMS_SCORES = 2
    TOTAL_DISCUSSION_SCORES = 2

    # Used to keep calculation of the average grade scores
    test_average_score = 0
    exam_average_score = 0
    discussion_average_score = 0
    
    # Calculating the test grade average
    for i in range(0, len(row) - (TOTAL_TEST_SCORES + 1)):
        test_average_score += (float(row[i]) * TEST_WEIGHT)
    test_average_score /= TOTAL_TEST_SCORES

    # Calculating the exam grade average
    for i in range(4, len(row) - (TOTAL_EXAMS_SCORES + 1)):
        exam_average_score += (float(row[i]) * EXAM_WEIGHT)
    exam_average_score /= TOTAL_EXAMS_SCORES

    # Calculating the discussion grade average
    for i in range(6, len(row) - 1):
        discussion_average_score += (float(row[i]) * DISCUSSION_WEIGHT)
    discussion_average_score /= TOTAL_DISCUSSION_SCORES

    # Project weighted grade
    project_grade = float(row[-1]) * PROJECT_WEIGHT

    # Return all the average scores
    return test_average_score, exam_average_score, discussion_average_score, project_grade

def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    # TODO - Implement this function.

    # Calculating the average of the scores
    average_score = sum(subject_list) / len(subject_list)
    return average_score


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""
    # TODO - Implement this function.

    # Calculating the weighted final grade by adding the average scores of the test, exam, discussion, and project.
    weighted_final_grade = (test_avg + exam_avg + discussion_avg + project_score) / 100
    return weighted_final_grade


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    # TODO - Implement this function.

    # Variable counts of students with a grade of A (90 and highter), B (80-89), C (70-79), D (60-69), and F (below 60).
    students_with_A_grade = 0
    studenst_with_B_grade = 0
    students_with_C_grade = 0
    students_with_D_grade = 0
    students_with_F_grade = 0

    # Check each grade
    for grade in weight_final_list:
        current_grade = grade * 100
        if current_grade >= 90:
            students_with_A_grade += 1
        elif current_grade >= 80 and grade < 90:
            studenst_with_B_grade += 1
        elif current_grade >= 70 and grade < 80:
            students_with_C_grade += 1
        elif current_grade >= 60 and grade < 70:
            students_with_D_grade += 1
        else:
            students_with_F_grade += 1

    # Printing number of stduents with final grade score 
    print(f"Number of students with final grade 90 or above: {students_with_A_grade}")
    print(f"Number of students with final grade 80-89: {studenst_with_B_grade}")
    print(f"Number of students with final grade 70-79: {students_with_C_grade}")
    print(f"Number of students with final grade 60-69: {students_with_D_grade}")
    print(f"Number of students with final grade below 60: {students_with_F_grade}")

if __name__ == "__main__":
    main()
