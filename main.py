import options
from options import *
import menus


def main():
    # counts how many Pokémon are in your party; party size should be <= 6 in main series games
    party_count = 0
    my_party = []
    choices_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # initializes my_party with choice of first Pokémon
    starter(party_count, my_party)
    menus.main_menu()

    while True:
        choice = input('Enter your choice (1-9): ')
        while choice not in choices_list:
            choice = input('Invalid entry. Re-enter your choice (1-9): ')

        # 1. Add Pokémon to party; can't have more than 6 Pokémon in party
        if choice == '1':
            add_to_party(party_count, my_party)
            party_count = len(my_party)

        # 2. Change PokeMon IVs
        elif choice == '2':
            poke_to_change = input('Which PokeMon would you like to change the stats of?'
                                       'Please enter their position in your party to avoid same-name conflicts.')
            while choice not in [str(i) for i in range(1, party_count + 1)]:
                poke_to_change = input('Please enter a number that corresponds to a position in your party,'
                                       f'i.e.,  (1-{party_count})')

            menus.iv_menu()
            options.change_ivs(int(input('Enter your choice: ')), party_count, poke_to_change)

            updated_ivs = input('Enter the new IVs as a space separated list: ').split()

        # 3. Change PokeMon EVs
        elif choice == '3':
            pass

        # 4. Change PokeMon Nature
        elif choice == '4':
            new_nature = input('Enter the nature you wish to apply: ').title()
            while new_nature not in pa.Natures:
                new_nature = input('Please enter a valid nature: ').title()

            print(f'Here are your new stats after changing nature:\n\n')

        elif choice == '5':
            pass
        elif choice == '6':
            pass

        # swap mon for another
        elif choice == '7':
            pass

        # something else
        elif choice == '8':
            break
        elif choice == '9':
            for i in my_party:
                print(i)


main()

print('\nThanks for using this program! bye bye ;-)')
