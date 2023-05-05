data = open('todo.txt').readlines()
while '\n' in data:
    data.pop(data.index('\n'))
exit_flag=0
while True:
    if exit_flag==1:
        break
    print('Здравствуйте, товарищ! Мы рады приветствовать вас в нашем приложении')
    print('Для того, чтобы добавить задачу введите команду "add"')
    print('Для того, чтобы просмотреть задачи введите команда "show"')
    print('Для того, чтобы удалить задачу введите команду "delete"')
    print('Для того, чтобы выйти из приложения введите команду "exit"')
    command = input('Введите команду->')
    if command=='add':
        case = input("Введите задачу ->")
        data.append(case)    
    elif command=='delete':
        while True:
            for i in range(0, len(data)):
                print(str(i+1) + '. ' + data[i])
            print("Какую задачу вы уже выполнили?")
            case_delete_index = int(input('Введите номер ->'))
            try:
                data.pop(case_delete_index - 1)
                break
            except:
                print('Что-то пошло не так, попробуйте еще раз')
    elif command=='show':
        for i in range(0, len(data)):
            print(data[i])
    elif command=='exit':
        exit_flag=1
        todo_file = open('todo.txt', 'w')
        for i in range(0, len(data)):
            todo_file.write(data[i])
    else:
        print('Вопрос непонятен')