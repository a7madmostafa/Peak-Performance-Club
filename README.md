# Peak-Performance-Club
Educational Project in Django

> I will write all steps in sequence

1- I created a github repository for the project and named it "Peak-Performance-Club".

2- I opened VS Code in a new directory and made a clone for the repository using the following command in the terminal:
```bash
git clone https://github.com/a7madmostafa/Peak-Performance-Club.git
```

3- I opened the repo directory in VS Code and created a new virtual environment using the following command:
```
cd Peak-Performance-Club
python -m venv venv
```

4- I activated the virtual environment using the following command:
- For Windows:
```
venv\Scripts\activate
```
- For MacOS/Linux:
```
source venv/bin/activate
```

5- I installed Django in the virtual environment using the following command:
```
pip install django==6.0
```

6- I created a new directory called `src` in the root of the project to keep all the source code.
```
mkdir src
```

7- I navigated to the `src` directory and created a new Django project called `peak_performance_club` using the following command:
```
cd src
django-admin startproject peak_performance_club .
```

8- I created a new Django app called `club_app` using the following command:
```
python manage.py startapp club_app
```

9- I added `club_app` to the `INSTALLED_APPS` in the `settings.py` file of the project.

10- I tested the project by running the development server using the following command:
```
python manage.py runserver
```
and I opened the browser and navigated to `http://127.0.0.1:8000/` to see the default Django welcome page.

11- I opened a new terminal and navigated to the prohect directory and activated the virtual environment.
```
cd Peak-Performance-Club/src
venv\Scripts\activate
```

12- I made migrations for the `club_app` and applied them using the following commands:
```
python manage.py makemigrations 
python manage.py migrate
```

13- I created a superuser for the admin panel using the following command:
```
python manage.py createsuperuser
```

14- I navigated to `http://127.0.0.1:8000/admin/` to see the admin panel and logged in using the superuser credentials I created. I confirmed that the admin panel is working correctly.

15- Let's Commit the changes to the repository:
```
git add .
git commit -m "Initial commit: Set up Django project and app"
```