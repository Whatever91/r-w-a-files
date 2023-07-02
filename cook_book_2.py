cook_book_dict={
'Омлет': [
   {'ingradient_name': 'Яйцо ', 'quantity': ' 2 ', 'measure': ' шт'},
   {'ingradient_name': 'Молоко ','quantity': ' 100 ','measure': ' мл'},
   {'ingradient_name': 'Помидор ','quantity': ' 2 ','measure': ' шт'}
    ],
 'Утка по-пекински': [
    {'ingradient_name': 'Утка ','quantity': ' 1 ','measure': ' шт'},
    {'ingradient_name': 'Вода ','quantity': ' 2 ','measure': ' л'},
    {'ingradient_name': 'Мед ','quantity': ' 3 ','measure': ' ст.л'},
    {'ingradient_name': 'Соевый соус ','quantity': ' 60 ','measure': ' мл'}
    ],
 'Запеченный картофель': [
     {'ingradient_name': 'Картофель ','quantity': ' 1 ','measure': ' кг'},
     {'ingradient_name': 'Яйцо ', 'quantity': ' 5 ', 'measure': ' шт'}, 
     {'ingradient_name': 'Чеснок ','quantity': ' 3 ','measure': ' зубч'},
     {'ingradient_name': 'Сыр гауда ','quantity': ' 100 ','measure': ' г'}
     ],
 'Фахитос': [
     {'ingradient_name': 'Говядина ','quantity': ' 500 ','measure': ' г'},
     {'ingradient_name': 'Перец сладкий ','quantity': ' 1 ','measure': ' шт'},
     {'ingradient_name': 'Лаваш ', 'quantity': ' 2 ', 'measure': ' шт'},
     {'ingradient_name': 'Винный уксус ','quantity': ' 1 ','measure': ' ст.л'},
     {'ingradient_name': 'Помидор ','quantity': ' 2 ','measure': ' шт'}
     ]
   }

from pprint import pprint

def get_shop_list_by_dishes(dishes_list, person_count=1):
    ingradient_dict_all = {}
    for dish in dishes_list:

        for el in cook_book_dict[dish]:
            #print(el) # {'ingradient_name': 'Картофель ', 'quantity': ' 1 ', 'measure': ' кг'}
                     # {'ingradient_name': 'Чеснок ', 'quantity': ' 3 ', 'measure': ' зубч'}
                     # {'ingradient_name': 'Сыр гауда ', 'quantity': ' 100 ', 'measure': ' г'}

            ingradient_dict = {} 
            ingradient_name=el['ingradient_name'] 
            working_dict={} 
            working_dict['measure']=el['measure'] 
            quantity= int(el['quantity'])*person_count 
            working_dict['quantity'] = quantity
            ingradient_dict[ingradient_name]= working_dict
            #print(ingradient_dict) # Для 'Запеченный картофель'на 1 персону:
                                   # {'Картофель ': {'measure': ' кг', 'quantity': 1}}
                                   # {'Чеснок ': {'measure': ' зубч', 'quantity': 3}}
                                   # {'Сыр гауда ': {'measure': ' г', 'quantity': 100}}
            for key in ingradient_dict:
                if key in ingradient_dict_all:
                    ingradient_dict[key]['quantity'] += ingradient_dict_all[key]['quantity']
            ingradient_dict_all.update(ingradient_dict)
    pprint(ingradient_dict_all) 

get_shop_list_by_dishes(['Омлет','Запеченный картофель'],2)

