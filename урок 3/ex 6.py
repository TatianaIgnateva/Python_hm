def int_func(right_words):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return right_words.title() if not set(right_words).difference(latin_char) else False
                               # если в отсортированном(right_words) нет символов
                                           # difference-отличающихся от (latin_char)  / заметка для меня

words = input('Введите слова через пробел').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ';')


