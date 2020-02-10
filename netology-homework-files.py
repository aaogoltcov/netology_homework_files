from pprint import pprint, pformat

with open('recipes.txt', encoding='utf8') as file:
    lines = list(line.split(" | ") for line in (lines.strip() for lines in file) if line)
    # print(lines)
    # cook_book = {}
    # ingredient = {}
    # ingredient_line = {'ingredient_name': lines[2][0], 'quantity': lines[2][1], 'measure': lines[2][2]}
    # ingredient.update(ingredient_line)
    # ingredient_list = []
    # ingredient_list.append(ingredient)
    # ingredient_list.append(ingredient)
    # print(ingredient_list)
    #
    # reciept = ''.join(map(str, lines[0]))
    #
    # cook_book_line = {reciept: ingredient_list}
    #
    # cook_book.update(cook_book_line)
    #
    # print(ingredient_line)
    # print(ingredient)
    # print(cook_book)

    # key = 'id'
    # value = 'context'
    #
    # dictionary = {key: value}
    # key_1 = 'id-1'
    # value_1 = 'context-1'
    #
    # dictionary.update({key:''})
    # dictionary.update({key_1:[]})
    # print(dictionary)
    # dictionary.update({key_1:value_1})
    # print(dictionary['id-1'])

    # current_line_count = 0
    # previous_line_count = 0
    # previous_line_length = 0
    # # reciept = str()
    # cook_book_line = {}

    # for line in lines:
    #
    #     ingredient = {}
    #
    #     if len(line) == 1 and (previous_line_length == 0 or previous_line_length > 1):
    #         reciept = ''.join(map(str, lines[current_line_count]))
    #         cook_book_line.update({reciept: []})
    #         cook_book.update(cook_book_line)
    #         # print(reciept, ' ', current_line_count, ' ', previous_line_length, ' ', cook_book)
    #         current_line_count += 1
    #         previous_line_length = len(line)
    #
    #
    #     elif len(line) == 1 and previous_line_length == 1:
    #         # print(reciept, ' ', current_line_count, ' ', previous_line_length, ' ', cook_book)
    #         current_line_count += 1
    #         previous_line_length = len(line)
    #
    #
    #     elif len(line) > 1:
    #         ingredient_line = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
    #         ingredient.update(ingredient_line)
    #         for key, value in cook_book.items():
    #             if key == reciept:
    #                 value.append(ingredient)
    #                 # ingredient_list.append(ingredient)
    #                 cook_book_line.update({reciept: value})
    #                 cook_book.update(cook_book_line)
    #                 # print(reciept, ' ', current_line_count, ' ', previous_line_length, ' ', cook_book)
    #                 current_line_count += 1
    #                 previous_line_length = len(line)
    #
    # pprint(cook_book, width=100, sort_dicts=False)

cook_book = {}  # Книга рецептов
cook_book_line = {}  # Рецепт блюда в книге рецептов
ingredient_list = []  # Список для одного ингридиента
reciept = str()  # Рецепт
ingredients_amount = int()  # Количество ингредиентов
ingredient_line = {}  # Описание ингредиента
previous_line_length = int()  # Длина списка предыдущего цикла
current_line_count = int()  # Текущий номер цикла

get_shop_list_by_dishes = []
dish_name = str()
person_count = int()
food_list = {}


def main():  # Основная функция
    global reciept, current_line_count, previous_line_length, ingredients_amount, dish_name, person_count

    for line in lines:
        ingredient = {}  # Список ингридентов

        if len(line) == 1 and (previous_line_length == 0 or previous_line_length > 1):
            reciept = ''.join(map(str, lines[current_line_count]))
            dish_define(cook_book_line, cook_book, reciept)
            current_line_count += 1
            previous_line_length = len(line)


        elif len(line) == 1 and previous_line_length == 1:
            ingredient_count()
            count = ''.join(map(str, lines[current_line_count]))
            ingredients_amount = int(count)
            current_line_count += 1
            previous_line_length = len(line)


        elif len(line) > 1 and len(line) <= ingredients_amount:
            ingredients_list(ingredient, line, reciept, cook_book, cook_book_line)
            current_line_count += 1
            previous_line_length = len(line)

    pprint(cook_book, width=100, sort_dicts=False)


    get_dished_checking(cook_book)

    # get_dishes_return(cook_book, get_shop_list_by_dishes, person_count)



    # print(get_shop_list_by_dishes)
    # print(get_shop_list_by_dishes[0])
    # print(get_shop_list_by_dishes[1])





def dish_define(cook_book_line, cook_book, reciept):  # Функция выбора блюда
    cook_book_line.update({reciept: []})
    cook_book.update(cook_book_line)


def ingredient_count():  #  Функция определения количества ингридентов
    count = ''.join(map(str, lines[current_line_count]))
    ingredients_amount = int(count)
    return ingredients_amount


def ingredients_list(ingredient, line, reciept, cook_book,
                     cook_book_line):  # Функция определения ингридиентов для блюда
    ingredient_line = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
    ingredient.update(ingredient_line)
    for key, value in cook_book.items():
        if key == reciept:
            value.append(ingredient)
            cook_book_line.update({reciept: value})
            cook_book.update(cook_book_line)


def get_dished_checking(cook_book):
    dishes = []
    dish_name = str()
    person_count = int()
    dishes_list = 0
    while dish_name != 'q':
        dish_name = str(input('Введите название блюда, пожалуйста: '))
        for key, value in cook_book.items():
            if key == dish_name:
                dishes.append(dish_name)
                dishes_list = 1
        if dishes_list == 0:
            print('Вы ввели не существующее блюдо, попробуйте еще раз')

    if dishes_list != 0:
        get_shop_list_by_dishes.append(dishes)
        person_count = int(input('Введите количество персон, пожалуйста: '))
        get_shop_list_by_dishes.append(person_count)

    dish_name = str()
    food_name = str()
    shop_list = {}
    food_list = {}
    out_shop_list_by_dished = {}
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
                        shop_list = {'measure': cook_book_line['measure'], 'quantity': (quantity_exist + quantity_current * person_count)}
                        food_list.update({food_name: shop_list})
                    else:
                        food_list.update({food_name: shop_list})
                    # out_shop_list_by_dished.rupdate({dish_name: food_list})

                    # print(cook_book_line['ingredient_name'])
    # print(out_shop_list_by_dished)
    pprint(food_list, width=100, sort_dicts=False)

    # print(cook_book_line)
                    # print(value)
                # print(value(quantity))



main()

# cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
# }

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }