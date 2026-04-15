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

15- Let's Commit the changes to the repository and make first push to the remote repository using the following commands:
```
git add .
git commit -m "Initial commit: Set up Django project and app"
git push -u origin main
```
Now, I have successfully set up the Django project and app, and pushed the initial code to the GitHub repository.

I will commit every 2-3 steps to keep the commit history clean and organized.

16- I will start to add the models and views to the project and let's start with `BaseModel` model in `club_app/models.py`.

```
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```
This `BaseModel` will be an abstract model that other models can inherit from to automatically include `created_at` and `updated_at` fields.

17- We have 5 models to create: `Branch`, `Member`, `Trainer`, `GymClass`, and `Equipment`. I will start with the `Branch` model.

```
class Branch(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```
and I will register the `Branch` model in the admin panel by adding the following code to `club_app/admin.py`:
```
from django.contrib import admin
from .models import Branch

admin.site.register(Branch)
```

18- I will make migrations and apply them to create the `Branch` model in the database using the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
We can now see the `Branch` model in the admin panel and we can add, edit, and delete branches from there.

19- Let's commit the changes to the repository:
```
git add .
git commit -m "Add BaseModel and Branch model, and register Branch in admin panel"
```

20- Let's create Our first view to display the list of branches. I will add the following code to `club_app/views.py`:
```
from django.shortcuts import render
from .models import Branch

def branches(request):
    branches = Branch.objects.all()
    return render(request, 'branches.html', {'branches': branches})
```
and I will add the following code to `club_app/urls.py`:
```
from django.urls import path
from . import views

urlpatterns = [
    path('branches/', views.branches, name='branches'),
]
```
and I will include the `club_app` URLs in the main `urls.py` of the project by adding the following code to `peak_performance_club/urls.py`:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('club_app.urls')),
]
```

21- I will create a template called `branches.html` in the `club_app/templates` directory to display the list of branches. The content of the `branches.html` file will be:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Branches</title>
</head>
<body>
    <h1>Branches</h1>
    <ul>
        {% if not branches %} 
            <li>No branches found</li> 
        {% endif %}
        
        {% for branch in branches %}
            <li>{{ branch.name }} - {{ branch.location }} - {{ branch.contact }}</li>
        {% endfor %}
    
    </ul>
</body>
</html>
```
and I will navigate to `http://127.0.0.1:8000/branches/` to check if the view is working correctly.

22- Let's commit the changes to the repository:
```
git add .
git commit -m "Add branches view and template to display list of branches"
```
Now we have successfully created the `Branch` model, registered it in the admin panel, created a view to display the list of branches, and created a template for that view. We have also committed all the changes to the repository.

23- Let's create the remaining models: `Member`, `Trainer`, `GymClass`, and `Equipment` in the `club_app/models.py` file. I will add the following code:
```
class Member(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Trainer(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GymClass(BaseModel):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    members = models.ManyToManyField(Member, related_name='classes')
    
    def __str__(self):
        return self.name

class Equipment(BaseModel):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_damaged = models.BooleanField(default=False)

    def __str__(self):
        return self.name
```
and I will make migrations and apply them to create the new models in the database using the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
and I will register the new models in the admin panel by adding the following code to `club_app/admin.py`:
```
from django.contrib import admin
from .models import Branch, Member, Trainer, GymClass, Equipment

admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(GymClass)
admin.site.register(Equipment)
```
Now we can see all the new models in the admin panel and we can add, edit, and delete instances of these models from there.

24- Let's commit the changes to the repository:
```
git add .
git commit -m "Add Member, Trainer, GymClass, and Equipment models, and register them in the admin panel"
```

