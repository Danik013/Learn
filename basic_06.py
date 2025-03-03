password = input(str("Введите пароль: "))


def is_very_long(password):    
    return any ([len(password) >= 12])
    	

def has_digit(password):
	return any(i.isdigit() for i in password)
	

def has_upper_letters(password):
	return any(i.isupper() for i in password)
	

def has_lower_letters(password):
	return any(i.islower() for i in password)


def has_symbols(password):
	return any(i == "%" or "#" for i in password)


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