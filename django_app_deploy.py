#Code to Configure Settings.py for deployment onto heroku
import os
import sys
import subprocess
class Django_Heroku_Deploy:
    def __init__(self, folder):
        self.folder=str(folder)
        print('Folder Name',self.folder)
        os.chdir(self.folder)

        self.filename="settings.py"
        #Install Required Packages
        self.modules=["django","django-heroku","heroku","gunicorn"]
        for m in self.modules:
            self.install(m)
        self.update_settings()

        os.chdir("..")

        self.update_requirements()
        self.update_procfile() 
    
    def install(self,package):
        print(package,"Installing.....")
        subprocess.call("pip install "+package)

    def update_requirements(self):
        #Fetch all the modules and dumpp it to requirements.txt
        print('Requirements Updating...')
        subprocess.call("pip freeze > requirements.txt", shell=True)

    def update_settings(self):
        print('Settings Updating......')                
        with open(self.filename, "r+") as f:
            line_found = any("django_heroku.settings(locals())" in line for line in f)
            if not line_found:
                f.seek(0, os.SEEK_END)
                f.write("\ndjango_heroku.settings(locals())\n") 
        
        #We read the existing text from file in READ mode
        with open(self.filename,"r") as f:
            line_found = any("import django_heroku" in line for line in f)
            if not line_found:
                src=open(self.filename,"r")
                fline="import django_heroku\n"    #Prepending string
                oline=src.readlines()
                #Here, we prepend the string we want to on first line
                oline.insert(0,fline)
                src.close()

                #We again open the file in WRITE mode 
                src=open(self.filename,"w")
                src.writelines(oline)
                src.close()

    def update_procfile(self):
        print('Procfile Updating.....')
        f = open("Procfile", "w")
        appname="todo"
        try:
            appname=sys.argv[1]
        except:
            pass
        f.write("web: gunicorn "+appname+".wsgi --log-file -")
        f.close()


