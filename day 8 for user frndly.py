def get_todos():  # it's only work when we call function (get_todos()) in new variable like : todos = get_todos()
    with open('rows.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

todos = []
# file = open(r"C:\Users\Abhi\PycharmProjects\pythonProject\row.txt", 'r') we use "r" for removing \n, \t, \a effect in location path

while True:
    user_action = input("add, show, edit (ex: edit 2), remove (ex: remove 3), all items, or exit : ")
    user_action = user_action.strip() # use : remove space from input(user_action)

  # if 'add' in user_action:  # this is old line of code
    if user_action.startswith("add"):  # 1) is use for only remove first 0,1,2,3, char of user input remove from only "add" input
        todo = user_action[4:]
  #this todos is not lical viariable its a globle variable
        todos = get_todos()   #replace by➡️ #  with open('rows.txt', 'r') as file:
                                               #   todos = file.readlines()  #   method 2
        todos.append(todo + '\n')

        with open('rows.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n") # use : to remove ("\n") | # method 3 :for strip ("\n")
            index = index + 1
            row = f"{index}-{item}" #as well as we can write {index + 1} for start index from 1
           # print(index, item)
            print(row)

            # with open('rows.txt', 'w') as file:
            #     file.writelines(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:])
            print(number)

            number = number - 1

            todos = get_todos()

            print('You choose this word to Edit : ', todos[number])
            new_char = input("Enter new charecter : ")
            todos[number] = new_char + '\n'
           # number = number + 1
            print(number + 1,'replaced by : ',new_char) #in loop we can print index one by one with out using [number = number + 1]

            with open('rows.txt', 'w') as file:
                file.writelines(todos)  # it will posible in it: file.writelines(['a', 'b', 'c'])
        except ValueError:    # we use exception error because user enter wrong input
            print("sir, you enter wrong value try again!")   #
        except IndexError:
            print("sir, you enter wrong number try again!")
            continue          # its for start code from while loop or Beginning or any loop
        # for item in todos:
        #     print(item)
    elif user_action.startswith('remove'):
        try:
            number = int(user_action[6:])
            todos = get_todos()

            number = number - 1
            user_remove_item =  todos[number].strip('\n')
            todos.pop(number)

            with open('rows.txt', 'w') as file:
                file.writelines(todos)

            message = f"You remove {user_remove_item} form the list."
            print(message)
        except ValueError:
            print("sir, you enter wrong value try again!")
        except IndexError:
            print("sir, you enter wrong nummber try again!")
            continue

    elif user_action.startswith('all items'):
        print(len(todos))
    elif 'exit' in user_action:
        break

    # if whatever in user_action:  # most of programer use _ for whatever   "_"
    #    print("hey you enter a unknown command here please try again")

print("thanx for intracting with us !")

