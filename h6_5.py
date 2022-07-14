

my_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        my_dict[subject] = int(lecture) + int(practice) + int(lab)

    print(f'{my_dict}')

