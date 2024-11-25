#pets=dict()
#n=int(input())

#for i in range(n):
   # req=input()
    #if req=="create":
       # p1={"введите вид питомца":a=input()}
#print("введите вид питомца")
#a=input()
#print("введите кличку питомца")
#b=input()
#print("введите возраст вашего питомца")
#c=input()
#print(a, b, c)

s_kl = 'Кличка: '
s_vid = 'Вид питомца: '
s_age = 'Возраст питомца: '
s_im_vl = 'Имя владельца: '
 
def years_word(n):
    return str(n) + ' ' + ('год' if n==1 else 'года' if n in (2,3,4) else 'лет')
 
def d_to_str(data, pet_name):
    d = data[pet_name]
    return f'Это {d[s_vid]}. {s_kl}{pet_name}. {s_age}{years_word(d[s_age])}. {s_im_vl}{d[s_im_vl]}'
 
pets = {}
print('Введите данные о питомце:')
pet_name = input(s_kl)
d = pets[pet_name] = {}
 
d[s_vid] = input(s_vid)
d[s_age] = int(input(s_age))
d[s_im_vl] = input(s_im_vl)
print()
print('Данные внесены в словарь.')
print(d_to_str(pets, pet_name))