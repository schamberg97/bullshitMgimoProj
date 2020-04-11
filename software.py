from my_shop import MyShop
from myBot import MYBOT
from sMenu import Menu

class software:
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
			
	@staticmethod
	def run():
		#Создаем магазин товаров
		myShop=MyShop("myShop.xml")
		#myShop.printProduct()
		
		#Добавляем тестовые данные
		myShop.addSampleData(200,2,2)
		#myShop.printProduct()
		myShop.saveXML("new.xml")
		
		#Создаем бота
		bot=MYBOT(myShop)
		#обучаем бота
		bot.botTraining(1)
		
		#получаем данные от пользователя
		print('Для выхода - нажмите Ctrl-C')
		sd=bot.getUserChoice()
		#строим рекомендацию и выводим рекомендованный товар
		print("Ваш рекомендованный товар: ",bot.getPrecigion(sd))