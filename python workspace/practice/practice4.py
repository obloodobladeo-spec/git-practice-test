from tkinter import *

root = Tk()
root.title("Nado GUI") # title of the window
root.geometry("640x480") # size of the window

frame = LabelFrame(root, text="버튼")
frame.pack()

label1 = Label(frame, text="안녕하세요")
label1.pack() # put the label on the window

label2 = Label(frame, text="반갑습니다")
label2.pack()

txt1 = Entry(frame, width=30)
txt1.pack()

def change():
    name1 = txt1.get()
    label1.config(text=f"또 만나요, {name1}")

button1 = Button(frame, text="버튼1", command=change)
button1.pack()

root.mainloop()