def check_password(username, password, password_length=8,
                   check_username=True, spec_sym=True):
    if len(password) < password_length:
        print("Пароль слишком короткий")
        return False
    elif check_username and username in password:
        print("Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} установлен")
        return True


def create_user(db):
    username = input("Введите имя пользователя: ")
    while True:
        password = input("Введите пароль: ")
        check = check_password(username, password)
        if check:
            break
    with open(db, 'a') as f:
        f.write(f"{username},{password}\n")


def create_user(db):
    username = input("Введите имя пользователя: ")
    while not check_password(
        username, password := input("Введите пароль: ")
    ):
        pass
    with open(db, 'a') as f:
        f.write(f"{username},{password}\n")


create_user('passwords.txt', password_length=10, spec_sym=True)
