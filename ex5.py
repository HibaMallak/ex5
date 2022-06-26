from fileinput import close
import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """

    students_in_course = []
    with open(input_json_path, 'r') as f:
        file = json.load(f)
        for student_course in file.values():
            for key in student_course.keys():
                student_name = student_course["student_name"]
                if key == "registered_courses":
                    for courses in student_course[key]:
                        if courses == course_name:
                            students_in_course += [student_name]

    return students_in_course




def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    open(input_json_path, 'r')
    file = json.load(input_json_path)
    input_json_path.close()
    open(output_file_path, 'w')
    courses_names_list = []
    for find_course_name in file.values():
        for course_name in find_course_name.values():
            courses_names_list.append(course_name)
    
    courses_names_list = list( dict.fromkeys(courses_names_list))
    courses_names_list.sort()
    for course in courses_names_list:
        students_in_current_course = names_of_registered_students(input_json_path, course_name)
        students_number = 0
        for student in students_in_current_course:
            students_number += 1
        output_file_path.write(course + " " + students_number + "\n")
    output_file_path.close()




def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass

