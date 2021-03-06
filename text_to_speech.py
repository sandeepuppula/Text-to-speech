from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to Speech")
root.geometry("800x500")


def talk():
    engine = pyttsx3.init()
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(00, END)


my_entry = Entry(root, font=("Helvetica",28))
my_entry.pack(pady = 20)

my_button = Button(root, text="Speak", command = talk)
my_button.pack(pady = 20)

root.mainloop()