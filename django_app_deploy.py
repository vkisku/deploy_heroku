#Code to Configure Settings.py for deployment onto heroku
import sys
import subprocess
filename="settings.py"
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

modules=["django","django-heroku","heroku","gunicorn"]
for m in modules:
    install(m)
 
import os

with open(filename, "r+") as f:
    line_found = any("django_heroku.settings(locals())" in line for line in f)
    if not line_found:
        f.seek(0, os.SEEK_END)
        f.write("\ndjango_heroku.settings(locals())\n") 
        


#We read the existing text from file in READ mode
with open(filename,"r") as f:
    line_found = any("import django_heroku" in line for line in f)
    if not line_found:
        src=open(filename,"r")
        fline="import django_heroku\n"    #Prepending string
        oline=src.readlines()
        #Here, we prepend the string we want to on first line
        oline.insert(0,fline)
        src.close()
         
        #We again open the file in WRITE mode 
        src=open(filename,"w")
        src.writelines(oline)
        src.close()

#################################

f = open("Procfile", "w")
appname="todo"
try:
    appname=sys.argv[1]
except:
    pass
f.write("web: gunicorn "+appname+".wsgi --log-file -")
f.close()
