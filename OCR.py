from PIL import Image
import pyocr

import tkinter as tk
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x600")
root.title("Camera App")

cap = cv2.VideoCapture(0)

def show_frame():
    ret, frame = cap.read()

    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)

    root.after(1, show_frame)
    
def take_picture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("picture.png", frame)
    cap.release()
    
# 撮影用のボタンを作成する
button = tk.Button(root, text="Take picture" , command=take_picture)
button.pack(padx=10, pady=10, side = tk.BOTTOM)

label = tk.Label(root)
label.pack()

show_frame()

root.mainloop()