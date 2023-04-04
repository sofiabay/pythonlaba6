countries = {'Россия': 'Москва', 'Италия': 'Рим', 'Польша': 'Варшава', 'Франция': 'Париж', 'Украина': 'Киев', 'Беларусь': 'Минск', 'Чехия': 'Прага', 'Дания': 'Копенгаген', 'Аргентина': 'Буэнос-Айрес', 'США': 'Вашингтон', 'Канада': 'Оттава'}
for key in countries:
  print(key, '-', countries [key])
capital=input("Введите старну:")
user=countries.get(capital)
  print(user)
list_keys = list(countries_keys())
list_keys.sort()
for i in list_keys:
  print(i, ':', countries[i])
