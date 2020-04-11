from sMenu import Menu
from aboutSoft import aboutSoft
from software import software

menu_items=["Об авторе", "О программе", "Вывести содержимое таблицы на экран", "Диалог", "Выход"]
menu_actions=[aboutSoft.showAuthorInfo, aboutSoft.showSoftInfo, software.runShowTables, software.run, aboutSoft.exit]
menu_title="Версия чатбота в терминале"

my_menu=Menu(menu_title, menu_items)

#my_menu.show_menu()
# В оригинале стоит, но на самом деле не нужно. Иначе лишний раз покажет меню
choice=my_menu.get_user_choice()
menu_actions[choice-1]()

# TODO: Задание 1. написать обработку для пунктов меню  -- СДЕЛАНО
# TODO: Задание 2. создать меню из пяти пунктов с обработкой -- СДЕЛАНО (но два пункта практически дублируют друг друга)
# TODO: Задание 3. создать массив обработчиков пунктов меню -- СДЕЛАНО