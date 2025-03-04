PASSWORD = input(str("Введите пароль: "))


def is_very_long(PASSWORD):    
    return any ([len(PASSWORD) >= 12])
    	

def has_digit(PASSWORD):
	return any(i.isdigit() for i in PASSWORD)
	

def has_upper_letters(PASSWORD):
	return any(i.isupper() for i in PASSWORD)
	

def has_lower_letters(PASSWORD):
	return any(i.islower() for i in PASSWORD)


def has_symbols(PASSWORD):
	return any(not i.isalnum() for i in PASSWORD)


def main(PASSWORD):

    score = 0
    checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
	
    for check in checks:
	    if check(PASSWORD):
		    score += 2

    print("Рейтинг пароля: ", score)
    return score

if __name__ == "__main__":
    main(PASSWORD)