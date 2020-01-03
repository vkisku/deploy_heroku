#Code to Configure Settings.py for deployment onto heroku
import os
import sys
import subprocess
class Django_Heroku_Deploy:
    def __init__(self, folder,environment=None):
        print(environment)
        self.enter_into_virtual_env(environment)
        self.folder=str(folder)
        print('Folder Name',self.folder)
        os.chdir(self.folder)

        self.filename="settings.py"
        #Install Required Packages
        self.modules=["django","django-heroku","heroku","gunicorn"]
        #for m in self.modules:
         #   self.install(m)
        self.update_settings()

        os.chdir("..")

        self.update_requirements()
        self.update_procfile() 
    
    def enter_into_virtual_env(self,environment):
        if environment is not None:
            if environment is not "None":
                print('Virtual environment Activating....')
                subprocess.call('workon '+environment,shell=True)


    def install(self,package):
        print(package,"Installing.....")
        subprocess.call("pip install "+package)

    def update_requirements(self):
        #Fetch all the modules and dumpp it to requirements.txt
        print('Requirements Updating...')
        subprocess.call("pip freeze > requirements.txt", shell=True)

    def list_virtual_env(self):
        vlist=subprocess.check_output("lsvirtualenv",shell=True)
        vlist=vlist.decode()
        vlist=vlist.split('\r\n')
        vlist=[x for x in vlist if x]
        #vlist=set(vlist)
        print(vlist)
        return vlist    

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


