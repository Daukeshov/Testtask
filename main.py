import os
import pandas as pd
import re


#Вывод директории в список
def directory():
    path = []
    for top, dirs, files in os.walk('C:/Users/madi.daukeshov/PycharmProjects/testtask/'):
        for nm in files:
            directory = os.path.join(top, nm)
            path.append(directory)

    #убираем ненужные файлы которые получили ранее
    global route
    route = []
    skip = 'testtask/.idea'
    for i in path:
        put = i.partition('PycharmProjects/')[2]
        if skip not in put:
            route.append(put)


def create_df(route):
    #Нормализация данных для обработки
    global test
    test = []
    for i in route:
        pat = i.replace('testtask/test5\\test7\\test10\\', '')
        rat = pat.replace('testtask/test5\\test7\\', '')
        cat = rat.replace('testtask/test5\\', '')
        bat = cat.replace('testtask/', '')
        test.append(bat)


    #Создаем DataFrame и добавляем путь по каждому файлу
    global df
    df = pd.DataFrame(route, columns = ['Папка в которой лежит файл'])
    for i in test:
        df.replace(regex=[i], value="", inplace=True)
    return route, test


def add_name_type(test):
    #Вытаскиваем название файла и добавляем в DataFrame
    name = []
    for i in test:
        nam = i.partition('.')[0]
        name.append(nam)
    df['название файла'] = name


    #Вытаскиваем расширение файла и добавляем в DataFrame
    type_file = []
    for i in test:
        mat = i.partition('.')[2]
        type_file.append(mat)
    df['расширение файла'] = type_file


#Импорт данных с DataFrame в Excel
def create_doc():
    writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
    df.to_excel(writer, 'результат')
    writer.close()


if __name__ == '__main__':
    directory()
    create_df(route)
    add_name_type(test)
    create_doc()