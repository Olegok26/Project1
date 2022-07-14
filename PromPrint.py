import re
import datetime

string = input('Введите что нужно сделать и дату: ')
months = ['января', 'февраля',  'марта', 'апреля', 'мая', 'июня','июля', 'августа', 'сентября', 'октября', 'ноября',
        'декабря', 'Января', 'Февраля','Марта', 'Апреля', 'Мая', 'Июня','Июля', 'Августа', 'Сентября', 'Октября',
         'Ноября', 'Декабря']
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
nxt = ['завтра', 'послезавтра', 'на следующей неделе', 'в следующем месяце', 'в следующем году']

nxts = 0
i = 0
l = 0
povt = 0
sts = 0
delta = 0
dwo = 0
t = 0
nxtm = 0
rept = 0
errors = 0
x = 0
z = 0
ds = 0
ms = 0
time = datetime.datetime.now()
k1 = len(months)
k2 = len(days)
k3 = len(repeat)
k4 = len(repeat1)
k5 = len(step)
k6 = len(nxt)

mp = 0
hp = 0
dp = 0
mop = 0
yp = 0

while i <= k1:
    if i != k1:
        if months[i] in string:
            mon = re.findall(r'(?<=\s)\d{1,2}\s' + months[i], string)
            mon1 = " ".join(mon)
            d1 = re.findall(r'\d{1,2}', mon1)
            dp = " ".join(d1)
            mop = i
            string = string.replace('' + mon1 + ' ', '')
            print('Дата ', dp)
            print('Месяц ', mop)
            errors = errors + 1
            ms = ms + 1
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
                ds = ds + 1
                print('День недели ', days[i])
                break
            else:
                while l < k3:
                    if repeat[l] in string:
                        rep = re.findall(repeat[l] + '\s' + days[i], string)
                        rep1 = " ".join(rep)
                        if repeat[l] in rep1:
                            dwo = i
                            rept = l
                            string = string.replace(repeat[l] + ' ' + days[i], '')
                            ds = ds + 1
                            print('Повторение', rep1)
                            errors = errors + 1
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
                        rept = l
                        string = string.replace(repeat[l] + ' ' + days[i], '')
                        ds = ds + 1
                        print('Повторение', rep1)
                        errors = ds + 1
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
        z = z + 1
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
        else:
            i = i + 1

i = 0

while i < k6:
    if ' ' + nxt[i] in string:
        nxtm = i
        nxts = nxts + 1
        string = string.replace(nxt[i], '')
    else:
        i = i + 1

if year in string:
    y1 = re.findall(r'(?<=\s)\d{2,4}\s' + year, string)
    y2 = " ".join(y1)
    yx = re.findall(r'\d{2,4}', y2)
    yp = " ".join(yx)
    print('Год ', yp)
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
            hx = re.findall(r'\d{2}', hour1)
            hp = " ".join(hx)
            print('Часы', hp)
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mx = re.findall(r'\d{2}', minute1)
            mp = " ".join(mx)
            print('Минуты', mp)
            string = string.replace(W1 + tt, '')
            x = x + 1
        else:
            time = re.findall(r'\d{2}.\d{2}', string)
            tt = " ".join(time)
            print('Время', tt)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hx = re.findall(r'\d{2}', hour1)
            hp = " ".join(hx)
            print('Часы', hp)
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mx = re.findall(r'\d{2}', minute1)
            mp = " ".join(mx)
            print('Минуты', mp)
            string = string.replace(tt, '')
            x = x + 1
    else:
        time = re.findall(r'\d{2}.\d{2}', string)
        tt = " ".join(time)
        print('Время', tt)
        hour = re.findall(r'\d{2}.', tt)
        hour1 = " ".join(hour)
        hx = re.findall(r'\d{2}', hour1)
        hp = " ".join(hx)
        print('Часы', hp)
        minute = re.findall(r'.\d{2}', tt)
        minute1 = " ".join(minute)
        mx = re.findall(r'\d{2}', minute1)
        mp = " ".join(mx)
        print('Минуты', mp)
        string = string.replace(tt, '')
        x = x + 1
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
            hx = re.findall(r'\d{2}', hour1)
            hp = " ".join(hx)
            print('Часы', hp)
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mx = re.findall(r'\d{2}', minute1)
            mp = " ".join(mx)
            print('Минуты', mp)
            string = string.replace(W1 + tt, '')
            x = x + 1
        else:
            time = re.findall(r'\d{2}.\d{2}', string)
            tt = " ".join(time)
            print('Время', tt)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hx = re.findall(r'\d{2}', hour1)
            hp = " ".join(hx)
            print('Часы', hp)
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mx = re.findall(r'\d{2}', minute1)
            mp = " ".join(mx)
            print('Минуты', mp)
            string = string.replace(tt, '')
            x = x + 1
    else:
        time = re.findall(r'\d{2}.\d{2}', string)
        tt = " ".join(time)
        print('Время', tt)
        hour = re.findall(r'\d{2}.', tt)
        hour1 = " ".join(hour)
        hx = re.findall(r'\d{2}', hour1)
        hp = " ".join(hx)
        print('Часы', hp)
        minute = re.findall(r'.\d{2}', tt)
        minute1 = " ".join(minute)
        mx = re.findall(r'\d{2}', minute1)
        mp = " ".join(mx)
        print('Минуты', mp)
        string = string.replace(tt, '')
        x = x + 1

