import re
import datetime

string = input('Введите что нужно сделать и дату: ')
months = ['Января', 'января', 'Февраля', 'февраля', 'Марта', 'марта', 'Апреля', 'апреля', 'Мая', 'мая', 'Июня', 'июня',
          'Июля', 'июля', 'Августа', 'августа', 'Сентября', 'сентября', 'Октября', 'октября', 'Ноября', 'ноября',
          'Декабря', 'декабря']
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье', 'будни', 'выходные',
        'понедельник', 'вторник', 'среду', 'пятницу', 'субботу', 'воскресенье', 'понедельникам', 'вторникам', 'средам',
        'четвергам', 'пятницам', 'субботам', 'воскресеньям', 'будням', 'выходным']
dayp = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье', 'будни', 'выходные']
year = 'года'
W1 = 'в '
repeat = ['каждый', 'каждую', 'по', 'Каждый', 'Каждую', 'По']
repeat1 = ['ежедневно', 'Ежедневно', 'Еженедельно', 'еженедельно', 'Ежемесячно',
           'ежемесячно', 'Ежегодно', 'ежегодно']
stepm = 'через'
step = ['минут', 'часов', 'дней', 'недель', 'месяцев', 'год', 'лет']
nxtm = ['на следующей неделе', 'в следующем месяце', 'в следующем году']
nxt = ['завтра', 'послезавтра', 'на следующей']

i = 0
l = 0
povt = 0
sts = 0
time = datetime.datetime.now()
k1 = len(months)
k2 = len(days)
k3 = len(repeat)
k4 = len(repeat1)
k5 = len(step)

while i <= k1:
    if i != k1:
        if months[i] in string:
            mon = re.findall(r'(?<=\s)\d{1,2}\s' + months[i], string)
            mon1 = " ".join(mon)
            d1 = re.findall(r'\d{1,2}', mon1)
            dp = " ".join(d1)
            mp = months[i]
            string = string.replace('' + mon1 + ' ', '')
            print('Дата ', dp)
            print('Месяц ', mp)
            break
        else:
            i = i + 1
    else:
        break

i = 0

while i < k2:
    if days[i] in string:
        if W1 in string:
            dw = re.findall(r'.\s' + days[i], string)
            dw1 = " ".join(dw)
            if W1 in dw1:
                dwo = i
                dw2 = re.findall(days[i], dw1)
                dwp = " ".join(dw2)
                string = string.replace(W1 + days[i], '')
                print('День недели ', days[i])
                break
            else:
                while l < k3:
                    if repeat[l] in string:
                        rep = re.findall(repeat[l] + '\s' + days[i], string)
                        rep1 = " ".join(rep)
                        if repeat[l] in rep1:
                            dwo = i
                            povt = povt + 1
                            string = string.replace(repeat[l] + ' ' + days[i], '')
                            print('Повторение', rep1)
                            break
                    else:
                        l = l + 1
                break
        else:
            while l < k3:
                if repeat[l] in string:
                    rep = re.findall(repeat[l] + ' ' + days[i], string)
                    rep1 = " ".join(rep)
                    if repeat[l] in rep1:
                        dwo = i
                        povt = povt + 2
                        string = string.replace(repeat[l] + ' ' + days[i], '')
                        print('Повторение', rep1)
                        break
                    break
                else:
                    l = l + 1
            break
    else:
        i = i + 1

i = 0

while i < k4:
    if repeat1[i] in string:
        if i <= 1:
            povt = 1
        elif i <= 3:
            povt = 2
        elif i <= 5:
            povt = 3
        else:
            povt = 4
        string = string.replace(repeat1[i], '')
        print('Повторение ', povt)
        break
    else:
        i = i + 1

i = 0

