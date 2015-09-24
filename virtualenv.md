## Virtualenv


Virtualenv helps isolate python dependencies on a local machine on a project by project basis. Assuming you have pip, it should be available with:

pip install virtaulenv

More info is available here:
http://docs.python-guide.org/en/latest/dev/virtualenvs/

I did the following:

virtualenv project_directory

#To prevent using system level packages, could also do:
#virtualenv --no-site-packages project_directory

cd project_directory
source bin/activate

autoenv is an optional but handy utility that will activate the virtualenv automatically for you once you enter the directory. (I often forget this step.)
https://github.com/kennethreitz/autoenv


