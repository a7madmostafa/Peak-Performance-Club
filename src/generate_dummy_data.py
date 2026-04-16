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
            start_date=datetime.now() + timedelta(days=random.randint(5, 50)),
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