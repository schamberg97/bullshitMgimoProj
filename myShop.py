# подключаем библиотеку
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import random
import pandas as pd


def prettify(elem):
    """Форматирование для получения читабельного XML.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='\t')


class PRODUCT:
    # словари общие для всех экземпляров класса
    COLOR = {}
    SEASON = {}
    MATERIAL = {}

    def __init__(self, product, color, season, material):
        # конструктор, создает экземпляр класса
        # создаем поля из списка
        self.id = product[0]
        self.name = product[1]
        self.category = product[2]
        self.price = product[3]
        self.color = product[4]
        self.size = product[5]
        self.season = product[6]
        self.material = product[7]
        # Заполняем справочники
        PRODUCT.COLOR = color
        PRODUCT.SEASON = season
        PRODUCT.MATERIAL = material

    def __str__(self):
        # переопределяем метод для вывода на экран
        return '({}, {}, {}, {}, {}, {}, {}, {})'.format(self.id, self.name, self.category, self.price,
                                                         PRODUCT.COLOR[self.color], self.size,
                                                         PRODUCT.SEASON[self.season], PRODUCT.MATERIAL[self.material])


class ORDER:
    def __init__(self, order):
        # конструктор, создает экземпляр класса
        # создаем поля из списка
        self.id = order[0]
        self.product = order[1]
        self.customer = order[2]
        self.date = order[3]

    def __str__(self):
        # переопределяем метод для вывода на экран
        return '({}, {}, {}, {})'.format(self.id, self.product, self.customer, self.date)


class CUSTOMER:
    # словарь общий для всех экземпляров класса
    CITIES = {}

    def __init__(self, customer, city):
        # конструктор, создает экземпляр класса
        # создаем поля из списка
        self.id = customer[0]
        self.firstname = customer[1]
        self.lastname = customer[2]
        self.age = customer[3]
        self.sex = customer[4]
        self.address = customer[5]
        CUSTOMER.CITIES = city

    def __str__(self):
        # переопределяем метод для вывода на экран
        return '({}, {}, {}, {}, {}, {})'.format(self.id, self.firstname, self.lastname, self.age,
                                                 self.sex, CUSTOMER.CITIES[self.address])


class CATEGORY:

    def __init__(self, category):
        # конструктор, создает экземпляр класса
        # создаем поля из списка
        self.id = category[0]
        self.name = category[1]
        self.parent = category[2]

    def __str__(self):
        # переопределяем метод для вывода на экран
        return '({}, {}, {})'.format(self.id, self.name, self.parent)


class MyShop:
    def __init__(self, filename):
        # читаем XML из файла
        dom = minidom.parse(filename)
        dom.normalize()

        # Читаем таблицу Materials
        pars = dom.getElementsByTagName("materials")[0]

        # Читаем элементы таблицы Materials
        nodes = pars.getElementsByTagName("material")

        # Создаем словарь по таблице Material
        MATERIAL = {}
        for node in nodes:
            id = node.getElementsByTagName("id")[0]
            name = node.getElementsByTagName("name")[0]
            MATERIAL[int(id.firstChild.data)] = name.firstChild.data
        # Аналогично нужно создать словари COLOR, SEASON, ADDRESS
        COLOR = {1: 'red', 2: 'black', 3: 'black', 4: 'black'}
        SEASON = {1: 'winter', 2: 'summer', 3: 'black', 4: 'black'}

        # Читаем таблицу Products
        pars = dom.getElementsByTagName("products")[0]

        # Читаем элементы таблицы Products
        nodes = pars.getElementsByTagName("product")

        # Создаем экземпляры классов Product
        self.product = {}

        for node in nodes:
            list = []  # создаем пустой список чтобы записать в него новый товар
            # читаем поля товара из БД
            list.append(int(node.getElementsByTagName("id")[0].firstChild.data))
            list.append(node.getElementsByTagName("name")[0].firstChild.data)
            list.append(int(node.getElementsByTagName("category")[0].firstChild.data))
            list.append(float(node.getElementsByTagName("price")[0].firstChild.data))
            list.append(int(node.getElementsByTagName("color")[0].firstChild.data))
            list.append(node.getElementsByTagName("size")[0].firstChild.data)
            list.append(int(node.getElementsByTagName("season")[0].firstChild.data))
            list.append(int(node.getElementsByTagName("material")[0].firstChild.data))
            # Добавляем товар в список товаров как экземпляр класса PRODUCT
            self.product[list[0]] = PRODUCT(list, COLOR, SEASON, MATERIAL)

        # Аналогично нужно прочитать в классы ORDER, CUSTOMER, CATEGORY
        # Читаем таблицу Seasons
        pars = dom.getElementsByTagName("seasons")[0]

        # Читаем элементы таблицы Seasons
        nodes = pars.getElementsByTagName("season")

        # Создаем словарь по таблице Seasons
        SEASON = {}
        for node in nodes:
            id = node.getElementsByTagName("id")[0]
            name = node.getElementsByTagName("name")[0]
            SEASON[int(id.firstChild.data)] = name.firstChild.data

        # Читаем таблицу Colors
        pars = dom.getElementsByTagName("colors")[0]

        # Читаем элементы таблицы Colors
        nodes = pars.getElementsByTagName("color")

        # Создаем словарь по таблице Color
        COLOR = {}
        for node in nodes:
            id = node.getElementsByTagName("id")[0]
            name = node.getElementsByTagName("name")[0]
            COLOR[int(id.firstChild.data)] = name.firstChild.data

        # Читаем таблицу Cities
        pars = dom.getElementsByTagName("cities")[0]

        # Читаем элементы таблицы Cities
        nodes = pars.getElementsByTagName("city")

        # Создаем словарь по таблице Cities
        CITIES = {}
        for node in nodes:
            id = node.getElementsByTagName("id")[0]
            name = node.getElementsByTagName("name")[0]
            CITIES[int(id.firstChild.data)] = name.firstChild.data

        # Читаем таблицу Orders
        pars = dom.getElementsByTagName("orders")[0]

        # Читаем элементы таблицы Orders
        nodes = pars.getElementsByTagName("order")

        # Создаем экземпляры классов Order
        self.order = {}

        for node in nodes:
            list = []  # создаем пустой список чтобы записать в него новый товар
            # читаем поля товара из БД
            list.append(int(node.getElementsByTagName("id")[0].firstChild.data))
            list.append(int(node.getElementsByTagName("product")[0].firstChild.data))
            list.append(int(node.getElementsByTagName("customer")[0].firstChild.data))
            list.append(node.getElementsByTagName("date")[0].firstChild.data)
            # Добавляем товар в список товаров как экземпляр класса ORDER
            self.order[list[0]] = ORDER(list)

        # Читаем таблицу Customers
        pars = dom.getElementsByTagName("customers")[0]

        # Читаем элементы таблицы Customers
        nodes = pars.getElementsByTagName("customer")

        # Создаем экземпляры классов Customer
        self.customer = {}

        for node in nodes:
            list = []  # создаем пустой список чтобы записать в него новый товар
            # читаем поля товара из БД
            list.append(int(node.getElementsByTagName("id")[0].firstChild.data))
            list.append(node.getElementsByTagName("firstname")[0].firstChild.data)
            list.append(node.getElementsByTagName("lastname")[0].firstChild.data)
            list.append(node.getElementsByTagName("age")[0].firstChild.data)
            list.append(node.getElementsByTagName("sex")[0].firstChild.data)
            list.append(int(node.getElementsByTagName("address")[0].firstChild.data))

            # Добавляем товар в список товаров как экземпляр класса CUSTOMER
            self.customer[list[0]] = CUSTOMER(list, CITIES)

        # Читаем таблицу Orders
        pars = dom.getElementsByTagName("categories")[0]

        # Читаем элементы таблицы Orders
        nodes = pars.getElementsByTagName("category")

        # Создаем экземпляры классов Order
        self.category = {}

        for node in nodes:
            list = []  # создаем пустой список чтобы записать в него новый товар
            # читаем поля товара из БД
            list.append(int(node.getElementsByTagName("id")[0].firstChild.data))
            list.append(node.getElementsByTagName("name")[0].firstChild.data)
            list.append(int(node.getElementsByTagName("parent")[0].firstChild.data))
            # Добавляем товар в список товаров как экземпляр класса CATEGORY
            self.category[list[0]] = CATEGORY(list)

    def printProduct(self):
        # проходим п всем товарам
        for p in self.product:  # p пробегает все ключи словаря
            # выводим значение по ключу
            print(self.product[p])

    def saveXML(self, filename):
        # создаем корневой элемент
        data = ET.Element('myShop')
        # создаем таблицу Товары
        products = ET.SubElement(data, 'products')
        # Записываем в нее все товары
        for c in self.product:
            # Добавляем элемент Товар
            prod = ET.SubElement(products, 'product')
            # Добавляем поле к элементу Товар
            id = ET.SubElement(prod, 'id')
            id.text = str(c)
            # Добавляем поле к элементу Товар
            name = ET.SubElement(prod, 'name')
            name.text = self.product[c].name
            # Добавляем поле к элементу Товар
            category = ET.SubElement(prod, 'category')
            category.text = str(self.product[c].category)
            # Добавляем поле к элементу Товар
            price = ET.SubElement(prod, 'price')
            price.text = str(self.product[c].price)
            # Добавляем поле к элементу Товар
            color = ET.SubElement(prod, 'color')
            color.text = str(self.product[c].color)
            # Добавляем поле к элементу Товар
            size = ET.SubElement(prod, 'size')
            size.text = self.product[c].size
            # Добавляем поле к элементу Товар
            season = ET.SubElement(prod, 'season')
            season.text = str(self.product[c].season)
            # Добавляем поле к элементу Товар
            material = ET.SubElement(prod, 'material')
            material.text = str(self.product[c].material)
        # Преобразуем в читабельный XML
        md = prettify(data)
        # Записываем в файл
        myfile = open(filename, "w", encoding='utf8')
        myfile.write(md)

        # добавляем метод для генерации тестовых данных для списков товаров, клиентов и заказов (последних генерируем больше)

    def addSampleData(self, nProd, nCustomer, nOrder):
        maxProd = max(self.product) + 1
        for i in range(nProd):
            lst = []  # создаем пустой список чтобы записать в него новый товар
            # читаем поля товара из БД
            lst.append(maxProd)  # это и есть id
            lst.append("Товар_" + str(i))  # номер (= наименование) товара
            lst.append(random.choice(
                list(self.category.keys())))  # категория товара выбирается случайно из ключей категорий
            lst.append(random.randint(100, 100000))  # цена товара
            lst.append(random.choice(list(self.product[1].COLOR)))  # цвет товара
            lst.append(random.choice(["F", "M", "S", "XS", "L", "XL"]))  # размер товара
            lst.append(random.choice(list(self.product[1].SEASON)))  # сезон товара
            lst.append(random.choice(list(self.product[1].MATERIAL)))  # материал товара
            # Добавляем товар в список товаров как экземпляр класса PRODUCT
            self.product[lst[0]] = PRODUCT(lst, self.product[1].COLOR, self.product[1].SEASON,
                                           self.product[1].MATERIAL)
            maxProd = maxProd + 1  # номер следующего товара

        maxCustomer = max(self.customer) + 1
        for i in range(nCustomer):
            lst = []  # создаем пустой список для записи в него нового клиента
            # читаем поля клиента из БД
            lst.append(maxCustomer)  # это и есть id
            lst.append("Имя_" + str(i))  # firstname
            lst.append("Фамилия_" + str(i))  # lastname
            lst.append(random.randint(15, 100))  # возраст
            lst.append(random.choice(["F", "M"]))  # пол
            lst.append(random.choice(list(self.customer[1].CITIES)))  # адрес (=город)
            # Добавляем клиента в список пользователей как экземпляр класса CUSTOMER
            self.customer[lst[0]] = CUSTOMER(lst, self.customer[1].CITIES)
            maxCustomer = maxCustomer + 1  # номер следующего клиента

        maxOrder = max(self.order)
        for i in range(nOrder):
            lst = []  # создаем пустой список для внесения в него новых заказов
            # читаем поля клиента из БД
            lst.append(maxOrder)  # это и есть id
            lst.append(
                int(random.choice(list(self.product.keys()))))  # товар выбирается случайно из ключей списка товаров
            lst.append(int(random.choice(
                list(self.customer.keys()))))  # покупатель выбирается случайно из ключей списка клиентов
            lst.append(str(random.randint(2010, 2019)) + "-" +
                       str(random.randint(00, 12)) + "-" + str(
                random.randint(00, 28)))  # дата без 29, 30, 31 чисел для удобств
            # Добавляем заказ в список заказов как экземпляр класса ORDER
            self.order[lst[0]] = ORDER(lst)
            maxOrder = maxOrder + 1  # номер следующего заказа

    def getTrainingData(self):
        """ так как мы их досоздали выше
        # Поскольку сейчас у нас нет заказов (не реализован шаг 3), то добавим просто случайные данные
        # если реализован этот шаг, то этот код нужно будет удалить
        order = {}
        for i in range(1500):
            order[i + 1] = [i + 1, random.choice(list(self.product)), random.randint(1, 30)]
        # Поскольку сейчас у нас нет клиентов (не реализован шаг 3), то добавим просто случайные данные
        # если реализован этот шаг, то этот код нужно будет удалить
        customer = {}
        for i in range(30):
            customer[i + 1] = [i + 1, random.randint(18, 65), random.choice([0, 1]),
                               random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
        """

        # Списки для хранения тренировочных данных
        pName = []
        pCategory = []
        pPrice = []
        pColor = []
        pSeason = []
        pMaterial = []

        cAge = []
        cSex = []
        cAddress = []

        # Проходим по всем заказам
        for i in self.order:
            # Выбираем из таблицы Товары товар по номеру из Заказа и добавляем поля в список
            pName.append(self.product[self.order[
                i].product].name)  # добавляем часть product вместо [1], когда она определена!!!!!
            pCategory.append(self.product[self.order[i].product].category)
            pPrice.append(self.product[self.order[i].product].price)
            pColor.append(self.product[self.order[i].product].color)
            pSeason.append(self.product[self.order[i].product].season)
            pMaterial.append(self.product[self.order[i].product].material)

            # Выбираем из таблицы Клиенты клиента по номеру из Заказа и добавляем поля в список
            cAge.append(self.customer[self.order[i].customer].age)
            cSex.append(self.customer[self.order[i].customer].sex)
            cAddress.append(self.customer[self.order[i].customer].address)
        # переводим буквенные обозначения пола в числовое выражение
        cSex01 = []
        for i in cSex:
            if i == 'F':
                cSex01.append(0)
            else:
                cSex01.append(1)

        # Создаем фрейм данных
        df = pd.DataFrame({'name': pName, 'category': pCategory, 'price': pPrice, 'color': pColor, 'season': pSeason,
                           'material': pMaterial, 'age': cAge, 'sex': cSex01, 'address': cAddress})
        return df
