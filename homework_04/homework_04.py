import string

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#task 1 - прибрати переноси
print_adventures = adwentures_of_tom_sawer.replace('\n', ' ')
print(print_adventures)
print('.'*100)

#task 2 - заміна на пробіл
replace_dots = print_adventures.replace('....', '')
print(replace_dots)
print('.'*100)

#task 3 - прибрати зайві пробіли

without_spaces = ' '.join(replace_dots.split())
print(without_spaces)
print('-'*100)

#task4 - знайти букву h

find_letter = without_spaces.find('h')
print(find_letter)
print('-'*100)

#task 5 - кількість слів з великої літери

split_without_spaces = without_spaces.split(' ')
print(split_without_spaces)

titled_words = []

for text in split_without_spaces:
    if text.istitle():
        print(text)
        titled_words.append(text)

print('\n')

count = sum(text.istitle() for text in split_without_spaces)
print(f'Amount of words starts with upper letter = {count}')
print('-'*100)

#task 6 - знайти позицію на якій Том зустрічается вдруге
print(titled_words)

first_index = titled_words.index('Tom')
second_index = titled_words.index('Tom', first_index + 1)

print(f'Tom знаходится на позиції - {second_index}')
print('-'*100)

#task 7 - розділити по закінченню речння

adwenture_sentence = without_spaces.split('. ')

adwentures_of_tom_sawer_sentences = '.\n'.join(adwenture_sentence)
print(adwentures_of_tom_sawer_sentences)
print('-'*100)

#task8 - вивести четверте речення і перенести у ніжній регістр

adwenture_devide = without_spaces.split('. ')
print(f'Кількість речень - {len(adwenture_devide)}')
print(adwenture_devide[3].lower())
print('-'*100)

#task9 - почато реченя на 'By the time'

for find_sentence in adwenture_devide:
    if find_sentence.startswith('By the time'):
        print(f'Я знайшов, і це речення - {find_sentence}')
print('-'*100)

#task10 - Виведіть кількість слів останнього речення

print(f'Кількість символів в останньому речені - {len(adwenture_devide[-1])}')
print('-'*100)
