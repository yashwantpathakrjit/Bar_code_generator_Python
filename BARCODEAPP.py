import tkinter as tk
from tkinter import Message, Text,messagebox
import cv2

import tkinter.ttk as ttk
import tkinter.font as font

from barcode import Code128

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

window = tk.Tk()
window.title("BarCodeGen")
dialog_title = 'QUIT'
window.geometry('1366x768')
window.configure()  # background='grey')
window.configure(background='Red')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message = tk.Label(window, text="Bar Code YP", bg="grey",
                   fg="black", width=50, height=3, font=('arial', 30, 'italic bold underline'))

message.place(x=80, y=20)

lbl = tk.Label(window, text="Library Card No", width=20, height=2,
               fg="white", bg="green", font=('times', 15, ' bold '))
lbl.place(x=400, y=200)

txt = tk.Entry(window, width=20, bg="green",fg="white", font=('times', 15, ' bold '))
txt.place(x=700, y=215)
lbl2 = tk.Label(window, text="Enroll No", width=20, fg="white",
                bg="green", height=2, font=('times', 15, ' bold '))
lbl2.place(x=400, y=300)
txt2 = tk.Entry(window, width=20, bg="green",
                fg="white", font=('times', 15, ' bold '))
txt2.place(x=700, y=315)



def TakeImages():
    number = txt.get()
    num2=txt2.get()


    my_code = Code128(number, writer=ImageWriter())

    if num2!="":
        my_code.save(num2)
    else:
        my_code.save(number)
    tk.messagebox.showinfo("done","click for next")
    txt2.delete(0,'end')
    txt.delete(0, 'end')
    res = ""
    message.configure(text=res)
    






takeImg = tk.Button(window, text="Genarate Code", command=TakeImages, fg="red", bg="yellow",
                    width=20, height=3, activebackground="Red", font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)

quitWindow = tk.Button(window, text="Quit", command=quit, fg="red", bg="yellow",
                       width=20, height=3, activebackground="Red", font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)


window.mainloop()