delta = int(delta)
dwo = (dwo + 1) % 7

if ms == 1:
    mop = (mop + 1) % 12

if sts > 0:
    if t == 0:
        if time.minute + delta > 60:
            mp = time.minute + delta % 60
            hp = time.hour + (time.minute + delta) // 60
            x = x + 6
        else:
            mp = time.minute + (delta % 60)
            x = x + 4
    elif t == 1:
        x = x + 5
        hp = (time.hour + delta) % 24
    elif t == 2:
        dp = time.day + delta
        wdp = time.weekday() + delta % 7
    elif t == 3:
        if time.month % 2 == 1:
            dp = (time.day + 7) % 31
        elif time.month == 12:
            dp = ((time.day + 7) % 31)
        elif time.month == 2:
            dp = (time.day + 7) % 28
    elif t == 4:
        mop = (time.month + delta) % 12
    elif t == 5:
        yp = time.year + delta
    elif t == 6:
        yp = time.year + delta

if nxts > 0:
    if nxtm == 0:
        dp = time.day + 1
        wdp = (time.weekday() + 1) % 7
    elif nxtm == 1:
        dp = time.day + 2
        wdp = (time.weekday() + 2) % 7
    elif nxtm == 3:
        mp = (time.month + 1) % 12
    elif nxtm == 4:
        yp = time.year + 1

povt = (povt * 2) - 1
print('Повторение массив', povt)
print(repeat1[povt])

if x == 0:
    hp = time.hour
    mp = time.minute
elif x == 4:
    hp = time.hour
elif x == 6:
    x = 0
elif x == 1:
    x = 0
else:
    mp = time.minute
if ds == 0 & z != 0:
    dwo = time.weekday()
if dp == 0:
    dp = time.day
if mop == 0:
    mop = time.month
if yp == 0:
    yp = time.year

if sts != 0:
    print(f'Статус:Успешно, Текст: {string}, Параметры: День недели: {days[dwo]}, Время: часы: {hp}, минуты: {mp}, '
          f'Дата: число: {dp}, месяц: {mop}, год:{yp} ')
elif z != 0:
    if povt == 1:
        print(f'Статус:Успешно, Текст: {string}, Параметры: Повторение: {repeat1[povt]}, Время: часы: {hp}, минуты: {mp}')
    elif povt == 3:
        print(f'Статус:Успешно, Текст: {string}, Параметры: Повторение: {repeat1[povt]}, День недели: {days[dwo]}, Время: '
          f'часы: {hp}, минуты: {mp}')
    elif povt  == 5:
        print(
            f'Статус:Успешно, Текст: {string}, Параметры: Повторение: {repeat1[povt]}, День недели: {days[dwo]}, Время: '
            f'часы: {hp}, минуты: {mp}, Дата: число: {dp}')
    elif povt == 7:
        print(
            f'Статус:Успешно, Текст: {string}, Параметры: Повторение: {repeat1[povt]}, День недели: {days[dwo]}, Время: '
            f'часы: {hp}, минуты: {mp}, Дата: число: {dp}, месяц: {mop}')
elif nxts != 0:
    print(f'Статус:Успешно, Текст: {string}, Параметры: День недели: {days[wdp]}, Даты: часы: {hp}, минуты: {mp}')
elif errors >= 1 and ds == 1:
    print(f'Статус:Успешно, Текст: {string}, Параметры: День недели: {days[dwo]}, Время: часы: {hp}, минуты: {mp}')
elif errors >= 1:
    print(f'Статус:Успешно, Текст: {string}, Время: часы: {hp}, минуты: {mp}, '
          f'Дата: число: {dp}, месяц: {mop}, год: {yp}')
else:
    print('Статус:ОШИБКА')
