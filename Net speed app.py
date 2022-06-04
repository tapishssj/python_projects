
from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+ " Mbps"
    up = str(round(sp.upload()/(10**6),3))+ " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("internet speed brrrr")
sp.geometry("500x700")
sp.config(bg="black")

lab = Label(sp,text= "Internet Speed Test", font=("Times",30,"bold"),bg="blue",fg="grey")
lab.place(x=55,y=40,height=80,width= 380) 

lab = Label(sp,text= "Download Speed", font=("Times",28,"bold"),bg="black",fg="yellow")
lab.place(x=55,y=130,height=50,width= 380) 

lab_down = Label(sp,text= "00 ", font=("Times",28,"bold"),bg="black",fg="yellow")
lab_down.place(x=55,y=200,height=50,width= 380) 

lab = Label(sp,text= "Upload Speed ", font=("Times",28,"bold"),bg="black",fg="yellow")
lab.place(x=55,y=290,height=50,width= 380) 

lab_up = Label(sp,text= "00", font=("Times",28,"bold"),bg="black",fg="yellow")
lab_up.place(x=55,y=360,height=50,width= 380) 

button = Button(sp,text='Start the test',font=("Times",28,"bold"),bg="grey",fg="white", relief=RAISED,command=speedcheck)
button.place(x=55,y=450,height=55,width= 380)

sp.mainloop() 
