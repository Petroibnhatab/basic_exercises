# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(f'Последняя буква в слове {word}: {word[-1]}')

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
word = word.lower()
vol = 0
for i in word:
    if i == 'а':
        vol +=1

print(f'Количество букв "а" в слове {word}: {vol}')



# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
count = 0
set_g = ('аеёиуыэюя')
for i in word.lower():
    if i in set_g:
        count +=1
print(f'Количество гласных букв в слове {word}: {count}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(f'Количество слов в предложении: "{sentence}" - {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
v = sentence.split()
vol = 0
while vol != len(v):
    print(v[vol][0])
    vol +=1


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???

print((len(sentence)) / len(sentence.split()))