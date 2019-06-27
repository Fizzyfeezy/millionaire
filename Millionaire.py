from tkinter import *
import sqlite3 as sql

import pygame

pygame.init()

root = Tk()

root.title("Who wants to be a Millionaire")
root.geometry('1353x352+0+0')
root.configure(background='black')

# =====================================Frames===========================================================================

ABC = Frame(root, bg='black')
ABC.grid()

ABC1 = Frame(root, bg='black', bd=20, width=900, height=600)
ABC1.grid(row=0, column=0)
ABC2 = Frame(root, bg='black', bd=20, width=430, height=600)
ABC2.grid(row=0, column=1)

ABC1a = Frame(ABC1, bg='black', bd=20, width=900, padx=130, height=200)
ABC1a.grid(row=0, column=0)
ABC1b = Frame(ABC1, bg='black', bd=20, width=900, height=200)
ABC1b.grid(row=1, column=0)
ABC1c = Frame(ABC1, bg='black', bd=20, width=900, height=200)
ABC1c.grid(row=2, column=0)


# =====================================Images===========================================================================

def change50_50():
    canvas = Canvas(ABC1a, bg='black', width=160, height=90)
    canvas.grid(column=0, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='50_50X.png')
    canvas.create_image(80, 45, image=image1)
    canvas.image = image1


def changeaudience():
    canvas = Canvas(ABC1a, bg='black', width=160, height=90)
    canvas.grid(column=1, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='audienceX.png')
    canvas.create_image(80, 45, image=image1)
    canvas.image = image1


def change_phone_a():
    canvas = Canvas(ABC1a, bg='black', width=160, height=90)
    canvas.grid(column=2, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='PhoneAX.png')
    canvas.create_image(80, 45, image=image1)
    canvas.image = image1


def million_picture1():
    canvas = Canvas(ABC2, bg='black', bd=20, width=430, height=600)
    canvas.grid(column=0, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='millionair1.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million_picture2():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(column=0, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='millionair2.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million_picture3():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(column=0, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='millionair3.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million_picture4():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(column=0, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='millionair4.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million_picture5():
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(column=0, row=0)
    canvas.delete("all")
    image1 = PhotoImage(file='millionair5.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


# =====================================Images===========================================================================

CentreImage = PhotoImage(file='centre.png')
LogoCentre = Button(ABC1b, image=CentreImage, bg='black', width=300, height=300)
LogoCentre.grid()

Image50_50 = PhotoImage(file='50_50.png')
Live50_50 = Button(ABC1a, image=Image50_50, bg='black', width=160, height=90, command=change50_50)
Live50_50.grid(row=0, column=0)

ImageAudience = PhotoImage(file='audience.png')
LiveAudience = Button(ABC1a, image=ImageAudience, bg='black', width=160, height=90, command=changeaudience)
LiveAudience.grid(row=0, column=1)

Image_PhoneA = PhotoImage(file='PhoneA.png')
LivePhoneA = Button(ABC1a, image=Image_PhoneA, bg='black', width=160, height=90, command=change_phone_a)
LivePhoneA.grid(row=0, column=2)

MillionaireImage = PhotoImage(file='millionair.png')
MillionImg = Button(ABC2, image=MillionaireImage, bg='black', width=430, height=600)
MillionImg.grid(row=0, column=0)

# =======================================Millionaire Questions==========================================================
Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()

Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()

Question1.set("Q1: What is 2 + 32")

Answer1.set("22")
Answer2.set("34")
Answer3.set("12")
Answer4.set("24")
'''correct_answer = "34"

if  correct_answer == textQuestion1.textarea="34":'''


def Question2():
    Question1.set("Q2: What is 32 + 32")
    Answer1.set("52")
    Answer2.set("32")
    Answer3.set("64")
    Answer4.set("87")
    million_picture1()


def Question3():
    Question1.set("Q3: What is 3 * 3")
    Answer1.set("12")
    Answer2.set("43")
    Answer3.set("8")
    Answer4.set("9")
    million_picture2()


def Question4():
    Question1.set("Q4: What is 300 / 3")
    Answer1.set("100")
    Answer2.set("20")
    Answer3.set("70")
    Answer4.set("110")
    million_picture3()


def Question5():
    Question1.set("Q4: What is 300 / 3")
    Answer1.set("100")
    Answer2.set("20")
    Answer3.set("70")
    Answer4.set("110")
    million_picture4()


# =======================================Texts,Label,Buttons============================================================

textQuestion = Entry(ABC1c, font=('arial', 18, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                     textvariable=Question1)
textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A:", bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)
textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                       justify=CENTER, textvariable=Answer1, command=Question5)
textQuestion1.grid(row=1, column=1, pady=4)

lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B:", bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                       justify=CENTER, textvariable=Answer2, command=Question2)
textQuestion2.grid(row=1, column=3, pady=4)

lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C:", bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionC.grid(row=2, column=0, pady=4, sticky=W)
textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                       justify=CENTER, textvariable=Answer3, command=Question3)
textQuestion3.grid(row=2, column=1, pady=4)

lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D:", bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionD.grid(row=2, column=2, pady=4, sticky=W)
textQuestion4 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                       justify=CENTER, textvariable=Answer4, command=Question4)
textQuestion4.grid(row=2, column=3, pady=4)

root.mainloop()
