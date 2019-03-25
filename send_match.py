import telepot
import session as ses
import sys
import json
from functions import getMatchHistory
from send_the_message import sendMessage

ses.main()

chat_id = sys.argv[1]

def getMatch(player, match_id) :
    matches = getMatchHistory(player)
    for match in matches:
        match_from_json = match['Match']
        if str(match_id) in str(match_from_json):
            return match

def getLoadoutDetails(singleton) :
    # Loadout items
    champ_items_dicts = ['Item_1', 'Item_2', 'Item_3', 'Item_4', 'Item_5']
    champ_items = []
    for champ_items_dict in champ_items_dicts :
        item = singleton[champ_items_dict]
        if len(item) :
            champ_items.append(item)

    # Loadout item levels
    champ_items_levels_dicts = ['ItemLevel1', 'ItemLevel2', 'ItemLevel3', 'ItemLevel4', 'ItemLevel5']
    champ_item_levels = []
    for champ_items_levels_dict in champ_items_levels_dicts :
        level = singleton[champ_items_levels_dict]
        champ_item_levels.append(level)

    # Constructing the message and saving into array
    # My madness will make sense later
    item_with_level = []
    count = 1
    arr_val = 0
    while count <= 5 :
        text = champ_items[arr_val] + ' - Lv: ' + str(champ_item_levels[arr_val])
        item_with_level.append(text)
        count += 1
        arr_val += 1

    final_text = ''
    for item_level in item_with_level :
        final_text += item_level + '\n'

    # Finally done. Returning constructed message. 
    final_text = '*- Champion Loadout -*' + '\n' + final_text
    return final_text

def getMatchItemDetails(singleton) :
    # In game purchases
    match_item_dicts = ['Active_1', 'Active_2', 'Active_3', 'Active_4']
    match_items = []

    for match_item_dict in match_item_dicts :
        item = singleton[match_item_dict]
        if len(item) :
            match_items.append(item)

    len_of_items = len(match_items)
    count = 1
    arr_val = 0
    final_text = ''
    while count <= len_of_items :
        final_text += match_items[arr_val] + '\n'
        count += 1
        arr_val += 1

    final_text = '*- In game items -* \n' + final_text

    return final_text

if __name__ == '__main__':
    # Checking if the player is actually valid because 
    # Node-RED sends Undefined when param not provided
    unauthorized = ['Undefined', 'undefined']
    player_arg = sys.argv[2]
    match_id = sys.argv[3]

    if player_arg in unauthorized :
        message = "Enter a player name"
        sendMessage(chat_id, message)
        exit()
    else: 
        singleton = getMatch(player_arg, match_id)
        print(singleton)

        # Easy vals to get
        player =        'Player: '          + str(singleton['playerName'])      + '\n'
        champion =      'Champion: '        + str(singleton['Champion'])        + '\n'
        damage_delt =   'Damage delt: '     + str(singleton['Damage'])          + '\n'
        damage_taken =  'Damage taken: '    + str(singleton['Damage_Taken'])    + '\n' 
        deaths =        'Deaths: '          + str(singleton['Deaths'])          + '\n' 
        healing =       'Healing: '         + str(singleton['Healing'])         + '\n' 
        killing_spree = 'Killing spree: '   + str(singleton['Killing_Spree'])   + '\n' 
        win_status =    'Win status: '      + str(singleton['Win_Status'])      + '\n'
        queue =         'Queue: '           + str(singleton['Queue'])           + '\n'

        title = '*== Match Details ==* \n'
        loadout_details = getLoadoutDetails(singleton)
        match_items = getMatchItemDetails(singleton)
        message = title + player + champion + queue + damage_delt + damage_taken + killing_spree + healing + win_status + '\n' + loadout_details + '\n' + match_items
        sendMessage(chat_id, message)
