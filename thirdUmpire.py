import tkinter
from tkinter.constants import ANCHOR
from functools import partial
import threading
import PIL
import cv2
from PIL import Image,ImageTk
import imutils
import time

stream = cv2.VideoCapture("VIDEO1.mp4")
def play(speed):
    print(f"You Clicked On Play. Speed is : {speed}")
    #play Video in Reverse Mode/Forward Mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame = stream.read()
    frame= imutils.resize(frame,width=Set_Width,height=Set_Height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame ,anchor=tkinter.NW)
    canvas.create_text(150,25,fill="yellow",font="Time 20 italic bold",text="Decision Pending")



def pending(decision):
    # Show decision Pending Image
    frame = cv2.cvtColor(cv2.imread("Pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=Set_Width,height=Set_Height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #Wait for 2 seconds
    time.sleep(2)

    #Show Sponsor image
    frame = cv2.cvtColor(cv2.imread("Sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=Set_Width,height=Set_Height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #wait for 1.5 seconds
    time.sleep(1.5)

    # Display Out or Not Out Image as Per Button Click
    # if args = "Out"
    if decision == "Out":
        DecisionImg = "out.png"
    else:
        DecisionImg = "notout.png"

    frame = cv2.cvtColor(cv2.imread(DecisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=Set_Width,height=Set_Height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)




def out():
    # Thread use for Secure our Software from Block or Hang when Frame change
    thread = threading.Thread(target=pending,args=("Out",))
    thread.daemon = 1
    thread.start()
    print("OUT")

def not_out():
    thread = threading.Thread(target=pending,args=("Not Out",)) 
    thread.daemon = 1
    thread.start()

    print("NOT OUT")

# main screen hight and width
Set_Width = 450
Set_Height = 250

#Tkinter Gui Starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit")

cv_img = cv2.cvtColor(cv2.imread("sq.jpeg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width=Set_Width,height=Set_Height)

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)

canvas.pack()

btn1 = tkinter.Button(window,text="<<< Previous (Fast)",width=63,command=partial(play,-25))
btn1.pack()

btn2 = tkinter.Button(window,text="<< Previous (Slow)",width=63,command=partial(play,-2))
btn2.pack()

btn3 = tkinter.Button(window,text="Next (Fast) >>>",width=63,command=partial(play,25))
btn3.pack()

btn4 = tkinter.Button(window,text="Next (Slow) >>",width=63,command=partial(play,2))
btn4.pack()


btn5 = tkinter.Button(window,text="Give Out",width=63,command=out)
btn5.pack()


btn6 = tkinter.Button(window,text="Give Not Out",width=63,command=not_out)
btn6.pack()


window.mainloop()

