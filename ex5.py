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
    f1= open(input_json_path, 'r')
    file = json.loads(f1.read())
    f1.close()
    f2=open(output_file_path, 'w')

    courses_names = {}
    for student in file:
        for course in file[student]['registered_courses']:
           if course in courses_names:
               courses_names[course]+=1
           else:
               courses_names[course]=1
    
    for course in sorted(courses_names):
        f2.write('"' + course + '"' + " " + str(courses_names[course]) + os.linesep)

    f2.close()


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    fout =open(output_json_path, 'w')
    lecturers = {}
    for file in os.listdir(json_directory_path):
        if(file.endswith('.json')):
            f = open(json_directory_path+ os.sep+file, 'r')
            data = json.loads(f.read())
            f.close()
            for course_id in data:
                for lecture in data[course_id]['lecturers']:
                    if lecture in lecturers:
                        if data[course_id]['course_name'] not in lecturers[lecture]:
                            lecturers[lecture].append(data[course_id]['course_name'])
                    else:
                         lecturers[lecture]= [data[course_id]['course_name']]
    

    fout.write(json.dumps(lecturers))

    fout.close()

