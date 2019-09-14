import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os

HEIGHT = 500
WIDTH = 600
root = tk.Tk()
root.geometry('600x500')
#------------------------------- The Page you can select your projects ---------------------------------

class Source:
	def __init__(self, root):
		self.root = root
		self.root.title('My Journal')
		self.height = HEIGHT
		self.width = WIDTH
		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width)
		self.canvas.pack()

		self.image = Image.open('img/desktopapp/landscapesource.jpg')
		self.background_image = ImageTk.PhotoImage(self.image)
		self.background_label = tk.Label(self.root, image = self.background_image)
		self.background_label.place(relwidth = 1, relheight = 1)

		self.frame = tk.Frame(self.root, bg = '#80c1ff', bd = 1)
		self.frame.place(relx = 0.2, rely = 0.14, relwidth = 0.6, relheight = 0.65)

		self.listbox = tk.Listbox(self.frame, font=("Copperplate Gothic Light", 12), fg = 'red',
						 selectbackground = 'green', highlightthickness = 0)
		self.datesfile = open('dates.txt', 'r+')
		self.dates = self.datesfile.readlines()
		for date in self.dates:
			if '\n' in str(date):
				date = date.split('\n')
				date = date[0]
			self.listbox.insert('end', date[8:len(date)-4])
		self.listbox.place(relwidth = 1, relheight = 1)

		self.topframe = tk.Frame(self.root, bg = '#FFD133', bd = 5)
		self.topframe.place(relx = 0.2, rely = 0.8, relwidth = 0.6, relheight = 0.1)

		self.buttontowrite = tk.Button(self.topframe,text = 'Edit', command = lambda: self.changetowrite(),
									bg = 'green', font=("Copperplate Gothic Light", 14))
		self.buttontowrite.place(relx = 0.51, rely = 0.05, relheight = 0.9, relwidth = 0.47)

		self.buttontosource = tk.Button(self.topframe,text = 'Return', command = lambda: self.changetosignup(),
									bg = 'brown', font=("Copperplate Gothic Light", 14))
		self.buttontosource.place(relx = 0.02, rely = 0.05, relheight = 0.9, relwidth = 0.47)
	def changetowrite(self):
		clicked_item = self.listbox.curselection()
		thedate = self.listbox.get(clicked_item[0])
		f = open('daybook/' + thedate + '.txt', 'r')
		clicked_text = f.read()
		home = EditPage(self.root)
		home.edit(clicked_text, True, 'daybook/' + thedate + '.txt')
		self.topframe.destroy()
	def changetosignup(self):
		sign = SignUp(self.root)
		self.topframe.destroy()
 
	
#------------------------------- The initial Page of the app ---------------------------------

class SignUp:
	def __init__(self, root):
		self.root = root
		self.root.title('My Journal')
		self.height = 500
		self.width = 600
		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width)
		self.canvas.pack()

		self.image = Image.open('img/desktopapp/journal.jpg')
		self.image = self.image.resize((600,500), Image.ANTIALIAS)
		self.background_image = ImageTk.PhotoImage(self.image)
		self.background_label = tk.Label(self.root, image = self.background_image)
		self.background_label.place(relwidth = 1, relheight = 1)

		self.topframe = tk.Frame(self.root, bg = '#FFD133', bd = 5)
		self.topframe.place(relx = 0.275, rely = 0.8, relwidth = 0.45,
					relheight = 0.1)

		self.button_image = Image.open('img/desktopapp/buttonforward.png')
		self.background_button_image = ImageTk.PhotoImage(self.button_image)
		self.buttontowrite = tk.Button(self.topframe,text = 'Write', command = lambda: self.changetowrite(),
									bg = 'green', font=("Copperplate Gothic Light", 14))
		self.buttontowrite.place(relx = 0.51, rely = 0.05, relheight = 0.9, relwidth = 0.47)
	
		self.buttontosource = tk.Button(self.topframe,text = 'Source', command = lambda: self.changetosource(),
									bg = 'brown', font=("Copperplate Gothic Light", 14))
		self.buttontosource.place(relx = 0.02, rely = 0.05, relheight = 0.9, relwidth = 0.47)

	def changetowrite(self):
		home = EditPage(self.root)
		self.topframe.destroy()
	def changetosource(self):
		source = Source(self.root)
		self.topframe.destroy()

	
