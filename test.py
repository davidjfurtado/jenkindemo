import os
import smtplib
import sys
import time
from asyncore import ExitNow
from tkinter import *
from tkinter import messagebox
from turtle import color

from gtts import gTTS
from PIL import Image, ImageTk
from playsound import playsound

# server.sendmail('davidofffurtado@gmail.com',victimemail,tes)
global label3



def home():
	root.destroy()
	os.system("python test.py")	
	
		
	
	




		

root=Tk()
root.geometry("800x500")
root.geometry("+200+80")
root.configure(bg="white")





image2 = Image.open("security1.png")
resize_image = image2.resize((299, 97))
 
# Resize the image using resize() method
resize_image = image2
 
img2 = ImageTk.PhotoImage(resize_image)


label2 = Label(image=img2,bg="white")
label2.image2 = img2
label2.pack()


imagebtn1=PhotoImage(file="back2.png")



 
# create label and add resize image

#img = ImageTk.PhotoImage(Image.open("logo.png"))
#panel = Label(root, image = img)
#panel.place(x=10,y=8)



imagebtn2=PhotoImage(file="seedata.png")


global annc;
global annc2


annc=StringVar()
annc2=StringVar()




lab=Label(root,text="Enter Victim Email",foreground="white", background="black").place(x=525,y=140)
lab2=Label(root,text="Enter Phising Link",fg="white",bg="black").place(x=525,y=210)
txt2=Entry(root, relief=GROOVE, textvariable=annc, highlightthickness=1,highlightbackground = "#ffb703",highlightcolor= "green",width=35).place(x=525,y=170)
txt1=Entry(root, relief=GROOVE, textvariable=annc2, highlightthickness=1,highlightbackground = "#ffb703",highlightcolor= "green",width=35).place(x=525,y=240)







def sendmail():
	

	victimemail=annc.get()
	phisinglink=annc2.get()
	tes="""Hello Good Morning,
	Win cash prize of 1 Crore instantly.
	Login using your Facebook Account.
	Click Here to Login   .
	""" +phisinglink+""" """
	print("us link:",str(phisinglink))
	label2.pack_forget()

	server=smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login('davidofffurtado@gmail.com','iyumoxolaplrpjqn')
	server.sendmail('davidofffurtado@gmail.com',victimemail,tes)
	image3 = Image.open("bait.png")
	resize_image3 = image3.resize((299, 97))

	# Resize the image using resize() method
	resize_image3 = image3

	img3 = ImageTk.PhotoImage(resize_image3)


	label3 = Label(image=img3,bg="white")
	label3.image3= img3
	label2.pack_forget()
	print("mail sent")
	label3.pack()
	mytext = 'Bait Deployed.'  
	language = 'en'
	myobj = gTTS(text=mytext, lang="en", slow=False) 
	myobj.save("welcome.mp3") 
	
	playsound("welcome.mp3")
	
	

	
	btn=Button(root, image=imagebtn1, command=home,borderwidth=0, bg="#FA8139")
	btn.place(x=10,y=10)
Button(root, text="Attack", width=10, height=1, bg="orange",command=sendmail).place(x=590,y=290)
root.mainloop()
