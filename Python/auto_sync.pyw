# Python program to explain shutil.move() method  
      
# importing os module  
import os  
  
# importing shutil module  
import shutil  
  
# path  
path = 'E:/Project/heroku_deploy/Python'
  
# List files and directories  
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'  
print("Before moving file:")  
print(os.listdir(path))  
  
  
# Source path  
source = 'E:/Project/heroku_deploy/Python/from/'
destination = 'E:/Project/heroku_deploy/Python/to/'
doc_list=['doc','docx','txt','text']
while(1):
	for filename in os.listdir(source):
		res = list(filter(filename.endswith, doc_list)) != [] 
		if res:
			if not os.path.exists('to/docs'):
				os.mkdir('to/docs')
			shutil.move(source+filename, 'to/docs/'+filename) 

  
# Destination path  

  
# Move the content of  
# source to destination  
#dest = shutil.move(source, destination)  
  
# List files and directories  
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"  
#print("After moving file:")  
#print(os.listdir(path))  
  
# Print path of newly  
# created file  
#print("Destination path:", dest) 