def request_user(f):
    user = False
    count = 1
    while f > 0:
        
        user_request = int(
            input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        f -= user_request
        print(f)
        count += 1
        user = not(user)
        if f == 0:
            print(f'Игрок {int(user)+1} победил!')

def bot(f):
    return (f % 29) - 1

full = 100
request_user(full)