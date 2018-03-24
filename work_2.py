##############################
# 1	    I	лат. unus, unum
# 5	    V	лат. quinque
# 10	X	лат. decem
# 50	L	лат. quinquaginta
# 100	C	лат. centum
# 500	D	лат. quingenti
# 1000	M	лат. mille
##############################

Roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1} #словарь с римскими обозначениями и их численным выражением
Subtraction_Rule = {"CM": 100, "CD": 100, "XC": 10, "XL": 10, "IX": 1, "IV": 1} #словарь с парой «обозначение разницы — вычитаемое значение»
Connection_Rule = {"M": "CM", "D": "CD", "C": "XC", "L": "XL", "X": "IX", "V": "IV"} #словарь с парой «полное число (1000, например) — ближайшее к нему по правилу вычитания (900)

def to_roman(Arabic_Number): #функция для перевода с арабской системы в римскую
    Arabic_Number = int(Arabic_Number)
    Roman_Number = ""
    for keys in Roman:
        Temp_Number = Arabic_Number // Roman[keys] #получаем целое значение от текущего в порядке словаря Roman
        Arabic_Number = Arabic_Number % Roman[keys] #получаем остаток для расчётов по правилу вычитания, если повезёт
        if (Temp_Number > 0 and Temp_Number < 4): #превращение целой части в римскую цифру
            Roman_Number = Roman_Number + keys * Temp_Number
        if (Arabic_Number % 9 == 0 and Arabic_Number > 0): #в данном ифе и елифе рассматриваются ситуации, когда мы попадаем на кратность 9 (900, 90, 9) и 4 (400, 40, 4) — тут применяется правило вычитания
            if (Arabic_Number < (Roman[keys] - Subtraction_Rule[Connection_Rule[keys]])): #экспериментально получено и жизненно необходимо, и нет, это не костыль
                continue
            Roman_Number = Roman_Number + Connection_Rule[keys] #добавляем комбинацию символов из правила вычитания (вроде IX)
            Arabic_Number = Arabic_Number - (Roman[keys] - Subtraction_Rule[Connection_Rule[keys]]) #и отнимаем от арабского числа ту часть, которая была внесена в римское
        elif (Arabic_Number % 4 == 0 and Arabic_Number > 0):
            if (Arabic_Number < (Roman[keys] - Subtraction_Rule[Connection_Rule[keys]])):
                continue
            Roman_Number = Roman_Number + Connection_Rule[keys]
            Arabic_Number = Arabic_Number - (Roman[keys] - Subtraction_Rule[Connection_Rule[keys]])
    return(Roman_Number)

def to_arabic(Roman_Number): #функция для перевода с римской системы в арабскую
    Roman_Number = Roman_Number.upper() #переводим в верхний регистр на случай, если пользователь ввёл что-то вроде lxix
    Arabic_Number = 0
    for i in Roman_Number: #в данном цикле просто суммируем все символы в соответствии с данными из словаря Roman и игнорируя правило вычитания
        Arabic_Number += Roman[i]
    for i in Subtraction_Rule: #в данном цикле восстанавливаем справедливость и вычитаем двойное вычитаемое значение (1 за то, что поленились это сделать раньше; 2 в соответствии с правилом вычитания)
        if (Roman_Number.find(i) != -1):
            Arabic_Number -= (Subtraction_Rule[i] * 2)
    return(Arabic_Number)

Number = input("Enter number (roman or arabic): ")
Variant = int(input("1. To roman numerals.\n2. To arabic numerals.\nVariant: "))

if (Variant == 1): print(to_roman(Number))
else: print(to_arabic(Number))


