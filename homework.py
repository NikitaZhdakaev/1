# Задача 1
# def request_user(f):
#     user = False
#     count = 1
#     while f > 0:
        
#         user_request = int(
#             input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
#         while user_request > 28:
#             print(f'Игрок {int(user)+1} повторите ввод!')
#             user_request = int(
#                 input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
#         f -= user_request
#         print(f)
#         count += 1
#         user = not(user)
#         if f == 0:
#             print(f'Игрок {int(user)+1} победил!')

# def bot(f):
#     return (f % 29) - 1

# full = 100
# request_user(full)

задача 2
with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('text_words.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond

txt_compr = file_encod(my_txt)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)