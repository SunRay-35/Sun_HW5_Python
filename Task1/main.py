# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print('Программа удаляет из строки слова, которые содержат в себе сочетание "абв"')

text = input('Введите строку: ')
words_in_text = text.split()
words_new = []

for word in words_in_text:
    if 'абв' not in word.lower():
        words_new.append(word)
        
words_new = ' '.join(words_new)
print(f'Новая строка: {words_new}')