import getpass


def is_very_long(password):
    return len(password) > 24


def is_case_sensitive(password):
    return not password.islower() and not password.isupper()


def has_digits_and_letters(password):
    has_digits = any(char.isdigit() for char in password)
    has_letters = any(char.isalpha() for char in password)
    return has_digits and has_letters


def has_special_characters(password):
    return not password.isalnum()


def is_very_short(password):
    return len(password) < 8


def has_digits_only(password):
    return password.isdigit()


def is_in_blacklist(password):
    # from top 50 most used passwords: https://wpengine.com/unmasked/
    blacklist = [
        'password',
        'baseball',
        'football',
        'qwertyuiop',
        'superman',
        '1qaz2wsx',
        'microsoft',
        'facebook',
    ]
    return password.lower() in blacklist


def compute_password_strength(password):
    bad_signs = [
        is_very_short,
        is_in_blacklist,
        has_digits_only,
    ]
    if any(bad_sign(password) for bad_sign in bad_signs):
        return 1
    strength_criteria = {
        is_very_long: 7,
        is_case_sensitive: 3,
        has_digits_and_letters: 2,
        has_special_characters: 1,
    }
    strength = 1
    for criterion, points in strength_criteria.items():
        if criterion(password):
            strength += points
    return min(strength, 10)


if __name__ == '__main__':
    password = getpass.getpass('Please enter the password to analyze: ')
    print(compute_password_strength(password))
