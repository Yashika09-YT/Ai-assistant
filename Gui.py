## install speechrecogntion and pyaudio library

from tkinter import*
from PIL import Image,ImageTk # pillow were used to convert the image jpg or png of any image 
import speech_to_text
import action 
root=Tk()
root.title("Ai Assistant")
root.geometry("706x1018")
#root.resizable(False,False) #these were used not resize the tkinter window
root.config(bg="#2E2E2E")

#ask function 
def ask():
  user_val=speech_to_text.speech_to_text()
  bot_val= action.Action(user_val)
  text.insert(END,'User----->'+user_val+"\n")
  if bot_val!=None:
     text.insert(END,"BOT<-----"+str(bot_val)+'\n')
  if bot_val == "ok Mam":
     root.destroy()

def send():
   send=entry.get()
   bot=action.Action(send)
   text.insert(END,'User----->'+send+"\n")
   if bot!=None:
     text.insert(END,"BOT<-----"+str(bot)+'\n')
   if bot == "ok Mam":
     root.destroy()

def del_text():
  text.delete('1.0','end')




# frame
frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#2E2E2E")
#grid or 
frame.grid(row=0,column=1,padx=55,pady=10)
# text lable
text_label = Label( frame,text="Ai Assistant",font=("Comic Sans MS", 14, "bold"),bg="#356696")  # Background color
text_label.grid(row = 0,column = 0, padx = 20,pady = 10)

#image
image=ImageTk.PhotoImage(Image.open("images/assistant.png"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

# adding a text widget
text=Text(root , font=('courier 10 bold'),bg="#356696")
text.grid(row=2, column=0)
text.place(x=90,y=475,width=375,height=100)

#entry widget 
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=600,width=350,height=30)


#button 1
Button1=Button(root,text='ASK' ,bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=110,y=650)

#button2
Button2=Button(root,text='Send' ,bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=350,y=650)


#button3
Button3=Button(root,text='Delete' ,bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
Button3.place(x=225,y=650)


root.mainloop()

