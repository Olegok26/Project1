import re

string = input('Введите что нужно сделать и дату: ')
months = ['Января', 'января', 'Февраля', 'февраля', 'Марта', 'марта', 'Апреля', 'апреля', 'Мая', 'мая', 'Июня', 'июня',
          'Июля', 'июля', 'Августа', 'августа', 'Сентября', 'сентября', 'Октября', 'октября', 'Ноября', 'ноября',
          'Декабря', 'декабря']
year = 'года'
i = 0
k2 = len(months)

while i <= k2:
    if i != k2:
        if months[i] in string:
            mon = re.findall(r'(?<=\s)\d{1,2}\s' + months[i], string)
            mon1 = " ".join(mon)
            dat = re.findall(r'\d{1,2}', mon1)
            monp = months[i]
            string = string.replace('' + mon1 + ' ', '')
            print('Дата ', " ".join(dat))
            print('Месяц ', monp)
            break
        else:
            i = i + 1
    else:
        break

if year in string:
    y1 = re.findall(r'(?<=\s)\d{2,4}\s' + year, string)
    y2 = " ".join(y1)
    y3 = re.findall(r'\d{2,4}', y2)
    print('Год ', " ".join(y3))
    string = string.replace('' + " ".join(y1) + ' ', '')
if ':' in string:
    time = re.findall(r'\d{2}.\d{2}', string)
    tt = " ".join(time)
    print('Время', tt)
    hour = re.findall(r'\d{2}.', tt)
    hour1 = " ".join(hour)
    hourp = re.findall(r'\d{2}', hour1)
    print('Часы', " ".join(hourp))
    minute = re.findall(r'.\d{2}', tt)
    minute1 = " ".join(minute)
    minutep = re.findall(r'\d{2}', minute1)
    print('Минуты', " ".join(minutep))
    string = string.replace(tt, '')

print(string)
