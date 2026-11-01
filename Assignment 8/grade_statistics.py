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
    # Empty student list and weighted grades to store values
    student_list = []
    weighted_grade_list = []

    try:
        # Open the grades CSV file.
        with open(GRADES_FILE, 'r') as grades:
            # Skipping the header row and starting on the row of the first student.
            line = grades.readline()
            line = grades.readlines()

            for l in line:
                # Splitting the commas before appending each student to list
                s = l.split(',')
                student_list.append(s)

        # Once finished with the CSV file, calculate each student's average grades and weighted grades.
        for i in range(len(student_list)):
            # Getting each student's average scores of the test, exam, discussion, and project.
            test_avg_score, exam_avg_score, discussion_avg_score, project_avg_score = process_row(student_list[i][2:])    # The [2:] is used to bypass the student name and student ID.
  
            # Calculating the weighted final score before adding the score to weighted grade list.
            weight_final_grade = weight_final(test_avg_score, exam_avg_score, discussion_avg_score, project_avg_score)
            weighted_grade_list.append(weight_final_grade)

        # Calculating the average of the scores by adding all the students' weighted grades together.
        average_scores = average_subject(weighted_grade_list)
        print(f"The average of the {len(weighted_grade_list)} scores is: {average_scores:.2f}")

        # Calculating how many students fall into each grade range.
        analyze_grade(weighted_grade_list)
        
    except FileNotFoundError as file_error:
        print(file_error)
    except TypeError as err:
        print(f"Error: {err}")

def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # TODO - Implement this function.

    # Constant variables inside this function. Based on the CSV file, the total number columns of tests, exams, and discussions.
    TOTAL_TEST_SCORES = 4
    TOTAL_EXAM_SCORES = 2
    TOTAL_DISCUSSION_SCORES = 2

    # Calculating the test grade average.
    # The 'i' variable will be used inside slicing string for starting point and ending point.
    i = TOTAL_TEST_SCORES
    total_test = 0
    for val in row[0:i]:  # Starting from the first test score column up to the last test score column using slicing string in loop.
        # Converting test score value to float multiplied by the test weight value before adding to test total.
        weighted_score = float(val) * TEST_WEIGHT
        total_test += weighted_score
    test_average_score = total_test / TOTAL_TEST_SCORES

    # Calculating the exam grade average.
    total_exam = 0
    for val in row[i:(i + TOTAL_EXAM_SCORES)]:   # [i:(i + TOTAL_EXAM_SCORES)] is used to get the two exam score values after the test score columns in CSV.
        # Converting exam score value to float multiplied by the exam weight value before adding to exam total.
        weighted_score = float(val) * EXAM_WEIGHT
        total_exam += weighted_score
    exam_average_score = total_exam / TOTAL_EXAM_SCORES
    # Adding before the next loop
    i += TOTAL_EXAM_SCORES

    # Calculating the discussion grade average
    total_discussion = 0
    for val in row[i:(i + TOTAL_DISCUSSION_SCORES)]:  # [i:(i + TOTAL_DISCUSSION_SCORES)] is used to get the two discussion score values after the exam score columns in CSV.
        # Converting discussion score value to float multiplied by the discussion weight value before adding to discussion total.
        weighted_score = float(val) * DISCUSSION_WEIGHT
        total_discussion += weighted_score
    discussion_average_score = total_discussion / TOTAL_DISCUSSION_SCORES

    # Project weighted grade
    project_grade = float(row[-1]) * PROJECT_WEIGHT

    # Return all the weighted scores.
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
    for weighted_grade in weight_final_list:
        score = weighted_grade * 100
        if score >= 90:
            students_with_A_grade += 1
        elif score >= 80 and weighted_grade < 90:
            studenst_with_B_grade += 1
        elif score >= 70 and weighted_grade < 80:
            students_with_C_grade += 1
        elif score >= 60 and weighted_grade < 70:
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
