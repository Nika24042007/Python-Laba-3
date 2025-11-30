from src.parser import parser
from src.constants import COMMANDS
from src.constants import COMMANDS_QUEUE


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    queue = None
    while True:
        f= 0
        ask = input("Enter command: ")
        if ask == "exit":
            return
        else:
            ask = parser(ask)
            try:
                if ask[0] in COMMANDS:
                    print(COMMANDS[ask[0]](*ask[1:]))
                elif ask[0] in COMMANDS_QUEUE:
                    if ask[0] != "creat" and queue == None:
                        f = 1
                        print("Error: no queue")
                    if ask[0] == "creat":
                        queue=COMMANDS_QUEUE[ask[0]]()
                        print("Очередь создана")
                    else:
                        print(COMMANDS_QUEUE[ask[0]](queue, *ask[1:]))
                        print("Команда выполнена")
                    
                else:
                    print("Command not found")
            except Exception as e:
                if f == 0:
                    print(f"Error: {e}")

if __name__ == "__main__":
    main()
