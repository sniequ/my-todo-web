FILEPATH = "todos.txt"
# poniżej filepath dla aplikacji instalowanej
# FILEPATH = "todos.txt"

# definicja custom funkcji
# w () dodajemy argument funkcji
def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    """
    # wyświetlenie wartości zmiennej za każdym użyciem get_todos
    # print(f"filepath: {filepath}")
    with open(filepath, 'r') as file_local:
         todos_local = file_local.readlines()
    return todos_local

# doc string - utworzenie dokumentacji
# print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write to-do item in textfile.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


text = "\
Cena produktywności.\n\
Sprawdzenie danych\n\
Edycja cennika\n\
"
print(__name__)
print ("Im outside - wyświetla się także poza __main__ z functions.py także w cli.py")
if __name__ == "__main__":
    print(text)
