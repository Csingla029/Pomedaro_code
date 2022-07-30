
# ---------------------------- CONSTANTS ------------------------------- #
from tabnanny import check
import math
import tkinter
from tkinter import font
from urllib import response
from PIL import ImageTk,Image
from pkg_resources import working_set
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER",fg=GREEN)
    mark=""
    label2.config(text=mark)
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps = reps+1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if(reps%8==0):
        label.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif(reps%2==0):
        label.config(text="Break",fg=PINK)
        count_down(short_break_sec)    
    else:
        label.config(text="TIMER",fg=GREEN)
        count_down(work_sec) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_min>=0 and count_min<10:
        count_min ="0" + str(count_min)
    if count_sec>=0 and count_sec<10:
        count_sec ="0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# A canvas widget is lay things up on each other

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



label = tkinter.Label(text="Timer",font=("FONT_NAME",35),bg=YELLOW,fg=GREEN)
label.grid(column=1,row=0)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# create_image(x,y,image)
# here x y chosen sich that they are in centre
path="./pomodoro-start/tomato.png"
img_to = ImageTk.PhotoImage(Image.open(path))
canvas.create_image(100,112,image=img_to)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))

canvas.grid(column=1,row=1)


# count_down(5)

button1 = tkinter.Button(text="Start",bg="white",command=start_timer)
button1.grid(column=0,row=2)


button2 = tkinter.Button(text="Reset",command=reset_timer)
button2.grid(column=2,row=2)

label2=tkinter.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,13))
label2.grid(column=1,row=3)   


window.mainloop()