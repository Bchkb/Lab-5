import re
import csv

PATH_1 = 'task1-ru.txt'
PATH_2 = 'task2.html'
PATH_3 = 'task3.txt'
PATH_OUT = 'table.csv'
MIDDLE_TEXT = 'middle.txt'


#Task 1
def word_point(text):
    res_w = re.findall(r'[а-яА-Я]{2,30}[.]', text)
    res_d = re.findall(r'[0-9][,]\d{1,}', text)
    return res_w, res_d


#Task 2
def pixel_values(text):
    res = re.findall(r'\d{0,}[p][x]', text)
    return res


#Task 3
def table_data(text):
    data_surname = re.findall(r'[A-Z][a-z]{0,}', text)
    data_email = re.findall(r'[-A-Za-z0-9]{1,}[@][-A-Za-z0-9]{1,}[.][a-z]{1,4}', text)
    data_date = re.findall(r'\d\d\d\d-\d\d-\d\d', text)
    data_site = re.findall(r'http[s]{0,1}://[www.]{0,4}[-A-Za-z0-9]{1,}[.][a-z]{,20}/', text)
    return data_surname, data_email, data_date, data_site


def table_data_id(text):
    data_id = re.findall(r'\d{1,4}', text)
    return data_id


def hide_date(text):
    data_date = re.sub(r'\d\d\d\d-\d\d-\d\d', '*', text)
    return data_date


def hide_email(text):
    data_email = re.sub(r'[A-Za-z]{1,}[-A-Za-z0-9]{0,}@[-A-Za-z0-9]{1,}[.][a-z]{1,4}', '*', text)
    return data_email


list_task1 = []
list_task2 = []


with open(PATH_1) as text:
    for line in text:
        res_w, res_d = word_point(line)
        if res_d != []: 
            list_task1.append(res_d)
        if res_w != []: 
            list_task1.append(res_w)

with open(PATH_2) as text:
    for line in text:
        res_p = pixel_values(line)
        if res_p != []:
            list_task2.append(res_p)



table = [['id', 'surname', 'email', 'date_reg', 'site']]
with open(PATH_3) as text, open(MIDDLE_TEXT, 'w') as mid:
    for line in text:
        data_surname, data_email, data_date, data_site = table_data(line)
        res = hide_email(line)
        res = hide_date(res)
        mid.write(res)


    
with open(MIDDLE_TEXT) as text, open(PATH_OUT, 'w') as out:
    for line in text:
        data_id = table_data_id(line)
    data_id.remove('0')
    data_id.remove('1000')
    data_id.append('10000')
    c = 0
    for i in range(len(data_id[0:100])):
        if c <= 6:
            if int(data_id[i]) > 1000:
                data_id.append(data_id[i][0:2])
                data_id.append(data_id[i][2:4])
                data_id.remove(data_id[i])
                c += 1
    
    writer = csv.writer(out)

    for i in range(len(data_id)):
        table.append([data_id[i], data_surname[i], data_email[i], data_date[i], data_site[i]])
    
    writer.writerows(table)