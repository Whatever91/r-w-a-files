from pprint import pprint

with open('recipes.txt', 'rt',encoding='utf-8') as file:
    cook_book= {} 
    for line in file:
        dish=line.strip() 
        number_ingradients = int(file.readline().strip()) 
        ingradients_list=[] 
        for _ in range(number_ingradients) :
            ingredient_name,quantity,measure= file.readline().strip().split('|')
            ingradients_list.append({
             'ingradient_name': ingredient_name,
             'quantity':quantity ,
             'measure': measure })
        file.readline() 
        cook_book[dish]=ingradients_list 
    pprint(cook_book , sort_dicts=False)

