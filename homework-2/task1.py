#1)Дан массив из словарей 
#1.1) отсортировать массив из словарей по значению ключа ‘age' 

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]



print(sorted(data,key=lambda k: k["age"]))


#1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :


def sort_city(dat):
    result = {}
    for i in dat:
        a = i.get('city')
        if a in result:
            result[a].append({'name': i.get('name'), 'age': i.get('age')})
        else:
            result[a] = [{'name': i.get('name'), 'age': i.get('age')}]

    return result

print(sort_city(data))
