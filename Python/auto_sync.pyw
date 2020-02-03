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
source = 'C:/Users/LENOVO/Downloads/'
destination = 'C:/Users/LENOVO/Downloads/to/'
doc_list=['doc','docx','txt','text','pdf','csv','xls','xlsx']
image_list=['jpg','jpeg','png','mp4','mkv','ico','svg']
zip_list=['zip','rar','gz']
sql_list=['sql']
exe_list=['exe','msi']
programming_list=['py','js','c','cpp','ino']
while(1):
    for filename in os.listdir(source):
        if list(filter(filename.endswith, doc_list)) != [] :
            if not os.path.exists('to/doc'):
                os.mkdir('to/doc')
            shutil.move(source+filename, 'to/doc/'+filename)
        elif list(filter(filename.endswith, image_list)) != []:
            if not os.path.exists('to/image'):
                os.mkdir('to/image')
            shutil.move(source+filename, 'to/image/'+filename)
            
        elif list(filter(filename.endswith, zip_list)) != [] :
            if not os.path.exists('to/zip'):
                os.mkdir('to/zip')
            shutil.move(source+filename, 'to/zip/'+filename)
            
        elif list(filter(filename.endswith, sql_list)) != [] :
                    if not os.path.exists('to/sql'):
                        os.mkdir('to/sql')
                    shutil.move(source+filename, 'to/sql/'+filename)   
        elif list(filter(filename.endswith, exe_list)) != [] :
                    if not os.path.exists('to/exe'):
                        os.mkdir('to/exe')
                    shutil.move(source+filename, 'to/exe/'+filename)
        elif list(filter(filename.endswith, programming_list)) != [] :
                    if not os.path.exists('to/programming'):
                        os.mkdir('to/programming')
                    shutil.move(source+filename, 'to/programming/'+filename)

  
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
