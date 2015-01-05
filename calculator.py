from tkinter import *

root = Tk()

labelframe = Frame(root)
labelframe.grid()

keyframe = Frame(root)
keyframe.grid()

operatorframe = Frame(root)
operatorframe.grid()

clearframe = Frame(root)
clearframe.grid()

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		
	def createWidgets(self, master=None):		
		
		display = StringVar()
		Label(labelframe, text="Input", width=10).grid(row=0, column=0, sticky=W)
		Entry(labelframe, relief=SUNKEN, textvariable=display, width=22).grid(row=0, column=1, columnspan=3, sticky=W)
		result = StringVar()
		Label(labelframe, text="Output", width=10).grid(row=1, column=0, sticky=W)
		Entry(labelframe, relief=SUNKEN, textvariable=result, width=22).grid(row=1, column=1, columnspan=3, sticky=W)

		i=0
		#keyDict={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'.', 11:'-'}
		#for i, key in keyDict.items():
		for key in "1234567890-.":
			Button(keyframe, text=key, width=10, command=lambda dp=display, c=key:dp.set(dp.get() + c)).grid(row=i//3, column=i%3, padx=0)
			i = i+1
		
		j = 0
		for char in '+-*/=':
			if char == '=':
				operatorbtn = Button(operatorframe, text=char, width=5)
				operatorbtn.grid(row=0, column=j, ipadx=1, padx=1, sticky=W)
				operatorbtn.bind('<ButtonRelease-1>', lambda e, dp=display, rst=result:self.calc(dp, rst), '+')
				
			else:
				operatorbtn = Button(operatorframe, text=char, width=5, command=lambda dp=display, c='%s'%char:dp.set(dp.get() + c))
				if 0<j<5: px=2
				else: px=0
				operatorbtn.grid(row=0, column=j, ipadx=0, padx=px, sticky=W)
			
			j = j + 1

		clearbtn = Button(clearframe, text='clear', width=32, command=lambda dp=display, rst=result:self.clear(dp, rst))
		clearbtn.grid(ipadx=3)
	
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