from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import time
import configparser
import os
import django_app_deploy as deploy
import sys
import subprocess

class App:
	def __init__(self, window, window_title, video_source=0):
		self.config = configparser.ConfigParser()
		self.scale = 100
		self.window = window
		self.window.geometry("500x180+300+300")
		self.window.title(window_title)
		self.directoryFlag=0
		self.createdflag=0
		self.label = Label(self.window,text="Prerequisite: Pip should be installed.").place(x=10,y=10)
		self.label = Label(self.window,text="Follow the steps to create Virtual Environment").place(x=10,y=30)
		self.label1 = Label(self.window,text="1. Enter the Name of the Unique Virtual Environment").place(x=10,y=50)
		self.label2 = Label(self.window,text="2.Press Create").place(x=10,y=70)
		self.label2 = Label(self.window,text="Environment Name:").place(x=10,y=90)
		
		self.environment=StringVar()
		self.EnvironmentEntry = Entry(self.window,textvariable = self.environment,width=20).place(x=155,y=90)
		self.folderSuccess = StringVar()
		self.folderError = StringVar()

		self.folderLabelSuccess = Label(self.window, fg='green', textvariable=self.folderSuccess).place(x=150,y=90)
		self.folderLabelError 	= Label(self.window, fg='red', textvariable=self.folderError).place(x=150,y=90)
		
		OptionList =self.list_virtual_env()
		OptionList=OptionList[2:]
		self.variable = StringVar()
		self.variable.set(OptionList[0]) # default value
		self.environmentOptions = OptionMenu(self.window, self.variable, *OptionList,command=self.get_environment_name).place(x=10,y=110)
		self.deploybutton = Button(self.window,text="Create",width=12,height=1,command=self.list_virtual_env).place(x=190,y=130)

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
		self.window.mainloop()

	def list_virtual_env(self):
		vlist=subprocess.check_output("lsvirtualenv",shell=True)
		vlist=vlist.decode()
		vlist=vlist.split('\r\n')
		vlist=[x for x in vlist if x]
		#vlist=set(vlist)
		print(vlist)
		return vlist
		#if self.environment.get() in vlist:
		#	messagebox.showinfo('Alert','Environment ALready Exits.')

	def get_environment_name(self,value):
		print(value)
		return value

	def create(self):
		if(not(self.environment.get() and (self.environment.get()).strip())):
			messagebox.showinfo("Alert", "Enter The environment name!")
		else:
			self.createdflag=1
			print(self.environment.get())
			try:
				subprocess.call("pip install virtualenvwrapper",shell=True)
				subprocess.call("pip install virtualenv",shell=True)
				try:
					subprocess.call("mkvirtualenv "+self.environment.get(),shell=True)
					print("Environment",self.environment.get(),"created Successfully.")
					messagebox.showinfo("Success","Environment "+self.environment.get()+" created Successfully.")
				except Exception as e:
					print(e)
					
			except Exception as e:
				print(e)

			#self.window.quit()

	def do_nothing(self):
		print('do Nothing')
		
	
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


App(Tk(), "Virtual Environment Create",0)