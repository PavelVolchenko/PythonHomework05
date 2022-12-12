""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """

string = 'зимбабве забвенный самозабвение стишок стимул забвение эмболия' \
         'слепая слепец стадия азалия акация алалия абвер идиотия'

result_string = string.split()
result_string = filter(lambda x: 'абв' not in x, result_string)
# result_string = filter(lambda x: (x.count('абв') != 1), string)  # альтернативная запись
print(f"Исходная строка: {string}")
print("Отформатированная строка:", end=' ')
print(*result_string)
