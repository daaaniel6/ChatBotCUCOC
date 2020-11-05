#import cunocBot
from tkinter import *

raiz = Tk()
raiz.title("Bot CUNOC")
raiz.config(bg="Blue")


frame = Frame(raiz, width=500, height=400)
frame.pack()

labelBot= Label(frame,text= "Bot: " )
labelBot.grid(row = 1,column=1,sticky = "e",padx=20,pady=20)

labelUser= Label(frame,text= "Yo: " )
labelUser.grid(row = 2,column = 1,sticky = "e",padx=20,pady=20)

userText = Entry(frame)
userText.grid(row=2,column=2,padx=20,pady=20)



raiz.mainloop()