import collections

 

# Инициализация "базы данных" питомцев

pets = {

    1: {

        "Мухтар": {

            "Вид питомца": "Собака",

            "Возраст питомца": 9,

            "Имя владельца": "Павел"

        },

    },

    2: {

        "Каа": {

            "Вид питомца": "Желторотый питон",

            "Возраст питомца": 19,

            "Имя владельца": "Саша"

        },

    },

    # и так далее

}

 

def create():

    last = collections.deque(pets, maxlen=1)[0]

    # Предполагается, что пользователь вводит информацию о новом питомце

    name = input("Введите имя питомца: ")

    pet_type = input("Введите вид питомца: ")

    age = int(input("Введите возраст питомца: "))

    owner_name = input("Введите имя владельца: ")

    pets[last + 1] = {name: {"Вид питомца": pet_type, "Возраст питомца": age, "Имя владельца": owner_name}}

 

def read(ID):

    if ID in pets:

        pet_info = pets[ID]

        for name, info in pet_info.items():

            print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}")

    else:

        print("Питомца с таким ID нет в базе данных.")

 

def update(ID):

    if ID in pets:

        # Предполагается, что пользователь вводит новую информацию о питомце

        name = input("Введите имя питомца: ")

        pet_type = input("Введите вид питомца: ")

        age = int(input("Введите возраст питомца: "))

        owner_name = input("Введите имя владельца: ")

        pets[ID] = {name: {"Вид питомца": pet_type, "Возраст питомца": age, "Имя владельца": owner_name}}

        print("Информация о питомце успешно обновлена.")

    else:

        print("Питомца с таким ID нет в базе данных.")

 

def delete(ID):

    if ID in pets:

        del pets[ID]

        print("Информация о питомце успешно удалена.")

    else:

        print("Питомца с таким ID нет в базе данных.")

 

def get_pet(ID):

    return pets.get(ID, False)

 

def get_suffix(age):

    if age % 10 == 1 and age != 11:

        return "год"

    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):

        return "года"

    else:

        return "лет"

 

def pets_list():

    print("Список питомцев:")

    for ID, pet_info in pets.items():

        for name, info in pet_info.items():

            print(f"ID: {ID}, Питомец: {name}, Вид: {info['Вид питомца']}, Возраст: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}, Владелец: {info['Имя владельца']}")

 

# Пример использования

command = ""

while command != "stop":

    command = input("Введите команду (create, read, update, delete, stop): ").strip().lower()

    if command == "create":

        create()

    elif command == "read":

        ID = int(input("Введите ID питомца: "))

        read(ID)

    elif command == "update":

        ID = int(input("Введите ID питомца: "))

        update(ID)

    elif command == "delete":

        ID = int(input("Введите ID питомца: "))

        delete(ID)

    elif command == "stop":

        print("Работа с базой данных завершена.")

    else:

        print("Некорректная команда.")

 

# После окончания работы вы можете вывести список питомцев

pets_list()