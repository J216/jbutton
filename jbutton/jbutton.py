#!/usr/bin/python3
import sys
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import subprocess
from subprocess import PIPE
import os

orig_pwd = os.path.abspath(os.curdir)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if len(sys.argv) < 2:
    command_string = "echo 'RED BUTTON!!!!!'"
else:
    command_string = str(sys.argv[1])

if len(sys.argv) < 3:
    btn_color = 'red'
else:
    btn_color = str(sys.argv[2])

class Window(Frame):
    window_title = "JButton"
    window_size = ""  #"427x630"
    icon_file = 'jsi-logo-64.png'

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.photos = []
        self.buttons = []
        self.labels = []
        self.processes = []
        # changing the title of our master widget
        self.master.title(self.window_title)
        #set window ico
        self.img = PhotoImage(file=self.icon_file)
        self.master.tk.call('wm', 'iconphoto', self.master._w, self.img)
        self.bind_all("<Control-q>", self.space_rats)
        #size of the window
        if self.window_size != "":
            self.master.geometry(self.window_size)
        # 'Entry' is used to display the input-field
        self.imageButton(fn="./"+btn_color+"-button.png", command=partial(self.runSubp, command_string)).grid(row = 0, column = 0, columnspan=5, padx=10, ipady=2)
    def imageButton(self,fn="",command=""):
        if command == "":
            command = self.space_rats
        if fn == "":
            fn = "./"+btn_color+"-button.png"
        b = Button(self.master,justify = LEFT,command=command)
        photo=PhotoImage(file=fn)
        b.config(image=photo)
        self.photos.append(photo)
        self.buttons.append(b)
        return b

    def showImage(self, fn=""):
        if fn == "":
            fn = "jsi-logo-64.png"
        load = Image.open(fn)
        render = ImageTk.PhotoImage(load)
        self.photos.append(render)
        # labels can be text or images
        img = Label(self.master, image=render)
        img.image = render
        self.labels.append(img)
        return img

    #Quit button function
    def space_rats(self, event=""):
        sys.exit(0)

    # Run command as subprocess
    def runSubp(self,commandString):
        #print(commandString)
        os.chdir(orig_pwd)
        p = subprocess.Popen("exec " +commandString, shell=True, stdout=PIPE)
        self.processes.append(p)
        out = str(p.communicate()[0])[2:-3].split('\\n')
        print(out[0])
        return out

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop() 


