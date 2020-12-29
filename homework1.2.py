# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_seconds = int(input('Введите время в секундах: '))

# minutes = time_seconds/60 с плавующей точкой получается надо делать округление, нашел функцию divmod,так проще
# print(f'Время в минутах: {minutes}')
# seconds = minutes//100
# print(seconds)

min, sec = divmod(time_seconds, 60)
hour, min = divmod(min, 60)

print(f'{hour:02}:{min:02}:{sec:02}')