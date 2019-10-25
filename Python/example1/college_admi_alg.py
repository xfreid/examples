'''
Instruction:
Prospective student data is organized in the superheroes.csv file such that the data for each
student is on one line, with the values separated by tabs. An example of two students’ data
might be:
Student,SAT,GPA,Interest,High School Quality,Sem1,Sem2,Sem3,Sem4
Abbess Horror ,1300,3.61,10,7,95,86,91,94
Adele Hawthorne ,1400,3.67,0,9,97,83,85,86
Adelicia von Krupp ,900,4,5,2,88,92,83,72

Problem 1: Getting set up with our data
  First, we need to make sure that we can appropriately read in the data line by line, parsing each
  line into a list and converting each element to the appropriate type.
  
  Task 1: read in your data set in main(), looping through its contents line by line. This data
  contains one row of headers at the beginning, so isolate the headers before reading through the
  rest of the file so you don't try to do calculations with them!
  Make use of the str.split(delimiter) function to break individual lines into a list of elements. Print
  the contents of your list after using the split function. You'll delete this print statement later but
  make sure to double check this before moving on! Once you have each line in a list, save the
  student's name in a variable, then delete this element from your list.

  Task 2: Once you have a list of strings for each line, you will write a function convert_row_type
  that takes one list of elements (representing the data for one student) as a parameter and
  converts it so that all numbers are converted to floats. Make sure not to lose any information
  when you do this conversion! Implement this as a pure function.
  Example:
  Input: ["1300","3.61","10","7","95","86","91","94"]
  Return value: [1300.0,3.61,10.0,7.0,95.0,86.0,91.0,94.0]

  Task 3: in main, once you've called convert_row_type on the list representing one row, call the
  provided check_row_type. If this function returns False, print out an error message. Ensure that
  none of the rows in your data return False when passed to this function.

  Task 4: separate your data. Use list slicing or while loops to separate your list (which should
  contain 8 numbers at this point) into two lists: one that contains the student's SAT, GPA,
  Interest, and High School Quality scores, and one that contains their 4 semester grades. You'll
  do Problems 2 - 5 with the first list of 4 numbers and Problem 6 with the list of grades.
'''

'''
Problem 2: Prospective Student Score
  Task 1: Write a function calculate_score that takes a list as a parameter and calculates an
  overall score for each student based on the following weights: 40% GPA, 30% SAT, 20%
  strength of curriculum, 10% demonstrated interest. The list parameter will contain all of the
  relevant information about the student. The return value is the student’s calculated score.
  To make this work, you will also need to normalize both GPA and SAT so that they are also on
  a 0 to 10 scale. To do this, multiply the GPA by 2, and divide the SAT score by 160.
  Example:
  Input: [1300.0,3.61,10.0,7.0]
  which represents a student with a 1300 SAT score, a 3.61 GPA, 10 out of 10 for interest and 7
  out of 10 for high school quality
  ((3.61 * 2) * 0.4) + ((1300 / 160) * 0.3) + (10 * 0.1) + (7 * 0.2) = 7.73 out of 10
  Output: 7.73
  Round each output score to 2 decimal points.

  Task 2: In your main() function, modify your loop that reads in and converts your data to call the
  calculate_score function for each line (row) of data (after you've converted it). Then, write the
  student's name and their calculated score to a new file called student_scores.csv such that
  each row contains a student’s name and their score, separated by a comma.
  Example:
  Abbess Horror ,1300,3.61,10,7,95,86,91,94
  Adele Hawthorne ,1400,3.67,0,9,97,83,85,86
  Adelicia von Krupp ,900,4,5,2,88,92,83,72
  lines written to file:
  Abbess Horror ,7.73
  Adele Hawthorne ,7.36
  Adelicia von Krupp ,5.79

  Task 3: Write all the student name and the score for all students who have a score of 6 or
  higher to a file called chosen_students.txt. You should do this in your main() function, where
  you have access to the returned calculated score for each student and their student name.
  Example:
  Abbess Horror ,1300,3.61,10,7,95,86,91,94
  Adele Hawthorne ,1400,3.67,0,9,97,83,85,86
  Adelicia von Krupp ,900,4,5,2,88,92,83,72
  lines written to file:
  Abbess Horror
  Adele Hawthorne
'''

