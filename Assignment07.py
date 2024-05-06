# -----------------------------------------------------------------
#
# Title: Assignment07.py
# Desc: This assignment builds on Assignment06 to demonstrate using data classes
# Change Log: (Who, When, What)
# TMcGrew, 2024-05-02, Created script reusing code from my Assignment06.py
# TMcGrew, 2024-05-04, Added a Student class, changed read/write to a file to work with new
#       Student class by making a list_of_dictionary_data variable as json can't use the
#       Student object directly, changed other functions to work with the object
# TMcGrew, 2024-05-05, Added properties and private attributes for the Student class,
#       changed the input_student_data method to return a list and added it equal to a list
#       where it calls it
# TMcGrew, 2024-05-06, Added a Person class that will now be the parent class of Student
# ------------------------------------------------------------------

# imports

import json
from json import JSONDecodeError

# from typing import TextIO #not needed except for type hints and to make it stop complaining

# Data -------------------------------------------- #

# constants

MENU: str = "\n --- Course Registration Program --- \n"
MENU += "Select from the following menu: \n"
MENU += "1. Register a Student for a Course \n"
MENU += "2. Show current data \n"
MENU += "3. Save data to a file \n"
MENU += "4. Exit the program \n"
MENU += "-------------------------------\n"

FILE_NAME: str = "Enrollments.json"

# variables

menu_choice: str = ""
students: list = []  # table of student data (list of objects) 


class Person:
    """
    A class representing person data.
    Acts as a template to create person objects.

    ChangeLog: (Who, When, What)
    TMcGrew,05.06.2024,Created class

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - TMcGrew 5.6.2024: Created the class.
    - TMcGrew 5.6.2024: Added properties and private attributes
    """

    # constructor
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    # getter and setter properties for the private attribute __first_name
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # getter and setter properties for the private attribute __last_name
    @property
    def last_name(self):
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return (f"{self.first_name},{self.last_name}")


