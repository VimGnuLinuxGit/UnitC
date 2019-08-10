#! /usr/bin/env python3
#-*- coding:utf-8 -*-
# Menu software
#=======================
# License: GNU GPL(v2.0)
# Software version 1.0
#=======================

from tkinter import *                                             



class MenuApp(object):

    def __init__(self, master):
        # MenuBar --------------------------------------------------------------------------------------#
        self.menuApp = master
        self.menuApp.title('MenuApp')
        self.menuApp.config(background='tan')
        self.fontBoldTop = ('Aria', 8, 'bold')
        self.fontBButtonMenuApp = ('Aria', 14, 'bold')
        self.intVarLanguage = IntVar()
        self.pictureMApp = PhotoImage(file='UnitC.png')
        self.menubar = Menu(self.menuApp, bg='tan')                                                           

        self.fileMenu = Menu(self.menubar, tearoff=0, background='tan')
        self.fileMenu.add_command(label='Exit', command=self.menuApp.destroy)
        self.menubar.add_cascade(label='File ', menu=self.fileMenu)

        self.heloMenu = Menu(self.menubar, tearoff=0, background='tan')
        self.heloMenu.add_command(label='Help', command=self.topHelp)
        self.heloMenu.add_command(label='About', command=self.topAbout)
        self.menubar.add_cascade(label='Help', menu=self.heloMenu)
        
        self.menuApp.configure(menu=self.menubar)


    # Menu function ------------------------------------------------------------------------------------#
    def topHelp(self):
        helpMassage = Toplevel()
        helpMassage.title('Help')
        helpMassage.resizable(width=False, height=False)
        labelHelp = Label(helpMassage, text=\
                'This is a small software\n'+\
                'unit conversion for\n'+\
                'civil engineering\n\n'+
                'Please send\n'+\
                'your comments and criticisms\n'+\
                'for the promotion\n'+\
                'of the software\n',\
                background='tan', font=self.fontBoldTop, compound=RIGHT, image=self.pictureMApp)
        labelHelp.pack()

    def topAbout(self):
        aboutMessage = Toplevel()
        aboutMessage.title('About')
        aboutMessage.resizable(width=False, height=False)
        labelAbout = Label(aboutMessage, text=\
                'Unit conversion civil engineering\n'+\
                'Version 1.0\n'+\
                'License: GPLv2\n\n'+\
                'Programmer info:\n'+\
                'Hasan Shirazi'+'\n'*4+\
                'Email:\nprogramming.gnulinux.0101@gmail.com\n',
                background='tan', font=self.fontBoldTop,  compound=RIGHT, image=self.pictureMApp)
        labelAbout.pack()



if __name__ == '__main__':
    root = Tk()
    app = MenuApp(root)
    root.mainloop()                                                                  
