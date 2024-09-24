# task number 1 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")
print('----------')

#task number 2 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")
    print(f"----------")

#task number 3 == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)
print('----------')

#task number 4 == Зробіть так, щоб кількість бананів була
apples = 2
banana = apples * 4
#можна написати невеличку программу з інпутом
apples_ = int(input("How many apples would you like to ->>>")) #press [Enter] once u finished typing numbers

bananas_ = apples_ * 4
print(f"In this case if you choose {apples_} apples, bananas will be 4 times more which is = {bananas_}")
print('----------')

# task 05 == виправте назви змінних
first_side = 1
second_side = 2
third_side = 3
fourth_side = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = first_side + second_side + third_side + fourth_side
print(f"Perimetery is equal to {perimetery}")
print('----------')

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apple_trees = 4
pears_trees = apple_trees + 5
plums_trees = apple_trees - 2

amount_of_trees = apple_trees + pears_trees + plums_trees
print(f"Amount of trees is {amount_of_trees}")
print('----------')

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

starting_point = 0
before_lunch = starting_point + 5
after_lunch = before_lunch - 10
evening_time = after_lunch + 4

print(f"Temperature in the evening time is equal to {evening_time}")
print('----------')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
amount_of_mens = 24
amount_of_girls = amount_of_mens / 2

sick_mens = amount_of_mens - 1
sick_girls = amount_of_girls - 2
print(f"Amount of kids for today is {sick_mens + sick_girls}")
print('----------')

#напишу простий код для калькуляції кількості дітей у саду (написано без виключень, тому краще закоментую)
"""amount_of_mens_ = int(input("How many mens are there ->>>>>"))
amount_of_girls_ = int(input("How many girsl are there ->>>>>"))
sick_mens_ = int(input("How many mens are sick today->>>"))
sick_girls_ = int(input("How many girls are sick today->>>"))

amount_of_kids_ = (amount_of_mens_ - sick_mens_) + (amount_of_girls_ - sick_girls_)
print(f"Amount of childrens today is {amount_of_kids_}")
print('----------')
"""


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2

final_price = first_book + second_book + third_book
print(f"Final price for all book is {final_price}")