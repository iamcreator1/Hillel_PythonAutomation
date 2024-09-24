import math

print('task01 - 03')
#task01 - Розділити змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
#task02 - Знайти та відобразити всі символи одинарної лапки (') у тексті
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n"'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n')

#task03 - вивести змінну alice_in_wonderland на друк
print(alice_in_wonderland)
print('----------')
#task04:
#Площа Чорного моря становить 436 402 км2, а площа Азовського
#моря становить 37 800 км2. Яку площу займають Чорне та Азов-
#ське моря разом?
print('task04')
black_sea_square = 436_402 #площа чорного моря
azov_sea_square = 37_800 #площа азовського моря
general_square = black_sea_square + azov_sea_square
print(f'Загальна площа Чорного та Азовського моря становить: {general_square} км2')

print('----------')
print('task05')

total_amount_of_products = 375291
first_second_sum = 250449
second_third_sum = 222950

var_c = total_amount_of_products - first_second_sum
var_b = second_third_sum - var_c
var_a = first_second_sum - var_b

print(f"Кількість товарів на першому складі: {var_a}")
print(f"Кількість товарів на другому складі: {var_b}")
print(f"Кількість товарів на третьому складі: {var_c}")


print('----------')
print('task06')
#task06
#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
#вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.
has_to_pay = 18 #кількість місяців які потрібно олпачувати
monthly_payment = 1179

price_for_computer = has_to_pay * monthly_payment
print(f'Фінальна ціна, яку потрібно заплатити за компьютер виплачуючи півтори року складає ---> {price_for_computer} грн')
print('----------')

print('task07')
first_par_a = 8019
second_par_a = 8
a_example = first_par_a % second_par_a
print(f'залишок від ділення в задачі а: {a_example}')

first_par_b = 9907
second_par_b = 9
b_example = first_par_b % second_par_b
print(f'залишок від ділення в задачі b: {b_example}')

first_par_c = 2789
second_par_c = 5
c_example = first_par_c % second_par_c
print(f'залишок від ділення в задачі с: {c_example}')

first_par_d = 7248
second_par_d = 6
d_example = first_par_d % second_par_d
print(f'залишок від ділення в задачі d: {d_example}')

first_par_e = 7128
second_par_e = 5
e_example = first_par_e % second_par_e
print(f'залишок від ділення в задачі е: {e_example}')

first_par_f = 19224
second_par_f = 9
f_example = first_par_f % second_par_f
print(f'залишок від ділення в задачі f: {f_example}')
print('----------')

print('task08')
#Іринка, готуючись до свого дня народження, склала список того,
#що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
#для даного її замовлення.
#Назва товару    Кількість   Ціна
#Піца велика     4           274 грн
#Піца середня    2           218 грн
#Сік             4           35 грн
#Торт            1           350 грн
#Вода            3           21 грн

large_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

amount_for_celebrating = (large_pizza_price * 4) + (medium_pizza_price * 2) + (juice_price * 4) + cake_price + (water_price * 3)
print(f'Кількість грошей, яка необхідна для замовлення товарів для святкування складає: {amount_for_celebrating} грн')
print('----------')

print('task09')
#task09
#Ігор займається фотографією. Він вирішив зібрати всі свої 232
#фотографії та вклеїти в альбом. На одній сторінці може бути
#розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
#Ігорю, щоб вклеїти всі фото?

amount_of_photos = 232
page_can_contain = 8
necessary_amount_of_page = math.ceil(amount_of_photos / page_can_contain)
print(f'{necessary_amount_of_page} - стільки сторінок потрібно буде Ігорю, щоб вклеіти усі свої фото')
print('----------')


print('task10')
#Родина зібралася в автомобільну подорож із Харкова в Буда-
#пешт. Відстань між цими містами становить 1600 км. Відомо,
#що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
#становить 48 літрів.
#1) Скільки літрів бензину знадобиться для такої подорожі?
#2) Скільки щонайменше разів родині необхідно заїхати на зап-
#равку під час цієї подорожі, кожного разу заправляючи пов-
#ний бак?

consumption_hundred = 9 #витрати літрів на 100 км
capacity_of_tank = 48 #обʼєм баку
trip_distance = 1600 #дистанція подорожі у км


necessary_amount_of_fuel = (trip_distance / 100) * consumption_hundred # 144 л палива необхідно на подорож
amount_of_stops = necessary_amount_of_fuel / capacity_of_tank #що найменше 3 рази треба ббуде заїхати на заправку

print(f'Кількість літрів бензину необхідно для подорожі - {math.ceil(necessary_amount_of_fuel)} л')
print(f'{math.ceil(amount_of_stops)} - мінімальная кільсть зупинок для заповнення баку паливом')

print('----------')