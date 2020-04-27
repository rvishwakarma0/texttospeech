import tkinter as tk
from gtts import gTTS
from playsound import playsound
###################for file name##########################
import os,uuid
def filename():
    
    cdate = str(uuid.uuid4())+"sound.mp3"   
    return os.path.join(os.getcwd(),cdate) 
######################################################
win=tk.Tk()
win.title("text to speech")
win.geometry("300x300")

def text_to_speech():
	text=entry.get()
	speech=gTTS(text=text,lang='en')
	filenameobj = filename()
	speech.save(filenameobj)
	playsound(filenameobj)

label=tk.Label(win,text="Enter Here: ")
label.grid(row=0,column=0)

entry=tk.Entry(win)
entry.grid(row=1,column=0)

button=tk.Button(win,text="Go",command=text_to_speech)
button.grid(row=1,column=1)
win.mainloop()