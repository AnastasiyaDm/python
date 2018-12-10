#1)Дан массив из словарей 
#1.1) отсортировать массив из словарей по значению ключа ‘age' 

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


def sort_age(age_sort):
    return age_sort.get('age')


print(sorted(data,key=sort_age))

#1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :
