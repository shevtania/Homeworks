# decorator for exceptions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return f'Not enough input args, must be two paremeters: name and phone : "{exception.args[0]}"'
        except IndexError:
            return 'This contact cannot be added, it already exists.'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner

TEL_BOOK = {}

#blocks for input commands:

def hello():
    result = 'How can I help you?'
    return result

@input_error
def add_contact(*args):
    name, phone = args
    TEL_BOOK[name] = phone
    result = f'Contact {name} added'
    return result 

@input_error
def change_contact(*args):
    name, phone = args
    old_phone = TEL_BOOK[name]
    TEL_BOOK[name] = phone
    result = f'Old number {old_phone} for {name} has been replaced with a number {phone}'
    return result

@input_error
def phone_from_name(args):
    name = args[0]
    phone = TEL_BOOK[name]
    result = f'Contact {name} has number {phone}'
    return result


def  show_all():
    result = ''
    if TEL_BOOK ==  {}:
        result = f'There are no contacts in the book.'
        return result

    for name, phone in TEL_BOOK.items():
        result = result + f'{name} : {phone}\n'
        
    return result

def exit():
    return 'exit'
    
    

HANDLERS = {
    "hello": hello,
    "good bye": exit,
    "close": exit,
    "exit": exit,
    "add": add_contact,
    "change": change_contact,
    "show all": show_all,
    "phone": phone_from_name,
}

def parser_input(user_input):
    command, *args = user_input.split()
    handler = None
    command = command.lower()
    if command in HANDLERS:
        handler = HANDLERS[command]
    else:
        if args:
            command = command + ' ' + args[0]
            args = args[1:]
            if command in HANDLERS:
                handler = HANDLERS.get(command)
        
    return handler, *args


def main():
    while True:
        user_input = input("Input command: ")
        handler, *args = parser_input(user_input)
        if handler:
            result = handler(*args)
        else:
            result = f'Unknown command'    
        
        if result == 'exit':
            print("Good bye!")
            break
        print(result)
        


if __name__ == "__main__":
    main()