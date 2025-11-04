from DTO.Videogame import Videogame

# CONTROLLER

games_list = [] # list to store all videogames

# controller functions
def add_game():
    try:
        new_vg = Videogame(create_id(),
                           None,
                           None,
                           None,
                           None)

        # properties that has to be checked are asked apart
        new_vg.name = valid_name(input('How is the new game called? '))
        new_vg.price = valid_price(input('What\'s this game price? '))
        new_vg.tags = ask_tags()
        valid_year((input('In what year was it launch? ')))

        # once a valid videogame is created, is added to the list
        games_list.append(new_vg)
        print('Game was added successfully!\n\n')

    except:
        print('Error, game was not created.')


def modify_game(selected_game_id):
    game_to_modify = fetch_game(selected_game_id)

    if game_to_modify!=None:
        game_to_modify.name = input('Changed name: ')
        game_to_modify.price = valid_price(input('New price: '))
        game_to_modify.tags = ask_tags()
        game_to_modify.year_of_creation = valid_year(input('Release year: '))


def delete_game(selected_game_id):
    game_to_delete = fetch_game(selected_game_id)

    if game_to_delete != None:
        games_list.remove(game_to_delete)
        print('Game deleted!\n\n')


def create_id():
    if len(games_list) > 0:
        return max(games_list, key= lambda game: game.Id).Id + 1
    else:
        return 1


def fetch_game(game_id):
    try:
        ex = int(game_id)
        for game in games_list:
            if game.Id == ex:
                return game
        print('Game not found!')
        return None

    except ValueError:
        print('Error, id is a whole number, try using one.')


# validation functions
def valid_name(name):
    while len(name) == 0:
        name = input('Error, name space is blank, enter a name: ')
    return name


def valid_price(price):
    while True:
        try:
            return float(price)
        except ValueError:
            price = input('Error, invalid price, enter a decimal number for the price: ')


def valid_year(year):
    while True:
        try:
            return int(year)
        except ValueError:
            year = input('Error, invalid year, enter a whole number for the year: ')


def ask_tags():
    tags = []
    print('Enter the new game tags one by one, left the space in blank to proceed')

    while True: # enter tags as long as it's not empty and has at least 1 tag
        print(f'\n\ntags already in: {tags}')
        tag = input('tag: ')

        if len(tag) == 0 and len(tags)>0:
            print('All tags have been retrived!')
            break
        elif len(tag) == 0 and len(tags) == 0:
            print('Error, you haven\'t input any tags yet.')
        else:
            tags.append(tag)

    return tags


def update():
    games_list.sort(key= lambda game: game.Id, reverse= False)


# to string
def to_string():
    listed_games = ''

    for game in games_list:
        listed_games+= (f'{game.Id} | {game.name} | {game.price} | '
                        f'{game.year_of_creation} | {game.tags} | {game.year_of_creation}\n')
    return listed_games if len(listed_games) > 0 else 'There are no games yet!\n'