#!/usr/bin/env python3

import random
import pyautogui
import tkinter as tk

# Wordlist with sweares. All sweares should be on a new line.
wordlist_name = "sweares_en.txt"

LARGE_FONT = ("Comic Sans MS", 30)
SMALL_FONT = ("Comic Sans MS", 15)

WINDOW_TITLE = "F*cking SH*T MUTHAF*CKAAAAAA"

# We pick these randomly so the GUI is always shiny and different.
colors = ["red", "blue", "orange", "green", "purple"]


class ShitPoster(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.title(WINDOW_TITLE)

        # make window static
        self.resizable(width=False, height=False)
        self.geometry("400x400")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # set background image
        background_img = tk.PhotoImage(file="watchyourprofanity1.png")
        background_label = tk.Label(self,image=background_img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_img
        background_label.pack(pady=0, padx=0)

        # Create all buttons and sliders
        start_button = tk.Button(background_label, text="START", command=start_shit, highlightbackground="magenta", bg="cyan", fg=random.choice(colors), font=SMALL_FONT)
        start_button.pack(pady=(100, 0))

        stop_button = tk.Button(background_label, text="STOP", command=stop_shit, bg="black", activebackground="magenta", fg=random.choice(colors), font=SMALL_FONT)
        stop_button.pack()

        lbl = tk.Label(background_label, text="FASTER", bg="red")
        lbl.pack(pady=(20,0))
        speed_slider = tk.Scale(background_label, width=40, from_=50, to=5000, command=change_speed, bg="yellow", fg=random.choice(colors), font=SMALL_FONT)
        speed_slider.pack()
        lbl = tk.Label(background_label, text="SLOWER", bg="#cc0099")
        lbl.pack(pady=(0,20))


        lbl = tk.Label(background_label, text="oooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        lbl.pack(pady=100)

# global bool that determines whether to insult or not to insult
type_shit = False
# global speed that determines the speed to insult (lower is faster)
speed = 1000


def start_shit():
    global type_shit
    type_shit = True
    print('[*] info: started shit')


def stop_shit():
    global type_shit
    type_shit = False
    print('[*] info: stopped shit')


def change_speed(val):
    global speed
    speed = val
    print('[*] info: speed changed to {}'.format(val))

# get sweares
sweares = []

with open(wordlist_name) as f:
    sweares = f.readlines()

app = ShitPoster()


def task():
    if type_shit:
        shit_to_say = random.choice(sweares)
        pyautogui.typewrite(shit_to_say)
    global speed
    app.after(speed, task)

app.after(speed, task)
app.mainloop()