class Student(Person):
    """
    A class representing student data.
    Acts as a template to create student objects that can be added to the student_data list.


    Properties:
    - first_name (str): The student's first name inherited from Person class
    - last_name (str): The student's last name inherited from Person class
    - course_name (str): The course student is registering.

    ChangeLog:
    - TMcGrew 5.4.2024: Created the class.
    - TMcGrew 5.5.2024: Added properties and private attributes
    - TMcGrew 5.6.2024: Now inherits from Person class
    - TMcGrew 5.6.2024: Removed first and last name getter and setters as Person now handles it
    - TMcGrew 5.6.2024: overwrote the __str__ from Person
    """

    # constructor
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ""):
        super().__init__(first_name=first_name, last_name=last_name)  # calls Person class constructor
        self.course_name = course_name

    # getter and setter properties for the private attribute __course_name
    @property
    def course_name(self):
        return self.__course_name.title()  # formatting code

    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value

    def __str__(self):
        return (f"{self.first_name},{self.last_name},{self.course_name}")


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    TMcGrew,04.29.2024,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        TMcGrew,04.29.2024,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user

        ChangeLog: (Who, When, What)
        TMcGrew,04.29.2024,Created function
        :param menu: string with menu of choices to display

        :return: None
        """
        # Present the menu of choices
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function takes input from the user as to menu choice and sets the global
        menu_choice variable

        ChangeLog: (Who, When, What)
        TMcGrew,04.29.2024,Created function

        :return: None
        """
        global menu_choice

        menu_choice = input('Your selection?: ')

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function takes a list of objects and presents them formatted to the user

        ChangeLog: (Who, When, What)
        TMcGrew,04.29.2024,Created function
        TMcGrew 05.4.2024, changed to take list of objects instead of dictionaries
        :param student_data: list of objects to display

        :return: None
        """
        # Present the current data
        for student in students:
            # print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")
            # Replace using dictionary keys with using object attributes
            print(f"{student.first_name} {student.last_name} is registered for {student.course_name}.")
            # could also just do print(student) since now there is an overwrote __str__ method

    @staticmethod
    def input_student_data(student_data=list) -> list:
        """ This function takes a list of dictionaries and gets input from the user, formats
        it into a Student object row and appends that list that was passed in

        ChangeLog: (Who, When, What)
        TMcGrew,04.29.2024,Created function
        TMcGrew,05.04.2024, now creates a Student object row and not a dictionary
        TMcGrew,05.05.2024, now returns the list
        TMcGrew,05.05.2024, now doesn't need the local variables as creates a new student object
            using each property's validation code

        :param student_data: list of objects to input student data to by appending it

        :return: list
        """
        # student_first_name: str = ""
        # student_last_name: str = ""
        # course_name: str = ""
        # student_row: Student = None  # one row of student data as a object

        # variables capturing the input asked from the user
        try:
            # student_first_name = input("Please enter your first name: ")
            # if not student_first_name.isalpha():
            #     raise ValueError("The first name should not contain numbers.")
            #
            # student_last_name = input("Please enter your last name: ")
            # if not student_last_name.isalpha():
            #     raise ValueError("The last name should not contain numbers.")
            #
            # course_name = input("Please enter the course name: ")

            # code to create a new student object using each property's validation code
            student = Student()  # Note this will use the default empty string arguments
            student.first_name = input("Please enter the student's first name: ")
            student.last_name = input("Please enter the student's last name: ")
            student.course_name = (input("Please enter the course name: "))
            student_data.append(student)

            # Add the student info to a dictionary using the student_row variable,
            # then add that dictionary to the student_data list to create a table of data
            # (a dictionary inside of a list).
            # student_row = \
            #     {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            # student_data.append(student_row)  # important use .append here so gets passed in and not local reference

            # Replace using a dictionary with using a student object
            # Add the student info into a Student object
            # student_row = \
            #     Student(first_name=student_first_name, last_name=student_last_name, course_name=course_name)
            # student_data.append(student_row)

            # notify user to pick '3' now to fully register by saving it to a file
            print("\nThank you! Please now select '3' to save the registration to a file.\n")

        except ValueError as e:
            IO.output_error_messages(e)  # Prints the custom message

        except Exception as e:
            IO.output_error_messages("There was a non-specific error!\n", e)

        return student_data


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    TMcGrew,04.29.2024,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads a json file and loads it into a list
        both of which are passed in when called

         ChangeLog: (Who, When, What)
         TMcGrew,04.29.2024,Created function
         TMcGrew 05.4.2024, changed to work with list of objects instead of dictionaries

        :param file_name: string data with name of file to read from
        :param student_data: list of object rows to be filled with file data

        :return: None
         """

        file: TextIO = None
        list_of_dictionary_data: list = []

        try:

            # When the program starts, read the file data into a list of dictionaries (table)
            file = open(file_name, "r")
            # Extract the data from the file

            # student_data += json.load(file)  # must import json above ###### here students? or student_data?
            # now student_data contains the parsed JSON data as a Python list of dictionaries
            # since passing in not just student_data = but += or could do loop through and append
            # it's a reference issue

            list_of_dictionary_data = json.load(file)  # the load function returns a list of json objects
            # converts the json dictionary objects to student objects
            for student in list_of_dictionary_data:
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)

        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!\n", e)
            IO.output_error_messages("Creating file since it doesn't exist", e)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)  # putting empty list in upon creation
        except JSONDecodeError as e:
            IO.output_error_messages("Data in file isn't valid. Resetting it...", e)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)  # putting empty list in upon creation
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!\n", e)
        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes to a list of dictionaries to a json file both of which
        are passed in

         ChangeLog: (Who, When, What)
         TMcGrew,04.29.2024,Created function
         TMcGrew,05.04.2024,now takes list of objects and converts to list of dictionaries

        :param file_name: string data with name of file to write to
        :param student_data: list of objects to be writen to the file

        :return: None
         """

        file: TextIO = None

        try:
            # Save the data to a file

            # Creates a new list to hold json data to use with the json.dump() function.
            # using this variable to create Json data from a student object
            list_of_dictionary_data: list = []

            # Convert List of Student objects to json compatible list of dictionary.
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            # open() function to open a file in the desired mode ("w" for writing, "a' to append).
            file = open(file_name, "w")
            # json.dump(student_data, file)
            json.dump(list_of_dictionary_data, file)
            # closes the file to save the information
            file.close()

            # shows user what it just wrote to the file
            for student in student_data:
                # Replaces using dictionary keys with using object attributes
                print(f"{student.first_name} {student.last_name} is fully registered for {student.course_name}.")
                # could also just do print(student) since now there is an overwrote __str__ method

            # print(f"{student['FirstName']} {student['LastName']} is fully registered for {student['CourseName']}.")

            # print a line to get space after printing info and before menu again
            print('\n')

        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format\n", e)
        except Exception as e:
            IO.output_error_messages("Built-In Python error info: ", e)
        finally:
            if file.closed == False:
                file.close()


# Beginning of the main body of this script

# When the program starts, read the file data into a list of dictionaries (table)
FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# -- present and process the data -- #

# repeat the following tasks
while (menu_choice != "4"):
    # # Present the menu of choices
    IO.output_menu(menu=MENU)  # now in two different functions instead of MENU and input on one line
    IO.input_menu_choice()

    if (menu_choice == '1'):
        students = IO.input_student_data(student_data=students)  # now returns so is now students =
        continue

    elif (menu_choice == '2'):
        # Present the current data
        IO.output_student_courses(students)
        print("\nPlease now select '3' to save the registrations you entered to a file.\n")
        continue

    elif (menu_choice == '3'):
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif (menu_choice == '4'):
        exit()
        # break? or continue? or exit()?

    else:
        # spacing
        print()
        # They they picked something other than the options given
        print("Please pick one of the options.")
        # spacing
        print()
        continue
