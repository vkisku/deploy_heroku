from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import time
import configparser
import os
import django_app_deploy as deploy

class App:
	def __init__(self, window, window_title, video_source=0):
		self.config = configparser.ConfigParser()
		self.scale = 100
		self.window = window
		self.window.geometry("500x200+300+300")
		self.window.title(window_title)
		self.directoryFlag=0
		self.envirormentName="None"

		self.label = Label(self.window,text="Follow the steps to deploy Django app to heroku").place(x=10,y=10)
		self.label1 = Label(self.window,text="1. Select Virtual Environment(Optional)").place(x=10,y=30)
		self.label2 = Label(self.window,text="2. Browse and select The Folder to your Project folder where settings.py is present").place(x=10,y=50)
		self.label3 = Label(self.window,text="3.Press Deploy").place(x=10,y=70)

		OptionList =deploy.Django_Heroku_Deploy.list_virtual_env(self)
		OptionList=OptionList[2:]
		OptionList.insert(0,self.envirormentName)
		self.variable = StringVar()
		self.variable.set(OptionList[0]) # default value
		#self.label3 = Label(self.window,text="Virtual Environment").place(x=10,y=90)
		#self.environmentOptions = OptionMenu(self.window, self.variable, *OptionList,command=self.get_environment_name).place(x=130,y=90)

		self.label3 = Label(self.window,text="Project Folder").place(x=10,y=130)
		self.folderbutton = Button(self.window,text="Browse Folder",width=12,height=1,command=self.get_dirname).place(x=120,y=130)
		self.folderSuccess = StringVar()
		self.folderError = StringVar()

		self.folderLabelSuccess = Label(self.window, fg='green', textvariable=self.folderSuccess).place(x=220,y=130)
		self.folderLabelError 	= Label(self.window, fg='red', textvariable=self.folderError).place(x=250,y=130)
		self.deploybutton = Button(self.window,text="Deploy",width=12,height=1,command=self.deploy).place(x=190,y=170)

		self.menubar = Menu(self.window)
		self.filemenu = Menu(self.menubar,tearoff = 0)
		self.filemenu.add_command(label='New',command=self.do_nothing)
		self.filemenu.add_command(label='Open',command=self.do_nothing)
		self.filemenu.add_command(label='Save',command=self.do_nothing)
		self.filemenu.add_command(label='Save As',command=self.do_nothing)
		self.filemenu.add_command(label='Close',command=self.do_nothing)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit",command=window.quit)
		self.menubar.add_cascade(label="File",menu=self.filemenu)
		self.window.config(menu=self.menubar)


		self.configuremenu=Menu(self.menubar,tearoff=0)
		#self.configuremenu.add_command(label='Edit',command=self.configure_window)
		self.menubar.add_cascade(label='Configure',menu=self.configuremenu)
		self.window.config(menu=self.menubar)
		# print(self.vid.background)
		self.barcode_current_data=""
		self.barcode_previous_data=""
		self.window.iconbitmap('favicon.ico')
		self.window.resizable(False, False)
		self.window.mainloop()
	
	def deploy(self):	
		if self.directoryFlag == 0:
			messagebox.showinfo("Alert", "Please Select Project Folder")
		elif self.directoryFlag == -1:
			messagebox.showinfo("ALert","Please Select Correct Project Folder")
		else:
			deploy.Django_Heroku_Deploy(self.folderSuccess.get(),self.envirormentName)
			messagebox.showinfo("Success","Success")
			print('Successfully Configured for Deployment.')
			self.window.quit()

	def do_nothing(self):
		print('do Nothing')	
		
	def get_environment_name(self,value):
		print('Environment=>',value)
		self.envirormentName=value
		return value

	def get_dirname(self):
		folder = askdirectory(initialdir = "/")
		if not any(fname.endswith('settings.py') for fname in os.listdir(folder)):
			self.folderSuccess.set("")
			self.folderError.set("Something Went Wrong!")
			self.directoryFlag=-1
		else:
			self.folderSuccess.set(folder)
			self.folderError.set("")
			self.directoryFlag=1
		#print(folder)		        
	
	def save_changes(self):
		self.cStatus()
		self.Batch()
		self.sync_setting()
		messagebox.showinfo("Save Changes", "Changes Successfull saved!")	


App(Tk(), "Deploy Django App",0)