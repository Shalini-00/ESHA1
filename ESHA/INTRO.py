from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time
import pygame  # pip install pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    #gif_path = "C:\\Users\\Anam Shaikh\\Desktop\\Front End Projects\\ESHA\\gif1.gif"

    # Enter the path to your GIF file
    img = Image.open("855.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    try:
        music_path = "music1.mp3"  # Enter the path to your music file
        mixer.music.load(music_path)  # Corrected variable name here
        mixer.music.play()
    except pygame.error as e:
        print("Error loading music file:", e)

    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((1000, 500))
        img_frame = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_frame)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()