'''
Problem 3: Looking for Outliers (10 points)
  Consider ways that this algorithm might systematically miss certain kinds of edge cases. For
  example, what if a student has a 0 for demonstrated interest because they don’t use social
  media or have access to a home computer? What if a student has a very high GPA but their
  SAT score is low enough to bring their score down; could this mean that they had a single bad
  test taking day?
  
  Task 1: Write a function is_outlier that can check for certain kinds of outliers. It should check
  for: (1) demonstrated interest scores of 0 and (2) a normalized GPA that is more than 2 points
  higher than the normalized SAT score. If either of these conditions is true, it should return True
  (because this student is an outlier); otherwise, the function returns False.

  Task 2: Call is_outlier for each student from your main() function and write the students' names
  to a file called outliers.txt, one name per line if they are an outlier.

  Task 3: Combine the work that you've done now to create an improved list of students to admit
  to your school. Write students names, one per line to the file chosen_improved.txt if they
  either have a score of 6 or greater or if they are an outlier and their score is 5 or greater. Make
  sure to take advantage of the work that you've already done by calling your functions from
  previous problems to help you out!
'''

'''
Problem 4: GPA Checker
  A single GPA score is not a full picture of a student’s academic performance, as it may have
  improved over time or included outlier courses or semesters. A more context-sensitive algorithm
  could consider a student’s entire transcript and checks for, for example, a single class score that
  is more than two letter grades (20 points) lower than all other scores. For this task, you will use
  the second half of the data for each student in the provided file.

  Task 1: Write a function grade_outlier that takes in a list of grades (of any length at least 2) and
  returns True if one single number is more than 20 points lower than all other numbers;
  otherwise, False. This function must not modify the list passed in!
  Example:
  Input: [99, 94, 87, 89, 56, 78, 89]
  Hint: Sort the list from lowest to highest, and check for the difference between the two lowest
  grades.
  78 - 56 = 22; 22 > 20
  Output: True
  Next, consider the data that we have: a list of grades for each student, one grade per semester
  for four semesters.
  Make sure that your grade_outlier function works by calling it for every row, passing in the
  grades list you isolated in problem 1, task 4. Print out an informative message about which
  students have a single grade outlier. You'll delete this later but it's a great way of testing your
  function!

  Finally, consider the importance of an algorithm being able to flag students who might have a
  lower overall GPA but have showed improvement over time.
  Task 2: Create a function grade_improvement that returns True if the score of each semester
  is higher than each previous semester and False otherwise. Hint: investigate how the ==
  operator works between two lists and think about using the sorted() function.
  
  Task 3: Using the grade information that you've just learned, create your own conditions based
  on the information from the previous problems and grade_outlier and grade_improvement to
  chose all students if they either have a score of 6 or greater or if they have a score of 5 or more
  and at least one of the following is true: is_outlier returns True, grade_outlier returns True, or
  grade_improvement returns true. Write the students who fit this description to
  extra_improved_chosen.txt, one name per line.
'''


# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


def convert_row_type(input_data):
    # debug
    out_data = []
    for field in input_data:
        new_field = float(field)
        # print("input field '" + field + "'")
        # new_field = float("{:.2f}".format(field_number))
        out_data.append(new_field)
        # print("output field '" + new_field + "'")
    return out_data

def calculate_score(scores):
    # Input: [1300.0,3.61,10.0,7.0]
    # 1300 SAT score, a 3.61 GPA, 10 out of 10 for interest, and 7
    # out of 10 for high school quality

    # assign each item in a list to a variable
    sat, gpa, int, qua = scores
    overall_score = ((gpa * 2) * 0.4) + ((sat / 160) * 0.3) + (int * 0.1) + (qua * 0.2)
    # Round each output score to 2 decimal points
    return round(overall_score, 2)

