# my_burger_shop/app/crud.py
from sqlalchemy.orm import Session  # Импорт Session для работы с базой данных
from . import models  # Импорт моделей приложения


# Функция для получения всех бургеров из базы данных
def get_burgers(db: Session):
    return db.query(models.Burger).all()  # Запрос всех записей из таблицы burgers


def add_to_cart(db: Session, burger_id: int, quantity: int):  # Функция для добавления бургера в корзину
    item = db.query(models.CartItem).filter(
        models.CartItem.burger_id == burger_id).first()  # Поиск элемента корзины с указанным burger_id
    if item:  # Если элемент найден, увеличить количество
        item.quantity += quantity
    else:  # Если элемент не найден, создать новый
        item = models.CartItem(burger_id=burger_id, quantity=quantity)
        db.add(item)  # Добавить новый элемент в сессию
    db.commit()  # Сохранить изменения в базе данных
    db.refresh(item)  # Обновить объект item с новыми данными из базы
    return item  # Возвращает объект CartItem


def get_cart_items(db: Session):  # Функция для получения всех элементов корзины
    return db.query(models.CartItem).all()  # Возвращает все записи из таблицы cart_items


def update_cart_item(db: Session, cart_item_id: int,
                     quantity: int):  # Функция для обновления количества элемента корзины
    item = db.query(models.CartItem).filter(models.CartItem.id == cart_item_id).first()  # Поиск элемента корзины по id
    if item:  # Если элемент найден, обновить количество
        item.quantity = quantity
        db.commit()  # Сохранить изменения
        db.refresh(item)  # Обновить объект item
    return item  # Возвращает обновленный объект CartItem


def remove_from_cart(db: Session, cart_item_id: int):  # Функция для удаления элемента из корзины
    item = db.query(models.CartItem).filter(models.CartItem.id == cart_item_id).first()  # Поиск элемента корзины по id
    if item:  # Если элемент найден, удалить его
        db.delete(item)  # Удалить элемент из сессии
        db.commit()  # Сохранить изменения
