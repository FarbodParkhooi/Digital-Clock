# import library(s)
from tkinter import *
import time
# Create def
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clock)
def Timer():
    TimerWindow = Toplevel()
    # TimerWindow Options
    TimerWindow.geometry('390x200')
    TimerWindow.resizable(False,False)
    TimerWindow.mainloop()
# Create valu
DigitalClockWindow = Tk()
text_font= ("Boulder", 50, 'bold')
background = "black"
foreground= "white"
border_width = 65
label = Label(DigitalClockWindow, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
# Window ability(s)
digital_clock()
DigitalClockWindow.title("Digital Clock || Farbod")
DigitalClockWindow.geometry("390x200") 
DigitalClockWindow.resizable(False,False)
DigitalClockWindow.mainloop()