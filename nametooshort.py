class NameTooShortError(Exception):
    pass



def validate_name(name):
    if len(name)<8:
        raise NameTooShortError('name is too short')
    else:
        return name




username = input("Enter your name: ")
validate_name(username)

print(f'Hello {username}')