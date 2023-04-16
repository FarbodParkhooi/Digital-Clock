# import library(s)
from tkinter import *
from time import sleep as sp
import time
import pyttsx3
# Create def
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clock)
def Timer():
    TimerWindow = Toplevel()
    Time = Entry(TimerWindow, width=50, borderwidth=5, bg='black', fg='white')
    def StartTimer():
        TimeG = Time.get()
        iTimeG = int(TimeG)
        firstLabel = Label(TimerWindow, text=iTimeG, bg='black', fg='white', font=('', 20))
        firstLabel.place(relx=0.40, rely=0.40)
        DigitalClockWindow.update_idletasks()
        sp(1)
        while iTimeG != 0:
            firstLabel.destroy()
            iTimeG -= 1
            iTimeGL = Label(TimerWindow, text=iTimeG, bg='black', fg='white', font=('', 20))
            iTimeGL.place(relx=0.40, rely=0.40)
            DigitalClockWindow.update_idletasks()
            sp(0.5)
            BlackL = Label(TimerWindow, text='', bg='black', padx=150, pady=150)
            BlackL.place(relx=0.40, rely=0.40)
            sp(0.5)
            iTimeGL.destroy()
        engine.say(text)
        engine.runAndWait()
    StartButton = Button(TimerWindow, text='Start', command=StartTimer, bg='black', fg='white', padx=140)
    StartButton.pack()
    Time.pack()
    TimerWindow.title('Timer')
    TimerWindow.geometry('390x240')
    TimerWindow.config(bg='black')
    TimerWindow.resizable(False,False)
    TimerWindow.mainloop()
# Create value
text = ".. Time Up! ."
engine = pyttsx3.init()
engine.setProperty('rate', 110)
DigitalClockWindow = Tk()
text_font= ("Boulder", 50, 'bold')
background = "black"
foreground= "white"
border_width = 65
label = Label(DigitalClockWindow, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
Button(DigitalClockWindow, text='Timer', command=Timer, bg='black', fg='white', borderwidth=3).grid(row=1, column=1)
# Window ability(s)
digital_clock()
DigitalClockWindow.title("Digital Clock") # New name
DigitalClockWindow.geometry("390x240") 
DigitalClockWindow.resizable(False,False)
DigitalClockWindow.config(bg='black')
DigitalClockWindow.mainloop()