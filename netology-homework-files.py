from pprint import pprint, pformat

# Чтение файла
with open('recipes.txt', encoding='utf8') as file:
    lines = list(line.split(" | ") for line in (lines.strip() for lines in file) if line)

cook_book = {}  # Книга рецептов
cook_book_line = {}  # Рецепт блюда в книге рецептов
ingredient_list = []  # Список для одного ингридиента
reciept = str()  # Рецепт
ingredients_amount = int()  # Количество ингредиентов
ingredient_line = {}  # Описание ингредиента
previous_line_length = int()  # Длина списка предыдущего цикла
current_line_count = int()  # Текущий номер цикла

get_shop_list_by_dishes = [] # Список блюда и количество людей для покупок продуктов
dish_name = str() # Название блюда
person_count = int() # Количество человек
food_list = {} # Список покупок


def main():  # Основная функция
    global reciept, current_line_count, previous_line_length, ingredients_amount, dish_name, person_count

    # ЗАДАЧА 1
    print('Список рецептов из файла: ')
    for line in lines:
        ingredient = {}  # Список ингридентов
        if len(line) == 1 and (previous_line_length == 0 or previous_line_length > 1):
            reciept = dish_define(cook_book_line, cook_book, reciept)
        elif len(line) == 1 and previous_line_length == 1:
            ingredients_amount = ingredient_count(ingredients_amount)
        elif 1 < len(line) <= ingredients_amount:
            ingredients_list(ingredient, line, reciept, cook_book, cook_book_line)
        previous_line_length = len(line)
        current_line_count += 1
    pprint(cook_book, width=100)
    print()

    # ЗАДАЧА 2
    get_dished_shop_list(cook_book)


# ЗАДАЧА №1
# Функция выбора блюда
def dish_define(cook_book_line, cook_book, reciept):
    reciept = ''.join(map(str, lines[current_line_count]))
    cook_book_line.update({reciept: []})
    cook_book.update(cook_book_line)
    return reciept


#  Функция определения количества ингридентов
def ingredient_count(ingredients_amount):
    count = ''.join(map(str, lines[current_line_count]))
    ingredients_amount = int(count)
    return ingredients_amount


# Функция определения ингридиентов для блюда
def ingredients_list(ingredient, line, reciept, cook_book, cook_book_line):
    ingredient_line = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
    ingredient.update(ingredient_line)
    for key, value in cook_book.items():
        if key == reciept:
            value.append(ingredient)
            cook_book_line.update({reciept: value})
            cook_book.update(cook_book_line)


# ЗАДАЧА №2
# Функция проверки введеных блюд и вывод результатов
def get_dished_shop_list(cook_book):
    dishes = [] # Лист со списком блюд
    dish_name = str() # Название блюда
    person_count = int() # Количество персон для приготовления блюд
    dishes_list = 0

    # Проверка введенных данных
    while dish_name != 'q':
        dish_name = str(input('Введите название блюда, пожалуйста (q - выйти): '))
        for key, value in cook_book.items():
            if key == dish_name:
                dishes.append(dish_name)
                dishes_list = 1
        if dishes_list == 0:
            print('Вы ввели не существующее блюдо, попробуйте еще раз ...')

    if dishes_list != 0:
        get_shop_list_by_dishes.append(dishes)
        person_count = int(input('Введите количество персон, пожалуйста: '))
        get_shop_list_by_dishes.append(person_count)

    # Вывод результатов
    food_list = {} # Список покупок
    for dish_name in get_shop_list_by_dishes[0]:
        # print(dish_name)
        for key, value in cook_book.items():
            if dish_name == key:
                # print(value)
                for cook_book_line in value:
                    quantity = int(cook_book_line['quantity'])
                    shop_list = {'measure': cook_book_line['measure'], 'quantity': (quantity * person_count)}
                    food_name = cook_book_line['ingredient_name']
                    if food_name in food_list:
                        quantity_exist = int(shop_list['quantity'])
                        quantity_current = int(cook_book_line['quantity'])
                        shop_list = {'measure': cook_book_line['measure'],
                                     'quantity': (quantity_exist + quantity_current * person_count)}
                        food_list.update({food_name: shop_list})
                    else:
                        food_list.update({food_name: shop_list})
    pprint(food_list, width=100)


main()