#------------------------------- The Page you can write your projects ---------------------------------

class EditPage:
	def __init__(self, root):
		self.iseditted = False
		self.data = []
		self.title = ''
		self.root = root
		self.root.title('My Journal')
		self.height = 500
		self.width = 600
		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width)
		self.canvas.pack()
	
		self.image = Image.open('img/desktopapp/landscape.jpg')
		self.background_image = ImageTk.PhotoImage(self.image)
		self.background_label = tk.Label(self.root, image = self.background_image)
		self.background_label.place(relwidth = 1, relheight = 1)

		self.topframe = tk.Frame(self.root, bg = '#80c1ff', bd = 1)
		self.topframe.place(relx = 0.125, rely = 0.18, relwidth = 0.75,
					relheight = 0.75)

		self.textimage = Image.open('img/desktopapp/textback.jpg')
		self.back_textimage = ImageTk.PhotoImage(self.textimage)
		self.textlabel = tk.Label(self.root, text = 'How was your day?', bg = '#006699',
						 fg = 'white', font = ("Eras Medium ITC", 12, 'italic'))
		self.textlabel.place(relx = 0.125, rely = 0.1, relheight = 0.07, relwidth = 0.75)

		self.text = tk.Text(self.topframe, font=("Eras Medium ITC", 12))
		self.text.place(relwidth = 0.96, relheight = 0.92)

		self.scrollbar = tk.Scrollbar(self.topframe)
		self.scrollbar.pack(side = 'right', fill = 'y')

		self.text.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.config(command = self.text.yview)

		self.button_image = Image.open('img/desktopapp/buttonbg.jpg')
		self.background_button_image = ImageTk.PhotoImage(self.button_image)
		self.button = tk.Button(self.topframe, text = 'Save it', state = 'active', 
						image = self.background_button_image, compound = 'center',
			 			command = lambda: self.createdaybook(self.text.get('1.0', 'end')), 
			 			font=("Copperplate Gothic Light", 14))
		self.button.place(relx = 0.5, rely = 0.93, relwidth = 0.245, relheight = 0.07)
		self.buttontosource = tk.Button(self.topframe,text = 'Return', command = lambda: self.changetosignup(),
									bg = 'brown', font=("Copperplate Gothic Light", 14))
		self.buttontosource.place(relx = 0.2, rely = 0.93, relwidth = 0.245, relheight = 0.07)
	
	def changetosignup(self):
		sign = SignUp(self.root)
		self.topframe.destroy()

	def createdaybook(self, entry):
		if self.iseditted:
			os.remove(self.edittedDate)
			with open('dates.txt', 'r') as file:
				lines = file.readlines()
			with open('dates.txt', 'w') as file2:
				for line in lines:
					if line.strip('\n') != self.edittedDate:
						if line != '\n':
							file2.write(line)
							print(line)

		self.newroot = tk.Tk()
		self.newcanvas = tk.Canvas(self.newroot, height = 100, width = 400)
		self.newcanvas.pack()

		self.newframe = tk.Frame(self.newroot, bg = '#80c1ff', bd = 2)
		self.newframe.place(relwidth = 1, relheight = 1)

		self.newlabel = tk.Label(self.newframe, text = 'Enter the Date as dd.mm.yyyy, leave "-", Enter the Time as hh.mm')
		self.newlabel.pack()

		self.entry = tk.Entry(self.newframe)
		self.entry.pack()

		self.newbutton = tk.Button(self.newframe, text = 'Set', command = lambda: self.settheTitle(self.entry.get()))
		self.newbutton.pack()

		if '\n' in str(entry):
			self.data.append(entry.split('\n'))
		self.text.delete('1.0', 'end')

			
	def settheTitle(self, entry):
		self.title = str(entry)
		self.newroot.destroy()
		self.title = 'daybook/' + self.title + '.txt'
		self.dates = open('dates.txt', 'a+')
		self.dates.write(self.title + '\n')
		self.dates.close()
		self.f = open(self.title, 'w+')
		self.f.write(self.data[0][0])
		self.f.close()
	def edit(self, clicked_text, editted, date):
		self.text.insert('1.0', clicked_text)
		self.iseditted = editted
		self.edittedDate = date

homepage = SignUp(root)

root.mainloop()