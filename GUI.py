from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6f8faf")

# Ask function 

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, 'User--->' + user_val + "\n")
    if bot_val != None:
        text.insert(END, 'bot <---' + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

# send function

def send():
    send = entry.get()
    bot = action.action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot != None:
        text.insert(END, 'bot <---' + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

# delete text function

def del_text():
    text.delete("1.0", "end")

#frame

frame=LabelFrame(root, padx= 100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1, padx=55, pady=10)

#text Label

text_label = Label(frame, text="AI Assistant",font=('courier 15 bold'))
text_label.grid(row=0, column=0, padx=40, pady= 10)

#image

# image  = ImageTk.PhotoImage(Image.open("image/My Photo.jpg"))
# #resized_image=image.resize((300,205), Image.ANTIALIAS)
# image_lable=Label(frame , image=image)
# image_lable.grid(row=1,column=0,pady=20 ,padx=10)

#Text widget

text= Text(root, font=('courier 12 bold'),bg="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)

#entry widget

entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=375,height=40)

#button1

Button1 = Button(root, text="ASK ME",bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575 )

# button2

Button2 = Button(root, text="SEND",bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575 )

# button3

Button3 = Button(root, text="DELETE",bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575 )


root.mainloop()
