import re
re.compile('[А-Яа-яЁё]+', )

string = input('Введите что нужно сделать и дату: ')
months = ['Января', 'января', 'Февраля', 'февраля', 'Марта', 'марта', 'Апреля', 'апреля', 'Мая', 'мая', 'Июня', 'июня',
          'Июля', 'июля', 'Августа', 'августа', 'Сентября', 'сентября', 'Октября', 'октября', 'Ноября', 'ноября',
          'Декабря', 'декабря']
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье', 'будни', 'выходные',
        'среду', 'пятницу', 'субботу', 'понедельникам', 'вторникам', 'средам', 'четвергам', 'пятницам', 'субботам',
        'воскресеньям', 'будням', 'выходным']
year = 'года'
W1 = 'в '
repeat = ['каждый', 'каждую', 'по', 'Каждый', 'Каждую', 'По']
repeat1 = ['ежедневно', 'Ежедневно']
i = 0
k1 = len(months)
k2 = len(days)
k3 = len(repeat)
k4 = len(repeat1)
l = 0
povt = 0
while i <= k1:
    if i != k1:
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

i = 0
s = 0
while i <= k2:
    if i != k2:
        if days[i] in string:
            if W1 in string:
                dw = re.findall(r'.\s' + days[i], string)
                dw1 = " ".join(dw)
                if W1 in dw1:
                    dwo = i
                    dw2 = re.findall(days[i], dw1)
                    dwp = " ".join(dw2)
                    string = string.replace(W1 + days[i], '')
                    print('День недели ', " ".join(dwp))
                    break
                else:
                    while l <= k3:
                        if l != k3:
                            if repeat[l] in string:
                                rep = re.findall(repeat[l] +'\s'+ days[i], string)
                                rep1 = " ".join(rep)
                                if repeat[l] in rep1:
                                    povt = povt + 1
                                    string = string.replace(repeat[l]+ ' ' + days[i], '')
                                    print('Повторение', rep1)
                                    break
                            else:
                                l = l + 1
                    break
            else:
                print('Нет W1')
                while l <= k3:
                    if l != k3:
                        if repeat[l] in string:
                            rep = re.findall(repeat[l]+days[i], string)
                            rep1 = " ".join(rep)
                            if repeat[l] in rep1:
                                povt = povt + 1
                                string = string.replace(repeat[l] + days[i], '')
                                print('Повторение', rep1)
                                break
                            break
                        else:
                            l = l + 1
                    break
                break
        else:
            i = i + 1

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
