import telepot
import session as ses
import sys
import json
from functions import getMatchHistory
from functions import getPlayer
from send_the_message import sendMessageInlineKeyboard, sendMessage
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


ses.main()

chat_id = sys.argv[1]

def getMatches(player) :
    matches = getMatchHistory(player)
    return matches

def constructButtonText(player_arg):
    matches = getMatches(player_arg)

    matches_arr = []
    message_arr = []
    champs_arr = []
    win_status_arr = []
    count = 1
    arr_val = 0
    while count <= 5 :
        #code here
        match_id = matches[arr_val]['Match']
        message = "/sendmatch " + player_arg + " " + str(match_id)
        champion = matches[arr_val]['Champion']
        win_status = matches[arr_val]['Win_Status']

        matches_arr.append(match_id)
        message_arr.append(message)
        champs_arr.append(champion)

        if win_status == "Win":
            win_status_arr.append("🔵")
        else:
            win_status_arr.append("🔴")

        count += 1
        arr_val += 1
    
    count = 1
    arr_val = 0
    text_arr = []
    while count <= 5 :
        text = str(str(count) + "- " + win_status_arr[arr_val] + " " + champs_arr[arr_val])
        text_arr.append(text)
        count += 1
        arr_val += 1

    return [text_arr, message_arr]

if __name__ == '__main__':
    # Checking if the player is actually valid because 
    # Node-RED sends Undefined when param not provided
    unauthorized = ['Undefined', 'undefined']
    player_arg = sys.argv[2]
    if player_arg in unauthorized :
        message = "Enter a player name"
        sendMessage(chat_id, message)
        exit()
    else: 
        button_arr = constructButtonText(player_arg)
        print (button_arr)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text=button_arr[0][0], callback_data=button_arr[1][0]), InlineKeyboardButton(text=button_arr[0][1], callback_data=button_arr[1][1])],
                   [InlineKeyboardButton(text=button_arr[0][2], callback_data=button_arr[1][2]), InlineKeyboardButton(text=button_arr[0][3], callback_data=button_arr[1][3])],
                   [InlineKeyboardButton(text=button_arr[0][4], callback_data=button_arr[1][4])],
               ])

        message = 'Here are the last 5 matches for *' + getPlayer(player_arg)['Name'] + '*'
        sendMessageInlineKeyboard(chat_id, message, keyboard)