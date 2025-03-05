def is_very_long(password):    
    return len(password) >= 12
        

def has_digit(password):
    return any(i.isdigit() for i in password)
    

def has_upper_letters(password):
    return any(i.isupper() for i in password)
    

def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isalnum() for i in password)


def main():

    password = input(str("Введите пароль: "))
    score = 0
    checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    for check in checks:
        if check(password):
            score += 2
    print("Рейтинг пароля: ", score)
    return score


if __name__ == "__main__":
    main()