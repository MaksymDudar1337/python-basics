# Проєкт: Система розрахунку вартості доставки
# Програма розраховує вартість доставки залежно від параметрів замовлення.

# Константи програми
BASE_PRICE: float = 50.0
PRICE_PER_KM: float = 8.0
PRICE_PER_KG: float = 12.0
REMOTE_SURCHARGE: float = 100.0

# Отримання інформації від користувача
print("====================================")
print(" СИСТЕМА РОЗРАХУНКУ ДОСТАВКИ")
print("====================================")

customer_name: str = input("Введіть ваше ім'я: ")

distance: float = float(input("Введіть відстань доставки (км): "))
weight: float = float(input("Введіть вагу посилки (кг): "))

delivery_type: str = input(
"Тип доставки (standard / express / pickup): "
).lower()

student_answer: str = input("Ви студент? (так/ні): ").lower()

# Перевірка статусу студента
is_student: bool = student_answer == "так"

# Перевірка введених даних
if distance <= 0 or weight <= 0:
print("Помилка! Відстань і вага повинні бути більшими за 0.")

else:
# Визначення типу доставки через match-case
match delivery_type:
case "standard":
delivery_multiplier: float = 1.0
delivery_name: str = "Стандартна доставка"

case "express":
delivery_multiplier = 1.5
delivery_name = "Експрес-доставка"

case "pickup":
delivery_multiplier = 0.5
delivery_name = "Самовивіз"

case _:
delivery_multiplier = 1.0
delivery_name = "Стандартна доставка"
print("Невідомий тип доставки. Обрано стандартну.")

# Математичний розрахунок
total = BASE_PRICE + distance * PRICE_PER_KM + weight * PRICE_PER_KG

# Застосування коефіцієнта доставки
total *= delivery_multiplier

# Вкладена умова
if distance > 20:
if weight > 10:
total += REMOTE_SURCHARGE
print("Додано надбавку за важку посилку на далеку відстань.")
else:
print("Доставка на далеку відстань.")

# Перевірка можливості отримання знижки
if is_student and total >= 200:
discount = total * 0.10
total -= discount
print("Вам нараховано студентську знижку 10%!")
elif total >= 500:
discount = total * 0.05
total -= discount
print("Вам нараховано знижку 5%.")
else:
discount = 0.0
print("Знижка не передбачена.")

# Логічні оператори AND, OR, NOT
if (distance <= 10 and weight <= 5) or not is_student:
category = "Звичайне замовлення"
else:
category = "Пільгове замовлення"

# Умовний вираз
delivery_message = "Швидка доставка!" if delivery_type == "express" else "Дякуємо за замовлення!"

# Визначення категорії вартості
if total < 150:
price_category = "Недорога доставка"
elif total < 400:
price_category = "Доставка середньої вартості"
else:
price_category = "Дорога доставка"

# Виведення результатів
print("\n========== РЕЗУЛЬТАТ ==========")
print(f"Клієнт: {customer_name}")
print(f"Тип доставки: {delivery_name}")
print(f"Відстань: {distance:.2f} км")
print(f"Вага посилки: {weight:.2f} кг")
print(f"Студент: {'Так' if is_student else 'Ні'}")
print(f"Категорія замовлення: {category}")
print(f"Сума знижки: {discount:.2f} грн")
print(f"Вартість доставки: {total:.2f} грн")
print(f"Категорія вартості: {price_category}")
print(delivery_message)
print("================================")
