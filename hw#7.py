# 1. Создать произвольный список =y
# 2. Добавить новый элемент типа str в конец списка =y
# 3. Добавить новый элемент типа int на место с индексом =y
# 4. Добавить новый элемент типа list в конец списка =yes
# 5. Добавить новый элемент типа tuple на место с индексом =
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка

# set = [1, 2, 3, 4, 5]
# set_extra = [149, "Hello", 2822]
# tuple = (100, 200, 300, 400, 500)
# set.append('String')
# set[2] = 23232
# set.append(set_extra)
# set[4] = (45, 56, 2, 78, 2)
# set.remove(1)
# set.count(2)
# print(set)

#Получите первый и последний элемент списка
# set = [24, "wow", 'w', 'ww2']
# print(set[0],set[-1])

#Проверить, есть ли в последовательности дубликаты
# list = [1, 1, 2, 3, 4, 5, 1, 6, 7, 7]
# set1 = set(list)
# if len(list) == len(set1):
#     print("Nope")
# else:
#     print('YES')

# Задача 1.4
# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением типа int
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу
# 6. Получить список ключей словаря

# dict = {
#     "book": [1, 2, 3],
#     "apple": 456,
#     "orange": 123
# }
# set = ["book", "apple", "orange"]
# set.append('string')
# set.append(132)
# tuple = (123, 234, 345, 456, 567, 678, 789, 890)
# list = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8]
# set.append(tuple)
# print(set)

#2.2. Представлено 2 выражения:
# А.
# lst_1 = [1, 5, 91]
# lst_2 = [1, 5, 91]
# Б.
# tpl_1 = (1, 5, 91)
# tpl_2 = (1, 5, 91)
# В чем разница между объектами в каждом из выражений?

#Ответ: Данные одинаковые, как помне нету разницы. К тому же в tuple нельзя менять значения

#Задача 3
# Продолжить код, с которым работали на уроке. Вывести имена студентов, которые старше 21

# students = [
#     {
#         'name': 'Ruslan',
#         'age': 20,
#         'gpa': 3.3
#     },
#     {
#         'name': 'Doki',
#         'age': 33,
#         'gpa': 2.8
#     },
# {
#         'name': 'Kent',
#         'age': 54,
#         'gpa': 5.0
#     }
#
# ]
#
# sum = 0
#Вывести имена студентов, которые старше 21.
# for i in students:
#     if i['age'] > 21:
#         print(i['name'])

#Задача 4
#Дана переменная Users(пользователи), которая является массивом состоящий из объектов (dictionaty).
# Каждый объект хранит в себе login(логин), password(пароль), name(имя), которые являются строкой.
# Нужно проверить все ли свойства заполнены у каждого объекта. Если хотя бы одно свойство отсутствует,
# то удалить этот объект с массива.

dict = {
    ""
}


