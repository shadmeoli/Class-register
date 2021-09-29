"""
#the table I am using in mysql workbench with the parameters

User --> d2i
password --> meoliminoo0820
Database for the app --> d2i_register
DataTable --> d2i_classes

"""
# class register class test app
import time
import os
import json
from datetime import datetime
import tkinter as tk
from tkinter.ttk import *
from tkinter import DoubleVar, ttk
from tkinter import messagebox
from tkinter.messagebox import *
from calendar import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime
# database
#postgresql
import psycopg2
import mysql.connector
import sqlite3

#get current time for future use fro class duretion calculation
now  = datetime.now()

# root window
main = tk.Tk()
main.geometry('500x300')
main.title('D2I Class Attendance')
main.config(background='LightCyan1')
main.resizable(False, False)

#mysql connection
myconn = mysql.connector.connect(user = 'd2i', host = 'localhost', password = 'meoliminoo0820')
print('DONE')


#mysql cursor
cur = myconn.cursor()

cur.execute('USE d2i_register')

# user entries capture
class entries():
    def student(self):
        stuN = studentE.get()
        lecN = lec.get()
        crse = course.get()
        classtime = datetime.now()
        data = {
            "student Name": stuN,
            "lectures Name": lecN,
            "Course Name": crse,
            "time": classtime
        }
        return data 


def date():
    ttk.Label(main, text='Choose date').place(x=200, y=180)

    cal = DateEntry(main, width=12, background='LightCyan1',
                    foreground='white', borderwidth=1, year=2021)
    cal.place(x=200, y=200)

# start function
def startSeccion():

    """
    #writing data to database
    #variable
    conn = psycopg2.connect(host = '127.0.0.1', user='shad', database='postgres', password='shadcodes')

    #grub data from user input 
    student = studentE.get()
    crse = course.get()
    admnum = 2459
    data = [student, crse, admnum]

    #postgres cursor object
    cur = conn.cursor()
    cur.execute(f"INSERT INTO d2i(studentadmissionnumber, studentname, course) VALUES('{admnum}', '{student}', '{crse}')")
    print(f"{data} uploaded class database succesfully")
    conn.commit()
    conn.close()
    print("Database connection closed")
    """
    #grub data from user input 
    student = studentE.get()
    lec_name = lec.get() 
    crse = course.get()

    messagebox.showinfo('Strated', 'Seccion started.')
    dat = entries()
    dat.student()
    main.destroy()
    start_time = now.strftime("%H:%M")
    time_duration = { "start" : start_time }
    print(time_duration)

    #wrting to a json file
    #classData = open('class.txt', 'r')
    import start


    #mysql database writing
    cur.execute(f"INSERT INTO d2i_classes(student_name, lecture_name, course_name) VALUES('{student}', '{lec_name}', '{crse}');")

    myconn.commit()
def endSeccion():
    messagebox.showinfo('Ended', 'Seccion ended.')
    print('ended')


# student credentials.
studentName = Label(main, text='Student Name',background='LightCyan1', foreground='gray40')
studentName.place(x=160, y=10)
studentE = Entry(main, foreground='gray')
studentE.place(x=160, y=30)

# teachers credentials.
lecName = Label(main, text="Lecture's Name",background='LightCyan1', foreground='gray40')
lecName.place(x=160, y=60)
lec = ttk.Combobox(main,background='LightCyan1', foreground='gray40',
                   values=[
                       'Mr.Edwin',
                       'Mr.John',
                       'Mr.Japheth',
                       'Mr.Wyclife',
                       'Mrs.Pauline'
                   ])
lec.place(x=160, y=80)
teacher = lec.get()

if teacher == 'Mrs.Pauline':
    course = ttk.Combobox(main,background='LightCyan1', foreground='gray40',
                          # school of foregin lagues
                          values=['English/Kiswahili',
                                  'Arabic',
                                  'Spanish',
                                  'German',
                                  'Chinese',
                                  'Italian',
                                  'French'
                                  ])

if teacher != 'Mrs.Pauline':
    # student course/package.
    courseName = Label(main, text="Course/Package Name",background='LightCyan1', foreground='gray40')
    courseName.place(x=160, y=110)
    course = ttk.Combobox(main,background='LightCyan1', foreground='gray40',
                          values=[
                              # school of graduate admssions and plcement
                              'TOEFL',
                              'IELTS',
                              'PTE',
                              'SAT',
                              'GRE',
                              'GMAT',
                              # school of foregin lagues
                              'English/Kiswahili',
                              'Arabic',
                              'Spanish',
                              'German',
                              'Chinese',
                              'Italian',
                              'French',
                              # school of ict & cert
                              'Computer Application Packages',
                              'Graphic Design & Animation',
                              # TVETA/CDACC/KNEC/COMPUTER ARTISAN,CRAFT & DIPLOMA PROGRAMMES
                              'Computer Application',
                              'ICDL',
                              'ICT',
                              'Network & System Administration',
                              'computer science',
                              'Diploma in ICT',
                              'Certified ICT Technologist',
                              'Cyber Security',
                              'Data Managment & Analytics',
                              # computer & network engineering
                              'A+',
                              'N+',
                              # CYBER SECURITY CERTIFICATIONS
                              'Certified Secure Computer User',
                              'Certified Network Defender',
                              'Certified Ethical Hacker',
                              'Certified Information. System Security Professional',
                              'Cyber Securty',
                              'Data Managment and Analytics',
                              # CODING AND SOFTWARE DEVELPMENT
                              'progrmming',
                              'Visual Basic Programming',
                              'VB.NET Programming & Dev.Environment',
                              'c# programmng',
                              'Python Programming',
                              'C/C++ Programming',
                              'Java Programming',
                              'Visual C++ Programming',
                              'Bundle offer',
                              'Intro to Data Sciecne',
                              'HTML5',
                              'Javascript',
                              'CSS3',
                              'Dreamweaver|Joomla|WordPress|Drupal',
                              'PHP',
                              'MySQL|MS SQL',
                              'Web Development',
                              'Android Programming|Python Django',
                              'Microsoft Tecnology Associate',
                              'Microsoft Certified Systems Developer',

                              # ORACLE CERTIFICATIONS
                              'Oracle  Certified Associate DBA',
                              'Sql and Administration/Workshop 1',
                              'OCP-Oracle Professional DBA',
                              'Administration/Workshop II',

                              # MICROSOFT CERTIFICATIONS
                              'Microsoft Certications',
                              'Azure//Microsoft 365//Dynamic 365',
                              'Linus Administration',
                              'Client/Server',
                              'Bundle Offer MTA,MCSA,MCSE,LINUX',
                              'Amazon Web Service-Cloud Computing',
                              'Associate//Professional'


                              # HUAWEI ICT ACADEMY CERTIFICATIONS
                              'HCIA-Routing and Switching',
                              'HCIA-Cloud Computing',
                              'HCIA-Security',
                              'HCIA-Artificial Intelligence',
                              'HCIA Routing and Switching',

                              # SCHOOL OF DATA SCIENCE
                              'Diploma in Applied Statics',
                              'Data Science-Azure AI and Machine Learning'

                          ])
    course.place(x=160, y=130)

# widgets(ttk styled and themed widgets)
s = ttk.Style()
s.configure('start.TButton', background='cyan')
s = ttk.Style()
s.configure('date.TButton', background='cyan')

# date and day selection
datePicker = Button(main, text="Date", command=date, style='date.TButton')
datePicker.place(x=100, y=250)

# lesson/seccion start
start = Button(main, text='START', command=startSeccion,
               cursor='hand2', style='start.TButton')
start.place(x=300, y=250)


if __name__ == '__main__':
    main.mainloop()
