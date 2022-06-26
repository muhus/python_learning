word = 'Test'
command = "down"


def up(word):
    return word.upper()


def down(word):
    return word.lower()


def default(*args, **kwargs):
    return "Unknown"


def process(command):
    command_dict = {
        'up': up,
        'down': down,
    }

    if command in command_dict:
        return command_dict[command]
    else:
        return default()

print(process(command)(word))
# якщо прибрати (word) то повертається сама функція,
# магія пайтону в тому що він може одразу підставляти аргументи в повернену функцію