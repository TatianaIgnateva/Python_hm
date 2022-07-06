def personal_inform():
    name = input('Введите имя ')
    surname = input('Введите фамилию ')
    year_bthd = input('Введите год рождения ')
    city = input('Введите город проживания ')
    telephone = input('Введите номер телефона ')
    return name, surname, year_bthd, city, telephone


name, surname, year_bthd, city, telephone = personal_inform()
print(f'Имя: {name}; Фамилия: {surname}; год рождения: {year_bthd}; город проживания: {city}; телефон: {telephone}.')
