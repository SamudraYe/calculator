#!/usr/bin/python

#import tkinter as tk
from tkinter import *

def frame(root, side):
    w = Frame(root)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w

#def button(root, side, text, command = None):
#    w = Button(root, text = text, command = command)
#    w.pack(side = side, expand = YES, fill = BOTH)
#    return w

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		#self.option_add('*Font', 'Courier 12')
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		
		display = StringVar()
		iptframe = frame(self, TOP)
		Label(iptframe, text="Input", width=10).pack(side=LEFT, expand=YES, fill=BOTH)
		Entry(iptframe, relief=SUNKEN, textvariable=display, width=22).pack(side=LEFT, expand=YES, fill=BOTH)
		
		result = StringVar()
		optframe = frame(self, TOP)
		Label(optframe, text="Output", width=10).pack(side=LEFT, expand=YES, fill=BOTH)
		Entry(optframe, relief=SUNKEN, textvariable=result, width=22).pack(side=LEFT, expand=YES, fill=BOTH)
		
		for key in ('123', '456', '789', '-0.'):
			keyframe = frame(self, TOP)
			for char in key:
				keybtn = Button(keyframe, text=char, width=10, command=lambda dp=display, c=char:dp.set(dp.get() + c))
				keybtn.pack(side=LEFT, expand=YES, fill=BOTH)
		
		operatorframe = frame(self, TOP)
		for char in '+-*/=':
			if char == '=':
				operatorbtn = Button(operatorframe, text=char, width=5)
				operatorbtn.pack(side=LEFT, expand=YES, fill=BOTH)
				operatorbtn.bind('<ButtonRelease-1>', lambda e, dp=display, rst=result:self.calc(dp, rst), '+')
				
			else:
				operatorbtn = Button(operatorframe, text=char, width=5, command=lambda dp=display, c='%s'%char:dp.set(dp.get() + c))
				operatorbtn.pack(side=LEFT, expand=YES, fill=BOTH)
				
		clearframe = frame(self, BOTTOM)
		clearbtn = Button(clearframe, text='clear', width=10, command=lambda dp=display, rst=result:self.clear(dp, rst))
		clearbtn.pack(side=LEFT, expand=YES, fill=BOTH)

	def calc(self, display, result):
		try:
			result.set(eval(display.get()))
		except:
			result.set("ERROR")
			
	def clear(self, display, result):
		display.set('')
		result.set('')

app=Application()
app.master.title("Sample application")
app.mainloop()