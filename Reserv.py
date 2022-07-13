variants = ['Приготовить покушать', 'Служебку подписать', 'Подписать служебку']
k1 = len(variants)
while i <= k1:
    if i != k1:
        if variants[i] in string:
            string = string.replace(variants[i] + ' ', '')
            a = variants[i]
            break
        else:
            i = i + 1
    else:
        print("Error")
        break

(?u)\w\sсред.{1,2}\s