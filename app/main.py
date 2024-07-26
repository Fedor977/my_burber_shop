# my_burger_shop/app/main.py
from fastapi import FastAPI, Depends, Form  # Импорт необходимых модулей из FastAPI
from sqlalchemy.orm import Session  # Импорт Session для работы с базой данных
from . import models, schemas, crud  # Импорт модулей приложения
from .database import engine, SessionLocal  # Импорт движка базы данных и функции сессии
from fastapi.templating import Jinja2Templates  # Импорт Jinja2 для работы с шаблонами
from fastapi.responses import HTMLResponse  # Импорт HTMLResponse для рендеринга HTML
from fastapi import Request  # Импорт Request для работы с запросами

models.Base.metadata.create_all(bind=engine)  # Создание всех таблиц в базе данных

app = FastAPI()  # Инициализация приложения FastAPI
templates = Jinja2Templates(directory="app/templates")  # Указание директории с шаблонами

# Функция зависимости для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    burgers = crud.get_burgers(db)  # Получение всех бургеров из базы данных
    return templates.TemplateResponse("index.html", {"request": request, "burgers": burgers})  # Рендеринг шаблона с данными


@app.post("/add-to-cart")  # Маршрут для добавления бургера в корзину
def add_to_cart(burger_id: int = Form(...), quantity: int = Form(...), db: Session = Depends(get_db)):
    crud.add_to_cart(db, burger_id, quantity)  # Вызов функции для добавления в корзину
    return {"message": "Item added to cart"}  # Возвращает сообщение об успешном добавлении


@app.get("/cart", response_class=HTMLResponse)  # Маршрут для просмотра корзины
def view_cart(request: Request, db: Session = Depends(get_db)):
    cart_items = crud.get_cart_items(db)  # Получение элементов корзины из базы данных
    total_sum = sum(item.quantity * item.burger.price for item in cart_items)  # Расчет общей суммы заказа
    return templates.TemplateResponse("cart.html", {"request": request, "cart_items": cart_items, "total_sum": total_sum})  # Отправка шаблона с данными корзины

