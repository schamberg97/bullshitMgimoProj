class software:
	@staticmethod
	def run():
		pass
	@staticmethod
	def runShowTables():
		#подключаем библиотеку
		import xml.dom.minidom as minidom
		from sMenu import Menu
		
		#читаем XML из файла
		dom = minidom.parse("myShop.xml")
		dom.normalize()
		
		#Читаем таблицу
		def listTable(what):
		        pars=dom.getElementsByTagName(what)[0]
		        #Читаем элементы таблицы Materials
		        nodes=pars.getElementsByTagName("item")
		
		        #Выводим элементы таблицы на экран
		        for node in nodes:
		                id = node.getElementsByTagName("id")[0]
		                name = node.getElementsByTagName("name")[0]
		                print(id.firstChild.data, name.firstChild.data)
		
		menu_items=["Категории", "Цвета", "Адреса", "Материал", "Сезон", "Товар"]
		menu_actions=['category','color', 'city', 'material', 'season', 'product'] # Базу клиентов и заказов не предлагаем ;)
		menu_title="Смотреть таблицу"
		
		
		my_menu=Menu(menu_title, menu_items)
		choice=my_menu.get_user_choice()
		listTable(menu_actions[choice-1])
		
		
		
		# TODO: Задание 1. добавить чтение остальных таблиц - СДЕЛАНО (кроме базы клиентов и заказов)
		# TODO: Задание 2. добавить меню для вывода таблицы по запросу пользователя
