'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''



a = input('введите цифры')
num = [int(a)for a in a.split()]
print(num)
sum = sum(num)
print(sum)
max = max(num)
print(max)
average = sum / len(num)
print(average)










