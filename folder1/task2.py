# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите число: '))
summa = 0
while number>10:
    summa +=number%10
    number//10
summa +=number
print(summa)
