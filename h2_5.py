#  2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
#     выполнить подсчёт строк и слов в каждой строке.


with open('text_2.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f'Содеожимое файла: \n{content}')

with open('text_2.txt', 'r') as f:
    len_content = f.readlines()
    print(f'Колличество строк в файле: \n{len(len_content)}')

numb_words = 0
numb_lines = 0
with open('text_2.txt', 'r') as f:

    for line in f:
        numb_lines += 1
        words_in_line = line.split()
        numb_words += len(words_in_line)
        print(f'Колличество слов в {numb_lines}-й строке - {len(words_in_line)}')





