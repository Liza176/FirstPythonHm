d_age = int(input('Введите возраст собаки '))


if d_age<= 2 :
   h_age = d_age * 10.5
else:
    h_age = 21 + (d_age- 2) * 4


print('Человеческий возраст собаки' , h_age)