if stepm in string:
    while i < k5:
        st = re.findall(stepm + r'\s\d{1,2}\s' + step[i], string)
        st1 = " ".join(st)
        if step[i] in st1:
            st2 = re.findall(r'\s\d{1,2}\s', st1)
            delta = " ".join(st2)
            sts = sts + 1
            t = i
            string = string.replace(st1, '')
            print('СТС ', sts)
            print('На сколько увеличить ', delta)
            break

if year in string:
    y1 = re.findall(r'(?<=\s)\d{2,4}\s' + year, string)
    y2 = " ".join(y1)
    yp = re.findall(r'\d{2,4}', y2)
    print('Год ', " ".join(yp))
    string = string.replace('' + " ".join(y1) + ' ', '')

if ':' in string:
    if W1 in string:
        tw = re.findall(r'.\s' + '\d{2}.\d{2}', string)
        tw1 = " ".join(tw)
        if W1 in tw1:
            time = re.findall(r'\d{2}.\d{2}', string)
            tt = " ".join(time)
            print('Время', tt)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hp = re.findall(r'\d{2}', hour1)
            print('Часы', " ".join(hp))
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mp = re.findall(r'\d{2}', minute1)
            print('Минуты', " ".join(mp))
            string = string.replace(W1 + tt, '')
        else:
            time = re.findall(r'\d{2}.\d{2}', string)
            tt = " ".join(time)
            print('Время', tt)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hp = re.findall(r'\d{2}', hour1)
            print('Часы', " ".join(hp))
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mp = re.findall(r'\d{2}', minute1)
            print('Минуты', " ".join(mp))
            string = string.replace(tt, '')
    else:
        time = re.findall(r'\d{2}.\d{2}', string)
        tt = " ".join(time)
        print('Время', tt)
        hour = re.findall(r'\d{2}.', tt)
        hour1 = " ".join(hour)
        hp = re.findall(r'\d{2}', hour1)
        print('Часы', " ".join(hp))
        minute = re.findall(r'.\d{2}', tt)
        minute1 = " ".join(minute)
        mp = re.findall(r'\d{2}', minute1)
        print('Минуты', " ".join(mp))
        string = string.replace(tt, '')
elif '.' in string:
    if W1 in string:
        tw = re.findall(r'.\s\d{2}.\d{2}\b', string)
        tw1 = " ".join(tw)
        if W1 in tw1:
            time = re.findall(r'\d{2}.\d{2}', string)
            tt = " ".join(time)
            print('Время', tt)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hp = re.findall(r'\d{2}', hour1)
            print('Часы', " ".join(hp))
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mp = re.findall(r'\d{2}', minute1)
            print('Минуты', " ".join(mp))
            string = string.replace(W1 + tt, '')
        else:
            time = re.findall(r'\d{2}.\d{2}', string)
            tt = " ".join(time)
            print('Время', tt)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hp = re.findall(r'\d{2}', hour1)
            print('Часы', " ".join(hp))
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mp = re.findall(r'\d{2}', minute1)
            print('Минуты', " ".join(mp))
            string = string.replace(tt, '')
    else:
        time = re.findall(r'\d{2}.\d{2}', string)
        tt = " ".join(time)
        print('Время', tt)
        hour = re.findall(r'\d{2}.', tt)
        hour1 = " ".join(hour)
        hp = re.findall(r'\d{2}', hour1)
        print('Часы', " ".join(hp))
        minute = re.findall(r'.\d{2}', tt)
        minute1 = " ".join(minute)
        mp = re.findall(r'\d{2}', minute1)
        print('Минуты', " ".join(mp))
        string = string.replace(tt, '')

delta = int(delta)
dwo = (i + 1) % 7

if sts > 0:
    if t == 0:
        mp = time.minute + delta
    elif t == 1:
        hp = time.hour + delta
    elif t == 2:
        dp = time.day + delta
        wdp = time.weekday() + delta % 7
    elif t == 3:
        wp = time.week + delta
    elif t == 4:
        mp = time.month + delta
    elif t == 5:
        yp = time.year + delta
    elif t == 6:
        yp = time.year + delta

print(string)
