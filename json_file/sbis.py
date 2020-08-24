# -*- coding: utf-8 -*-
import os 
import sys
import json
#import errors

#статические переменные
errors = list()
user_input = input('Введите имя файла: ')

#счетчик ошибок
def ercount():
    errors.append() 

# основная функция, потом в класс
def open_json():
    
    try:
        with open(user_input, "r", encoding='utf-8') as jfile:
            json1 = json.load(jfile)
            #print(json1)
        
        for key, value in json1.items():
            print(key, value)
            types = value['Типы']
            data = value['Данные']
            def valid():
                yy = []
                ii = []
                for y in types.values():
                    yy.append(y)
                for i in data.values():
                    ii.append(i)
                print(yy,ii)
                #if 
                return yy,ii

            valid()
                
    except:
        print('Данного файла нет')
        pass
    

    

#unit tests
def utest():
    pass

open_json()



