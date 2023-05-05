data = open('todo.txt').readlines()
while '\n' in data:
    data.pop(data.index('\n'))
exit_flag=0
while True:
    if exit_flag==1:
        break
    print('Hello, comrade! We are heppy to see you at our app')
    print('For adding task, enter"add"')
    print('For show all your tasks, enter "show"')
    print('For delete one of your tasks, enter "delete"')
    print('For exit the app, enter "exit"')
    command = input('Enter command->')
    if command=='add':
        case = input("Enter task ->")
        data.append(case)    
    elif command=='delete':
        while True:
            for i in range(0, len(data)):
                print(str(i+1) + '. ' + data[i])
            print("What task's already done?")
            case_delete_index = int(input('Enter the number ->'))
            try:
                data.pop(case_delete_index - 1)
                break
            except:
                print('Somethimg wrong')
    elif command=='show':
        for i in range(0, len(data)):
            print(data[i])
    elif command=='exit':
        exit_flag=1
        todo_file = open('todo.txt', 'w')
        for i in range(0, len(data)):
            todo_file.write(data[i])
    else:
        print('Wrong command')