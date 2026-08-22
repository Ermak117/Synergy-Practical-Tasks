import datetime

# Прописываем список с днями недели;
days_week = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]


# Функция для определения дня недели;
def day_week(day, month, year):
    data = datetime.date(year, month, day)
    return days_week[data.weekday()]


# Функция для определения високосного года;
def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


# Функция для определения текущего возраста;
def current_age(day, month, year):
    current_date = datetime.date.today()
    your_age = current_date.year - year

    # Если день рождения ещё не наступил в этом году проверяем через условие
    if current_date.month < month:
        your_age = your_age - 1
    elif current_date.month == month and current_date.day < day:
        your_age = your_age - 1

    return your_age


# Цифры для "электронного табло"

numbers = {
    "0": ["***", "* *", "* *", "* *", "***"],
    "1": ["  *", "  *", "  *", "  *", "  *"],
    "2": ["***", "  *", "***", "*  ", "***"],
    "3": ["***", "  *", "***", "  *", "***"],
    "4": ["* *", "* *", "***", "  *", "  *"],
    "5": ["***", "*  ", "***", "  *", "***"],
    "6": ["***", "*  ", "***", "* *", "***"],
    "7": ["***", "  *", "  *", "  *", "  *"],
    "8": ["***", "* *", "***", "* *", "***"],
    "9": ["***", "* *", "***", "  *", "***"],
    " ": ["   ", "   ", "   ", "   ", "   "]
}


# Функция для прорисовки даты звёздочками
def date_output(day, month, year):
    # Формат ДД ММ ГГГГ
    # :02d означает, что число будет занимать 2 знака, например 5 -> 05
    # :04d означает, что год будет занимать 4 знака
    data_str = f"{day:02d} {month:02d} {year:04d}"

    # Высота цифр - 5 строк
    for line_height in range(5):
        result = ""

        for znak in data_str:
            # Берём готовую строку цифры переформатированную звездочками 
            result = result + numbers[znak][line_height] + "  "

        print(result)


# Основная программа
print("")
print("Введите дату рождения:")
print("")
# Запрашиваем ввод дня рождения 

day = int(input("День: "))
month = int(input("Месяц: "))
year = int(input("Год: "))

print("День недели:", day_week(day, month, year))

if leap(year):
    print("Високосный год: да")
else:
    print("Високосный год: нет")

print("Вам сейчас:", current_age(day, month, year))

print("")
print("Дата рождения на табло звёздочками:")
print("")
date_output(day, month, year)
print("")
