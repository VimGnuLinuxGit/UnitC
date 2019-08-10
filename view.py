#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# View software
#=======================
# License: GNU GPL(v2.0)
# Software version 1.0
#=======================

from tkinter import *
from tkinter import ttk
from menuApp import MenuApp
from listItemComboBox import ListItemComboBox



class View(MenuApp, ListItemComboBox):

    def __init__(self, master):
        ListItemComboBox.__init__(self) # input __init__ listItemComboBox
        MenuApp.__init__(self, master) # Input __init__ MenuApp


        # Labelframe, entry, button, combobox, label ---------------------------------------------------#
        self.guiApp = master
        self.guiApp.configure(background='tan')
        self.guiApp.title('Software unit conversion')
        self.guiApp.resizable(width=False, height=False)

        self.fontBButtonApp = ('Aria', 10, 'bold')
        self.fontBFrameApp = ('Aria', 9, 'bold')

        self.varComboBox = StringVar()
        self.varComboBox.set('Please select unit conversion')  

        self.joinItemComboBox = '\n'.join(self.listItemComboBox.keys()) # Keys listItemComboBox

        self.labelFrameInput = LabelFrame(self.guiApp, text='Input unit ',\
                font=self.fontBFrameApp, background='tan')
        self.labelFrameOutput = LabelFrame(self.guiApp, text='Output unit ',\
                font=self.fontBFrameApp, background='tan')

        self.entryUnit = Entry(self.labelFrameInput, background='wheat')
        self.buttonClear = Button(self.labelFrameInput, text='  Clear  ',\
                background='wheat', font=self.fontBButtonApp, command=self.cleanigInputOutput)

        self.comboBoxUnit = ttk.Combobox(self.labelFrameInput, state='readonly',\
                values=self.joinItemComboBox, textvariable=self.varComboBox, font=('Aria', 12))

        self.buttonUnitConvert = Button(self.labelFrameInput, text='Convert',\
                background='wheat', font=self.fontBButtonApp, command=self.unitConvert)

        self.textOutput =Text(self.labelFrameOutput, background='wheat', width=37,\
                stat='disable', height=5, font=('Aria', 12))

        self.labelFrameInput.grid(row=0, column=0, padx=5, pady=5, sticky='EW')
        self.labelFrameOutput.grid(row=1, column=0, padx=5, pady=5, sticky='EW')
        self.entryUnit.grid(row=0, column=0, padx=5, pady=2, sticky='NEWS')
        self.comboBoxUnit.grid(row=1, column=0, padx=5, pady=2, ipadx=16, sticky='NEWS')
        self.buttonClear.grid(row=0, column=1, padx=5, pady=2, ipadx=15, sticky='NEWS')
        self.buttonUnitConvert.grid(row=1, column=1, padx=5, pady=2, sticky='NEWS')
        self.textOutput.grid(row=0, column=0, padx=5, pady=5)


    # Functions --------------------------------------------------------------------------------------- #
    def cleanigInputOutput(self):
        self.entryUnit.delete('0', 'end')
        self.textOutput.configure(stat='normal')
        self.textOutput.delete('1.0', 'end')
        self.textOutput.configure(stat='disable')
        self.comboBoxUnit.configure(textvariable=self.varComboBox.set('')) # No character highlighting
        self.comboBoxUnit.configure(textvariable=self.varComboBox.set('Please select unit conversion'))

    def cleaningTextOutput(self):
        self.textOutput.configure(stat='normal')
        self.textOutput.delete('1.0', 'end')

    def tryCatch(self):
        self.cleaningTextOutput() # Normal Text
        self.textOutput.configure(foreground='red')
        entryUnitGet = self.entryUnit.get()
        chosenComboBItem = self.varComboBox.get()
        errorEntryUnit = 'Please enter your amount\nfor example:\n(1 or 1.1 or -1 or -1.1)'
        errorComboBox = 'Please select unit conversion.'
        errorEntryUComboB = errorEntryUnit +'\n'*2+errorComboBox

        if chosenComboBItem == 'Please select unit conversion':
            try:
                float(eval(entryUnitGet))
                self.textOutput.insert(END, errorComboBox)
                self.textOutput.configure(stat='disable')
            except:
                self.textOutput.insert(END, errorEntryUComboB)
                self.textOutput.configure(stat='disable')

        else:
            try:
                float(eval(entryUnitGet)) 
                return 'NoError' # No error entryUnit and comboBoxUnit
            except:
                self.textOutput.insert(END, errorEntryUnit)
                self.textOutput.configure(stat='disable')

    def unitConvert(self):
        if self.tryCatch() == 'NoError':
            for item in self.listItemComboBox.keys():
                if item == self.comboBoxUnit.get():
                    self.textOutput.insert(END, item +'\n'*2+\
                                        str(eval(self.entryUnit.get()+self.listItemComboBox[item])))
                    self.textOutput.configure(foreground='green', stat='disable')
                    break



if __name__ == '__main__':
    root = Tk()
    app = View(root)
    root.mainloop()
