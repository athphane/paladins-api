import telepot
import session as ses
import sys
from functions import getChampionRanks
from functions import getPlayer
from send_the_message import sendMessage

ses.main()

chat_id = sys.argv[1]

if __name__ == "__main__":

    # Checking if the player is actually valid because 
    # Node-RED sends Undefined when param not provided
    unauthorized = ['Undefined', 'undefined']
    player_arg = sys.argv[2]

    if player_arg in unauthorized :
        message = "Enter a player name"
        sendMessage(chat_id, message)
        exit()

    else :
        # Now running the real shit
        player_name = getPlayer(player_arg)['Name']
        champions = getChampionRanks(player_arg)

        count = 1
        arr_val = 0
        while count <= 5 :  
            champion = champions[arr_val]
            champ_name = champion['champion']
            champ_rank = str(champion['Rank'])
            champ_kills = str(champion['Kills'])
            champ_deaths = str(champion['Deaths'])
            champ_assists = str(champion['Assists'])
            champ_gold = str(champion['Gold'])
            champ_minutes = champion['Minutes']

            if champ_minutes > 60:
                champ_hours = champ_minutes / 60
                champ_hours = round(champ_hours)
                champ_minutes = str(champ_minutes % 60)
                champ_hours = str(champ_hours)
                champ_minutes_str = "Time Played: " + champ_hours + " Hours " + champ_minutes + " Minutes\n"
            else: 
                champ_minutes_str = "Time Played: " + str(champ_minutes) + " Minutes\n"
            

            champ_minutes = str(champ_minutes)
            champ_wins = str(champion['Wins'])
            champ_losses = str(champion['Losses'])

            if champion['Wins'] >= 0 or champion['Losses'] > 1:
                if champion['Wins'] == 0:
                    champ_win_ratio = str(round(0,2))
                else:
                    champ_win_ratio = ( champion["Wins"] / (champion['Wins'] + champion['Losses']) ) * 100
                    champ_win_ratio = str(round(champ_win_ratio,2))
            else: 
                champ_win_ratio = str("NULL")

            message = "*== CHAMPION STATS FOR " + player_name + " ==*" + "\n" + "Champion: " + champ_name + "\n" + "Rank: " + champ_rank + "\n" + "Kills: " + champ_kills + "\n" + "Deaths: " + champ_deaths + "\n" + "Assists: " + champ_assists + "\n" + "Gold Gained: " + champ_gold + "\n" + champ_minutes_str + "Wins: " + champ_wins + "\n" + "Losses: " + champ_losses + "\n" + "Win Ratio: " + champ_win_ratio + "%\n"
            sendMessage(chat_id, message)
        
            count += 1
            arr_val += 1