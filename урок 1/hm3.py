time_in_second = int(input('Введите время в секундах'))

seconds = time_in_second % 60     # значение секунд
minutes_for_hours = time_in_second // 60     # минуты для дальнейшего преобразования
minutes = minutes_for_hours % 60     # значение минут
hours = minutes_for_hours // 60      # значение часов


print('%02d:%02d:%02d' % (hours, minutes, seconds))