25- Let's create dummy data for our models using a script. I will create a new file called `generate_dummy_data.py` in the `src` directory and add the following code to it:
```
import random
from datetime import datetime, timedelta
from decimal import Decimal

from club_app.models import Branch, Member, Trainer, GymClass, Equipment


def run():
    # =====================
    # 🧹 OPTIONAL CLEAN RESET
    # =====================
    GymClass.objects.all().delete()
    Equipment.objects.all().delete()
    Member.objects.all().delete()
    Trainer.objects.all().delete()
    Branch.objects.all().delete()

    # =====================
    # 🏢 BRANCHES (10)
    # =====================
    branches = []
    for i in range(10):
        b = Branch.objects.create(
            name=f"Branch {i+1}",
            location=random.choice(["Cairo", "Giza", "Nasr City", "Alex"]),
            contact=f"0100{i:07d}"
        )
        branches.append(b)

    # =====================
    # 👤 MEMBERS (10)
    # =====================
    members = []
    for i in range(10):
        m = Member.objects.create(
            name=f"Member {i+1}",
            phone=f"0111{i:07d}",
            branch=random.choice(branches),
            balance=Decimal(random.randint(100, 2000))
        )
        members.append(m)

    # =====================
    # 🏋️ TRAINERS (10)
    # =====================
    trainers = []
    specialties = ["Yoga", "CrossFit", "Zumba", "Bodybuilding", "HIIT"]

    for i in range(10):
        t = Trainer.objects.create(
            name=f"Trainer {i+1}",
            phone=f"0122{i:07d}",
            branch=random.choice(branches),
            specialization=random.choice(specialties)
        )
        trainers.append(t)

    # =====================
    # 🏋️ EQUIPMENT (10)
    # =====================
    equipment_names = [
        "Treadmill", "Bench Press", "Dumbbells", "Row Machine",
        "Bike", "Cable Machine", "Squat Rack", "Leg Press",
        "Elliptical", "Pull-up Bar"
    ]

    for i in range(10):
        Equipment.objects.create(
            name=equipment_names[i],
            branch=random.choice(branches),
            purchase_date=datetime.now().date() - timedelta(days=random.randint(30, 1000)),
            price=Decimal(random.randint(5000, 50000)),
            is_damaged=random.choice([False, False, False, True])  # mostly safe
        )

    # =====================
    # 🧘 GYM CLASSES (10)
    # =====================
    classes = []

    for i in range(10):
        gc = GymClass.objects.create(
            name=random.choice(["Yoga", "Zumba", "CrossFit", "HIIT"]),
            trainer=random.choice(trainers),
            start_date=datetime.now() + timedelta(days=random.randint(1, 30)),
            base_price=Decimal(random.randint(100, 1000))
        )
        classes.append(gc)

    # =====================
    # 🔗 MANY-TO-MANY (MEMBERS ↔ CLASSES)
    # =====================
    for gc in classes:
        enrolled_members = random.sample(members, k=random.randint(3, 7))
        gc.members.add(*enrolled_members)

    print("✅ Gym dummy data created successfully!")
```

This script (created with the help of `chatGPT`) will create 10 branches, 10 members, 10 trainers, 10 pieces of equipment, and 10 gym classes with random data. It will also randomly enroll members in gym classes.
To run this script, I will use the following command in the terminal (src directory):
```
python manage.py shell 
```
and then in the shell, I will execute the following code:
```
from generate_dummy_data import run
run()
```
and we can check the admin panel to see the newly created dummy data.

26- Let's commit the changes to the repository:
```
git add .
git commit -m "Add generate_dummy_data script to create dummy data for the models"
```

27- Let's create views for the home page annd all the models to display their data. I will add the following code to `club_app/views.py`:
```
from django.shortcuts import render
from .models import Branch, Member, Trainer, GymClass, Equipment

# Create your views here.

def home(request):
    context = {
        "branches": Branch.objects.all(),
        "members": Member.objects.all(),
        "trainers": Trainer.objects.all(),
        "classes": GymClass.objects.all(),
        "equipment": Equipment.objects.all(),
    }
    return render(request, "home.html", context)

def branches(request):
    context = {
        "branches": Branch.objects.all(),
    }
    return render(request, "branches.html", context)

def members(request):
    context = {
        "members": Member.objects.all(),
    }
    return render(request, "members.html", context)

def trainers(request):
    context = {
        "trainers": Trainer.objects.all(),
    }
    return render(request, "trainers.html", context)

def classes(request):
    context = {
        "classes": GymClass.objects.all()
    }
    return render(request, "classes.html", context)

def equipments(request):
    context = {
        "equipments": Equipment.objects.all(),
    }
    return render(request, "equipments.html", context)

```
and I will add the following code to `club_app/urls.py`:
```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("members/", views.members, name="members"),
    path("trainers/", views.trainers, name="trainers"),
    path("classes/", views.classes, name="classes"),
    path("branches/", views.branches, name="branches"),
    path("equipments/", views.equipments, name="equipments"),
]
```

