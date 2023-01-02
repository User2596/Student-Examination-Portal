import csv
import re
import matplotlib.pyplot as plt
import numpy as np
import student
import course
import batch
import department
import examination
def main():
    print("1. To create, update, remove or to generate a report of a student, enter '1'.")
    print("2. To create or view details and statistics of a course, enter '2'.")
    print("3. To create or view details and statistics of a batch, enter '3'.")
    print("4. To create or view details and statistics of a department, enter '4'.")
    print("5. To enter marks or view statistics of examination, enter '5'.")
    choice=input()
    if (choice=='1'):
        u=int(input("1. To create a new student, enter 1 \n2. To update student details, enter 2 \n3. To remove a student, enter 3 \n4. To generate report card of a student, enter 4 \n"))
        std_id=input("Enter student id: ")
        std_name=input("Enter student name: ")
        std_rollno=input("Enter student roll no.: ")
        std_batchid=input("Enter student batch id: ")
        if(u==1):
            student.new_student(std_id,std_name,std_rollno,std_batchid)
        elif(u==2):
            student.update_student(std_id,std_name,std_rollno,std_batchid)
        elif(u==3):
            student.remove_student(std_id,std_name,std_rollno,std_batchid)
        elif(u==4):
            student.result_student(std_id,std_name,std_rollno,std_batchid)
        else:
            print("Something went wrong. Please try again.")
    elif(choice=='2'):
        u=int(input("1. To create a new course, press 1 \n2. To view performance of all the students in a course, press 2 \n3. To view course statistics, press 3 \n"))
        if(u==1):
            marks_obt={"Student name":[],"Roll no.":[],"Marks":[]}
            crse_id=input("Enter the course ID: ")
            crse_name=input("Enter the course Name: ")
            n=int(input("Enter the number of students whose marks are to be entered: "))
            for i in range(n):
                name=input("Enter the name of the student: ")
                rollno=input("Enter the roll number of the student: ")
                marks=input("Enter the marks: ")
                marks_obt["Student Name"].append(name)
                marks_obt["Roll Number"].append(rollno)
                marks_obt["Marks"].append(marks)
            course.new_course(crse_id,crse_name,marks_obt)
        elif(u==2):
            crse_id=input("Enter the course ID: ")
            crse_name=input("Enter the course name: ")
            course.view_course(crse_id,crse_name)
        elif(u==3):
            crse_id=input("Enter the course ID: ")
            crse_name=input("Enter the course name: ")
            course.histogram_course(crse_id,crse_name)
        else:
            print("Something went wrong. Please try again.")
    elif(choice=='3'):
        u=int(input("1. To create a new batch, press 1 \n2. To view list of all students in a batch, press 2 \n3. To view list of all courses taught in a batch, press 3 \n4. To view complete performance of all students in a batch, press 4 \n5. To view pie chart of the student distribution of the grades, press 5 \n"))
        if(u==1):
            batch_id=input("Enter the batch ID: ")
            batch_name=input("Enter the batch name: ")
            dept_name=input("Enter the department name: ")
            n=int(input("Enter the number of courses to be entered: "))
            crse_list=[]
            for i in range(n):
                crse_id=input("Enter course ID: ")
                crse_list.append(crse_id)
            std_list=[]
            n=int(input("Enter the number of students to be entered: "))
            for i in range(n):
                std_id=input("Enter the student ID: ")
                std_list.append(std_id)
            batch.new_batch(batch_id,batch_name,dept_name,crse_list,std_list)
        elif(u==2):
            batch_id=input("Enter the batch ID: ")
            batch_name=input("Enter the batch name: ")
            batch.studentlist_batch(batch_id,batch_name)
        elif(u==3):
            batch_id=input("Enter the batch ID: ")
            batch_name=input("Enter the batch name: ")
            batch.courselist_batch(batch_id,batch_name)
        elif(u==4):
            batch_id=input("Enter the batch ID: ")
            batch_name=input("Enter the batch name: ")
            batch.performance_batch(batch_id,batch_name)
        elif(u==5):
            batch_id=input("Enter the batch ID: ")
            batch_name=input("Enter the batch name: ")
            batch.pie_batch(batch_id,batch_name)
        else:
            print("Something went wrong. Please try again.")
    elif(choice=='4'):
        u=int(input("1. To create a new department, press 1 \n2. To view all batches in a department, press 2 \n3. To view average performance of all batches in the department, press 3 \n4. To view department statistics, press 4 \n"))
        if(u==1):
            dept_id=input("Enter the department ID: ")
            dept_name=input("Enter the department name: ")
            dept_batchlist=[]
            n=int(input("Enter the number of batches to be entered: "))
            for i in range(n):
                batch_id=input("Enter the batch ID: ")
                dept_batchlist.append(batch_id)
            department.new_department(dept_id,dept_name,dept_batchlist)
        elif(u==2):
            department_id=input("Enter the department ID: ")
            department.viewbatch_department(department_id)
        elif(u==3):
            dept_id=input("Enter the department ID: ")
            department.avgperformance_department(dept_id)
        elif(u==4):
            dept_id=input("Enter the department ID: ")
            department.lineplot_department(dept_id)
        else:
            print("Something went wrong. Please try again.")
    elif(choice=='5'):
        u=int(input("1. To enter marks of students for a specific examination, press 1 \n2. To view performance of all students in the examination, press 2 \n3. To view examination statistics, press 3 \n"))
        if(u==1):
            m=int(input("Enter the number of courses in the examination: "))
            for i in range(m):
                crse_name=input("Enter the course name: ")
                std_list=[]
                n=int(input("Enter the number of students to be entered: "))
                for j in range(n):
                    std_name=input("Enter the student name: ")
                    std_rollno=input("Enter the student roll number: ")
                    std_marks=input("Enter the student marks: ")
                    std_list.append([std_rollno,std_name,std_marks])
                    examination.exam(crse_name,std_list)
        elif(u==2):
            year=input("Enter the year of admission of the batch: ")
            examination.view_exam(year)
        elif(u==3):
            year=input("Enter the year of admission of the batch: ")
            examination.scatterplot_exam(year)
        else:
            print("Something went wrong. Please try again.")
    else:
        print("Something went wrong. Please try again.")
if __name__=="__main__":
    main()
