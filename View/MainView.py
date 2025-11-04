import Controller.VideogamesController as vgc

# functions
def menu():
    print('VIDEOGAME MANAGER\n\n')

    while True:
        match input('1. List games\n'
                    '2. Add game.\n'
                    '3. Modify game.\n'
                    '4. Delete game. \n'
                    'Option: '):
            case '1':
                print(f'{vgc.to_string()}')

            case '2':
                vgc.add_game()
                vgc.update()

            case '3':
                vgc.modify_game(input('What the id of the game you want to modify '
                                      '(enter 0 to cancel)? '))
                vgc.update()

            case '4':
                vgc.delete_game(input('What the id of the game you want to delete '
                                      '(enter 0 to cancel)? '))
                vgc.update()

            case '0':
                break

            case _:
                print('Error, invalid option, use one of the stated.\n\n')

    print('Program finilized!')


# program start
menu()