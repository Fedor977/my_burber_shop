# my_burger_shop/app/init_data.py
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine

# Создаем сессию
db = SessionLocal()

# Примеры бургеров
burgers = [
    {"name": "Cheeseburger", "description": "A delicious cheeseburger with cheddar cheese", "price": 5.99},
    {"name": "Hamburger", "description": "Classic hamburger with lettuce, tomato, and onion", "price": 4.99},
    {"name": "Bacon Burger", "description": "Burger with crispy bacon strips", "price": 6.99},
    {"name": "Veggie Burger", "description": "Healthy veggie burger with a mix of vegetables", "price": 5.49},
]

# Заполнение базы данных
for burger_data in burgers:
    burger = models.Burger(**burger_data)
    db.add(burger)

db.commit()  # Сохранение изменений в базе данных
db.close()  # Закрытие сессии
