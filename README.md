#  StudyBuddy

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/PritamSuryawanshii/Last_Year_CollegeProject.git

```

--> Move into the directory where we have the project files : 
```bash
cd studybuddy

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv { envname }

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```
`
⚠ Then, the development server will be started at 
```bash 
http://127.0.0.1:8000/
```
#


## 💻 If You Want To Create New Django Project 
### --> Create a Django Project
```
django-admin startproject project_name
```



### --> Create a New App In Django Project
```
python manage.py startapp app_name
```
#### DON'T Forget to Register the App { name } in settings.py
