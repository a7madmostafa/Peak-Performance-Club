# 🏋️ Peak Performance Club

A Django-based web application for managing a fitness club, including branches, members, trainers, classes, and equipment.

---

## 🚀 Overview

**Peak Performance Club** is an educational Django project that simulates a real-world gym management system.
It demonstrates how to design scalable Django applications using models, views, templates, and advanced ORM features.

---

## ✨ Features

* 🏢 Manage gym **Branches**
* 👤 Track **Members** and balances
* 🧑‍🏫 Manage **Trainers** and specializations
* 🧘 Organize **Gym Classes** with enrollments
* 🏋️ Monitor **Equipment** and maintenance status
* 🔥 Identify **Trending Classes** (based on members count)
* 💰 Apply **Early Bird Discounts**
* ⭐ Detect **VIP Members**
* ⚠️ Track **Damaged Equipment** using Proxy Models

---

## 🧠 Key Django Concepts Used

* Abstract Models (`BaseModel`)
* Custom QuerySets & Managers
* Model Properties (`@property`)
* Proxy Models
* Relationships:

  * ForeignKey
  * ManyToMany
* Django Admin customization
* Template inheritance

---

## 🏗️ Project Structure

```
Peak-Performance-Club/
│
├── venv/
├── src/
│   ├── peak_performance_club/
│   ├── club_app/
│   ├── templates/
│   ├── generate_dummy_data.py
│   └── manage.py
│
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/a7madmostafa/Peak-Performance-Club.git
cd Peak-Performance-Club
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate it

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django==6.0
```

### 5. Run migrations

```bash
cd src
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

---

## 🌐 Available Routes

| Page      | URL            |
| --------- | -------------- |
| Home      | `/`            |
| Branches  | `/branches/`   |
| Members   | `/members/`    |
| Trainers  | `/trainers/`   |
| Classes   | `/classes/`    |
| Equipment | `/equipments/` |
| Admin     | `/admin/`      |

---

## 🧪 Generate Dummy Data

To populate the database with sample data:

```bash
python manage.py shell
```

```python
from generate_dummy_data import run
run()
```

---

## 💡 Example Features in Code

### VIP Member

```python
@property
def is_vip(self):
    return self.balance > 1000
```

### Trending Classes

```python
GymClass.objects.trending()
```

### Early Bird Pricing

```python
def early_bird_price(self):
    if self.start_date > timezone.now() + timedelta(days=30):
        return self.base_price * 0.8
    return self.base_price
```

---

## 📸 Future Improvements

* Authentication system (login/register)
* Booking system for classes
* Payment integration
* Dashboard with analytics
* REST API using Django REST Framework
* Deployment (Railway / Render)

---

## 📚 Learning Purpose

This project is part of a hands-on learning journey to understand how Django works in real-world scenarios, from database design to UI rendering.

---

## 👨‍💻 Author

**Ahmad Mostafa**

* GitHub: https://github.com/a7madmostafa

---

## ⭐ Contributing

Feel free to fork the project and submit pull requests.

---

## 📄 License

This project is for educational purposes.
