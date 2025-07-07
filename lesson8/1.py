"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""
surname, name, patronymic = input('фамилия имя отчество').split()
def format_fio(full_name, short_name=True):
  
    if short_name:
        return f"- {surname} {name[0]}.{patronymic[0]}."
    if full_name:
        return f"- {name[0]}.{patronymic[0]}.{surname}"
print(format_fio("фамилия и.о.")) 
print(format_fio("и.о.фамилия", short_name = False))




