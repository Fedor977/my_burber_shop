# my_burger_shop/app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey  # Импорт необходимых типов данных
from .database import Base  # Импорт базового класса для моделей
from sqlalchemy.orm import relationship


# Модель бургера
class Burger(Base):
    __tablename__ = "burgers"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор бургера
    name = Column(String, index=True)  # Название бургера
    description = Column(String, index=True)  # Описание бургера
    price = Column(Float)  # Цена бургера


class CartItem(Base):  # Модель для хранения данных о товарах в корзине
    __tablename__ = "cart_items"  # Название таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор элемента корзины
    burger_id = Column(Integer, ForeignKey("burgers.id"))  # Идентификатор бургера, на который ссылается элемент корзины
    quantity = Column(Integer)  # Количество бургеров в корзине
    burger = relationship("Burger")  # Связь с моделью Burger для доступа к информации о бургере