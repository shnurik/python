
__author__ = 'Корнейчук Александр Николаевич'


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:
    def __init__(self, Name):
        self.Name = Name

    def full_name(self):
        sname = self.Name.split(" ")
        return sname[0] + " " + sname[1][0] + "." + sname[2][0] + "."


class Teacher(People):
    def __init__(self, Name, Subject):
        super().__init__(Name)
        self.Subject = Subject
        self.teachers_sub = {self.Name: self.Subject}


class Students(People):
    def __init__(self, Name, mother, father, ClassN):
        super().__init__(Name)
        self.mother = mother
        self.father = father
        self.ClassN = ClassN


class classes():
    def __init__(self, ClassN, *Name):
        self.Name = Name
        self.ClassN = ClassN


stud = [Students("Иванов Иван Иванович", "Петрова Петровна Петровична", "Сидоров Сидор Сидорович", "5А"),
        Students("Блажко Александр Иванович", "Цой Петровна Николаевна", "Бондаренко Андрей Андреевич", "5Б"),
        Students("Мартиросян Ксения Ивановна", "Терехов Сергей Александрович", "Терехова Александра Александровна", "5В"),
        Students("Маркова Наталья Сергеевна", "Чудный Денис Николаевич", "Пушкина Варвара Николаевна", "5Г"),
        Students("Измайлова Нина Николаевна", "Пайтон Петр Александрович", "Сидоров Анатолий Петрович", "5А"),
        Students("Исаев Юрий Иванович", "Исаев Петр Петрович", "Азизов Сидор Сидорович", "6А"),
        Students("Азизов Азиз Ахмедович", "Попов Петр Петрович", "Поддубный Сидор Сидорович", "7А"),
        Students("Мартышева Анна Ивановна", "Исаева Матрона Петровна", "Надеждин Сидор Сидорович", "6А"),
        Students("Попов Денис Викторович", "Менделеев Петр Петрович", "Галкин Сидор Сидорович", "5А"),
        Students("Попова Анна Викторовна", "Фетисов Петр Петрович", "Зверев Сидор Сидорович", "7Б"),
        Students("Поддубный Николай Ефимович", "Чудный Петр Петрович", "Блажко Сидор Сидорович", "6Б"),
        Students("Надеждин Николай Федорович", "Карась Петр Петрович", "Приходько Сидор Сидорович", "6В"),
        Students("Менделеев Сергей Анатольевич", "Максимов Петр Петрович", "Макаров Сидор Сидорович", "6В"),
        Students("Лермонтов Павел Николаевич", "Печка Петр Петрович", "Мухамед Сидор Сидорович", "5А"),
        Students("Алушкин Петр Петрович", "Киркоров Петр Петрович", "Николаев Сидор Сидорович", "5А"),
        Students("Пивоваров Антон Геннадиевич", "Принт Петр Петрович", "Неживой Сидор Сидорович", "5А"),
        Students("Глушко Анастасия Михайловна", "Мартиросян Петр Петрович", "Фетисовый Сидор Сидорович", "5А"),
        Students("Крепыш Федр Николаевич", "Путин Петр Петрович", "Песков Сидор Сидорович", "5А"),
        Students("Петров Александр Александрович", "Медведев Петр Петрович", "Соловьев Сидор Сидорович", "5А"),
        Students("Малая Любовь Николавена", "Эрих Петр Петрович", "Маринов Сидор Сидорович", "7А"),
        Students("Зверев Сергей Петрович", "Внуков Петр Петрович", "Гринь Сидор Сидорович", "5А"),
        Students("Кирокоров Андрей Валерьевич", "Пронин Петр Петрович", "Перепечка Сидор Сидорович", "5А"),
        Students("Простой Виктор Анатольевич", "Максаков Петр Петрович", "Малинин Сидор Сидорович", "6А"),
        Students("Галкина Яна Николаевна", "Кронштадский Петр Петрович", "Великий Сидор Сидорович", "7А"),
        Students("Фетисов Николай Петрович", "Русский Петр Петрович", "Яковлев Сидор Сидорович", "7А")]

teach = [Teacher("Корнейчук Александра Николаевна", "Физика"),
         Teacher("Сорокина Анна Владимировна", "Физра"),
         Teacher("Фролова Виктория Николаевна", "Физика"),
         Teacher("Пушкин Сергей Николаевич", "Алгебра"),
         Teacher("Толстый Иван Петрович", "Математика"),
         Teacher("Амбросова Ирина Викторовна", "История"),
         Teacher("Неважная Александра Михайловна", "Русский"),
         Teacher("Небоскреб Наталья Ефимовна", "Иняз")]

class_sb = [classes("5", teach[3], teach[4], teach[5]),
            classes("6", teach[3], teach[4], teach[5], teach[6], teach[0]),
            classes("7", teach[3], teach[4], teach[5], teach[6], teach[1])]

print("Выбирите действие: \n 1. Получить полный список всех классов школы \n 2. Получить список всех учеников в указанном классе \n 3. Получить список всех предметов указанного ученика \n 4. Узнать ФИО родителей указанного ученика \n 5. Получить список всех Учителей, преподающих в указанном классе")
try:
    operation = "!"
    while operation != 0:
        operation = int(input("Введите номер операции: "))
        if operation == 1:
            class_list = []
            i = 0
            while i < len(stud):
                class_list.append(stud[i].ClassN)
                i += 1
            print(set(class_list))
        elif operation == 2:
            cls = input("Введите номер класса: ")
            print("Список учащихся в данном классе: ")
            for line in stud:
                if line.ClassN == cls:
                    print(line.full_name())
        elif operation == 3:
            name = input("Укажите ФИО ученика: ")
            for line in stud:
                if name == line.Name:
                    print("{}, учащихся {} класса \n Изучают предметы: ".format(name, line.ClassN))
                    for tch in class_sb:
                        if tch.ClassN == line.ClassN[0]:
                            for nameClas in tch.Name:
                                for nameTeach in teach:
                                    if nameClas.Name == nameTeach.Name:
                                        print(nameTeach.teachers_sub[nameTeach.Name])
                                        #print(nameTeach.teachers_sub) с учителями
        elif operation == 4:
            name = input("Укажите ФИО ученика: ")
            for line in stud:
                if name == line.Name:
                    print("Мама :", line.mother, "Папа: ", line.father)
        elif operation == 5:
            clas = input("Укажите класс, что бы получить список учителей: ")
            print("Учительский состав класса {}".format(clas))
            for line in class_sb:
                if clas[0] == line.ClassN:
                    for i in line.Name:
                        print(i.Name)
        elif operation == 0:
            break
        else:
            print("Неверная команда")
except ValueError:
    print("Неверная команда")