28- I will create templates for each view in the `club_app/templates` directory.Starting with `base.html` which will be the base template for all other templates:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peak Performance Club</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```
and I will create templates for each view in the `club_app/templates` directory.
- `home.html`:
```
{% extends "base.html" %}

{% block content %}
    <h1>Welcome to Peak Performance Club</h1>
    <p>Explore our branches, members, trainers, classes, and equipment!</p>
{% endblock %}
```
- `branches.html`:
```
{% extends "base.html" %}

{% block content %}
    <h1>Branches</h1>
    <ul>
        {% if not branches %} 
            <li>No branches found</li> 
        {% endif %}
        
        {% for branch in branches %}
            <li>{{ branch.name }} - {{ branch.location }} - {{ branch.contact }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```
29- Let's Pause here and test the views and templates we created so far by navigating to the corresponding URLs in the browser:
- Home page: `http://127.0.0.1:8000/`
- Members page: `http://127.0.0.1:8000/branches/`

and commit the changes to the repository:
```
git add .
git commit -m "Add views and templates for home page and branches"
```
Now we have successfully created views and templates for the home page and branches. We can continue creating views and templates for the remaining models in the same way.

30- Let's create views and templates for the remaining models in the same way.  
- `members.html`:
```
{% extends "base.html" %}

{% block content %}
    <h1>Members</h1>
    <ul>
        {% if not members %} 
            <li>No members found</li> 
        {% endif %}
        
        {% for member in members %}
            <li>{{ member.name }} - {{ member.phone }} - {{ member.branch.name }} - ${{ member.balance }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```
- `trainers.html`:
```
{% extends "base.html" %}

{% block content %}
    <h1>Trainers</h1>
    <ul>
        {% if not trainers %} 
            <li>No trainers found</li> 
        {% endif %}
        
        {% for trainer in trainers %}
            <li>{{ trainer.name }} - {{ trainer.phone }} - {{ trainer.branch.name }} - {{ trainer.specialization }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```
- `classes.html`:
```
{% extends "base.html" %}

{% block content %}
    <h1>Classes</h1>
    <ul>
        {% if not classes %} 
            <li>No classes found</li> 
        {% endif %}
        
        {% for class in classes %}
            <li>{{ class.name }} - {{ class.trainer.name }} - {{ class.start_date }} - ${{ class.base_price }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```
- `equipments.html`:
```
{% extends "base.html" %}

{% block content %}
    <h1>Equipments</h1>
    <ul>
        {% if not equipments %} 
            <li>No equipments found</li> 
        {% endif %}
        
        {% for equipment in equipments %}
            <li>{{ equipment.name }} - {{ equipment.branch.name }} - {{ equipment.purchase_date }} - ${{ equipment.price }} - {% if equipment.is_damaged %}Damaged{% else %}Good{% endif %}</li>
        {% endfor %}
    </ul>
{% endblock %}
```
and I will navigate to the corresponding URLs in the browser to check if the views and templates are working correctly:
- Members page: `http://127.0.0.1:8000/members/`
- Trainers page: `http://127.0.0.1:8000/trainers/`
- Classes page: `http://127.0.0.1:8000/classes/`
- Equipments page: `http://127.0.0.1:8000/equipments/`

and commit the changes to the repository:
```
git add .
git commit -m "Add views and templates for members, trainers, classes, and equipments"
```
Now we have successfully created views and templates for all the models and we can see the data displayed correctly in the browser. We have also committed all the changes to the repository.

> And Now, we have a fully functional Django project with models, views, templates, and dummy data. We will continue to enhance the project by adding more features, improving the UI, and implementing additional functionalities.

So, Let's Push the changes to the remote repository before we continue with the next steps:
```
git push
```

Now, let's continue with the next steps of the project.

32- Add property to `Member` model:

```
class Member(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return self.name
    
    @property
    def is_vip(self):
        return self.balance > 1000
```
This property will return `True` if the member's balance is greater than 1000, indicating that they are a VIP member, and `False` otherwise.

So, Let's commit the changes to the repository:
```
git add .
git commit -m "Add is_vip property to Member model to determine if a member is a VIP based on their balance"
```

33- Add Custom QuerySet `trending` to `GymClass` model and `early_bird_price` method to calculate the price for early bird members for a gym class scheduled to start in more than 30 days:

```
class GymClassQuerySet(models.QuerySet):

    def trending(self):
        return self.annotate(num_members=models.Count('members')).filter(num_members__gt=5).order_by('-num_members')
    
class GymClassManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return GymClassQuerySet(self.model, using=self._db)
    
    def trending(self):
        return self.get_queryset().trending()
    

class GymClass(BaseModel):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    base_price = models.FloatField()
    members = models.ManyToManyField(Member, related_name='classes')

    objects = GymClassManager()

    def early_bird_price(self):
        if self.start_date > timezone.now() + timedelta(days=30):
            return round(self.base_price * 0.8) # self.base_price * 0.8
        return self.base_price
    
    def __str__(self):
        return self.name
```

Let's break down the changes we made to the `GymClass` model:

```
class GymClassQuerySet(models.QuerySet):

    def trending(self):
        return self.annotate(num_members=models.Count('members')).filter(num_members__gt=5).order_by('-num_members')
```
+ This is a custom `QuerySet` class for the `GymClass` model. It defines a method called `trending` that annotates each gym class with the number of members enrolled in it (`num_members`), filters the classes to include only those with more than 5 members, and orders them by the number of members in descending order.
+ Annotation means that we are adding a new field (`num_members`) to each `GymClass` instance in the queryset, which contains the count of related `Member` instances.

```
class GymClassManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return GymClassQuerySet(self.model, using=self._db)
    
    def trending(self):
        return self.get_queryset().trending()
```
+ This is a custom manager for the `GymClass` model. It overrides the `get_queryset` method to return an instance of `GymClassQuerySet`, which allows us to use the custom `trending` method directly from the manager.

```
class GymClass(BaseModel):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    base_price = models.FloatField()
    members = models.ManyToManyField(Member, related_name='classes')

    objects = GymClassManager()

    def early_bird_price(self):
        if self.start_date > timezone.now() + timedelta(days=30):
            return round(self.base_price * 0.8) # self.base_price * 0.8
        return self.base_price
    
    def __str__(self):
        return self.name
```
+ We set the `objects` attribute of the `GymClass` model to an instance of `GymClassManager`, which allows us to use the custom manager methods.
+ We added a method called `early_bird_price` that checks if the `start_date` of the gym class is more than 30 days in the future. If it is, it returns a discounted price (20% off the base price). Otherwise, it returns the regular base price.

So, we will edit the view of `classes` in `clubapp/views.py` to include the trending classes:
```
def classes(request):
    context = {
        "classes": GymClass.objects.all(),
        "trending_classes": GymClass.objects.trending(),
    }
    return render(request, "classes.html", context)
```
So, Let's commit the changes to the repository:
```
git add .
git commit -m "Add trending custom queryset to GymClass and early_bird_price method to calculate discounted price for early bird members"
```
34- Add Proxy Model `DamagedEquipment` to `Equipment` model to represent only the damaged equipment:

```
class EquipmentManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_damaged=True)
    
class DamagedEquipment(Equipment):
    objects = EquipmentManager()

    class Meta:
        proxy = True
        verbose_name = "Maintenance Alert"

```
This code defines a proxy model called `DamagedEquipment` that inherits from the `Equipment` model. The custom manager `EquipmentManager` overrides the `get_queryset` method to filter the equipment to include only those that are damaged (`is_damaged=True`). The `Meta` class specifies that this is a proxy model and gives it a verbose name of "Maintenance Alert".

* Let's add the proxy model to the `admin.py` file:
```
admin.site.register(DamagedEquipment)
```
* Let's make migrations and apply them using the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

* Let's commit the changes to the repository:
```
git add .
git commit -m "Add DamagedEquipment proxy model"
```

35- Let's edit our templates with the help of `chatGPT`. You can find the updated templates in the `templates` directory. I will replace the existing templates with the updated ones and commit the changes and push the changes to the repository:
```
git add .
git commit -m "Update templates with better styling and structure"
git push
```

Now, We have a full functional Django project with models, views, templates, and dummy data. 

+ We applied Some Useful Functions:
1. `BaseModel` abstract class to define common fields (created_at, updated_at) for all models.
2. `is_vip` method to determine if a member is a VIP based on their balance.
3. `early_bird_price` method to calculate discounted price for early bird members.
4. `trending` method to annotate each gym class with the number of members enrolled in it and filter the classes to include only those with more than 5 members.
5. `DamagedEquipment` proxy model to represent only the damaged equipment.

