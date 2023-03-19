# import library(s)
from tkinter import *
import time
# Create def
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clock)
digital_clock()
def Timer():
    TimerWindow = Toplevel()
    None
# Create valu
DigitalClockWindow = Tk()
text_font= ("Boulder", 50, 'bold')
background = "black"
foreground= "white"
border_width = 65
label = Label(DigitalClockWindow, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
Button(DigitalClockWindow, text='Timer', command=Timer)
# Window ability(s)
DigitalClockWindow.title("Digital Clock") 
DigitalClockWindow.geometry("390x200") 
DigitalClockWindow.resizable(False,False)
DigitalClockWindow.mainloop()