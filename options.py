import pokemon_attributes as pa
import sys
import moves

# Note: options 8 and 9 are straightforward enough to implement in main.py


# option 1
def add_to_party(party_count, my_party):
    if party_count == 6:
        print('Party is full! Cannot add to party.')
        return
    poke_mon = input('Choose a PokéMon to add: ').title()
    myPokeMon = verify_mon(poke_mon)
    if myPokeMon is not None:
        my_party.append(myPokeMon)
        party_count += 1
    else:
        print('Add to party failed. No changes made.')


# option 2
def change_ivs(iv_choice, party_count, poke_to_change):
    while iv_choice < 1 or iv_choice > party_count:
        print('Invalid entry. Please select a valid option (1-6).')
        iv_choice = int(input())

    new_iv = int(input('Enter the new IV (0-31'))

    # 1. HP
    if iv_choice == 1:
        poke_to_change.ivs[0] = new_iv

    # 2. Attack
    elif iv_choice == 2:
        poke_to_change.ivs[1] = new_iv

    # 3. Defense
    elif iv_choice == 3:
        poke_to_change.ivs[2] = new_iv

    # 4. Special Attack
    elif iv_choice == 4:
        poke_to_change.ivs[3] = new_iv

    # 5. Special Defense
    elif iv_choice == 5:
        poke_to_change.ivs[4] = new_iv

    # 6. Speed
    elif iv_choice == 6:
        poke_to_change.ivs[5] = new_iv


# option 3
def change_evs():
    pass


# option 4
def change_nature():
    pass


# option 5
def change_held_item():
    pass


# option 6
def change_moves():
    pass


# option 7
def change_pokemon():
    pass


# helper function
# Returns Pokémon data if found, None if not found
def verify_mon(pokemon):
    pa.myCursor.execute(f"SELECT * FROM pokemon_stats where `Name` = \"{pokemon}\"")
    res = pa.myCursor.fetchone()
    if res is None:
        print('No match found.')
        return None
    myPokeMon = pa.PokeMon(res)
    print(f'You have added the following PokeMon to your party:\n{myPokeMon}')
    return myPokeMon


# starter function
# sets up initial party of first Pokémon
def starter(party_count, my_party):
    print('\nWelcome to the PokeMon Party Creator!')
    poke_mon = input('Choose a starting PokeMon: ').title()
    myPokeMon = verify_mon(poke_mon)
    if myPokeMon is not None:
        my_party.append(myPokeMon)
        party_count += 1
    else:
        sys.exit()
