def turnNumberIntoPercent(number):
    num = str(number)
    num = num.replace('.','')
    if number >= 100:
        num = num[:1] + '.' + num[1:]
    else:
        num = '.' + num
    return float(num)