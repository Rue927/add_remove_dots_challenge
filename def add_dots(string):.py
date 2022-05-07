def add_dots(string):
    new_string = ".".join(string)
    return new_string
print(add_dots("test"))

def remove_dots(string):
    new_string = string
    result = new_string.replace(".", "")
    return result