def is_outlier(scores):
    # (1) demonstrated interest scores of 0 and 
    # (2) a normalized GPA that is more than 2 points higher than the normalized SAT score. 
    # If either of these conditions is true, it should return True

    sat, gpa, int, qua = scores
    normalized_gpa = gpa * 2
    normalized_sat = sat / 160
    if int == 0 or normalized_gpa > normalized_sat + 2.0:
        # print("{} > {} + 2.0".format(normalized_gpa, normalized_sat))
        return True
    else:
        return False

def grade_outlier(grades):
    # Sort the list from lowest to highest, and check for the difference between the 
    # two lowest grades.
    print("------ grade_outliner -------")
    grades.sort()
    print(grades)
    if grades[0] < grades[1] - 20:
        return True
    else:
        return False

def grade_improvement(original_grades, grades):
    # returns True if the score of each semester
    # is higher than each previous semester and False otherwise
    #  Hint: investigate how the ==
    # operator works between two lists and think about using the sorted() function.
    # my origianl thinking: sem1_grade < sem2_grade < sem3_grade < sem4_grad
    # with hint, if origna list == sort list    
    print("------ grade_improvement -------")
    print(original_grades)
    print(grades)
    if original_grades == grades:
        return True
    else:
        return False



import os
import os.path
from os import path
def init():
    # remove all the generated files if they exist
    if path.exists("student_score.csv"):
        os.remove("student_score.csv")
    if path.exists("chosen_student.txt"):
        os.remove("chosen_student.txt")
    if path.exists("chosen_improved.txt"):
        os.remove("chosen_improved.txt")


def main():
    # Change this line of code as needed but
    # make sure to change it back to "superheroes_large.csv"
    # before turning in your work!
    filename = "C:/Git/Python/example1/student_data.csv"
    input_file = open(filename, "r")

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()

    # loop through the rest of file
    for line in input_file.readlines():
        print(line)
        student_data = line.split(',')
        student_name = student_data[0]
        student_data.remove(student_name)
        print(student_name)
        print(student_data)
        formatted_data = convert_row_type(student_data)
        # print(formatted_data)
        if not check_row_types(formatted_data):
            break

        # slice the list
        # In list[first:last], last is not included
        scores = formatted_data[0:4]
        print(scores)
        grades = formatted_data[4:]
        print(grades)

        # calculated score from scores
        cal_score = calculate_score(scores)
        # print(cal_score)

        # write student_score.csv
        out_file1 = open("student_score.csv", "a")
        out_file1.write("{},{}\n".format(student_name, cal_score))
        out_file1.close()

        # write chosen_student.txt
        out_file2 = open("chosen_student.txt", "a")
        if cal_score >= 6:
            out_file2.write(student_name + "\n")
        out_file2.close()

        # write chosen_improved.txt
        out_file3 = open("chosen_improved.txt", "a")
        is_outliner = is_outlier(scores) and cal_score >= 5
        if is_outliner:
            print("{} is outliner".format(student_name))

        # By default, python is "passing by reference"
        # when you assign one list to another, you simpy creates a reference
        # not create a copy. when you pass a list to a function and that function
        # modified the list, the original list also changes
        print("before calling grae_outlier")
        print(grades)
        orignal_grades = grades.copy()
        is_grade_outliner = grade_outlier(grades)
        print("after calling grae_outlier")
        print(grades)
        if is_grade_outliner:
            print("{} is grade outliner".format(student_name))

        if cal_score >= 6 or is_outliner:
            out_file3.write(student_name + "\n")
        out_file3.close()

        grade_improvement(orignal_grades, grades)

    # close the file
    input_file.close()

    print("done!")

init()
main()



