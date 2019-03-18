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

        # If a third argument exists, only send the details of said champion
        if len(sys.argv) > 3 :
            champion_arg = sys.argv[3].lower()
            champion_list = []

            # My way of getting a list of champions played by the player 
            # This madness will make sense later
            for champion in champions:
                champion_name = champion['champion'].lower()
                champion_list.append(champion_name)

            # Iterating through all of the champion details
            for champion in champions:
                champion_name = champion['champion'].lower()

                # Checking if the champion name matches the name in champion argument (sys.argv[3])
                # Parses, constructs and sends message if it matches.
                if champion_arg in champion_name:
                    champ_name = champion['champion']
                    champ_rank = str(champion['Rank'])
                    champ_kills = str(champion['Kills'])
                    champ_deaths = str(champion['Deaths'])
                    champ_assists = str(champion['Assists'])
                    champ_gold = str(champion['Gold'])
                    champ_minutes = champion['Minutes']

                    # Pathetic attempt at trying to convert play minutes to hours and minutes.
                    # some have str() cause the message construction fails since it's an integer.
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

                    # Checking if the champion has been played at all
                    if champion['Wins'] >= 0 or champion['Losses'] > 1:

                        # Checking if the champion has any wins
                        if champion['Wins'] == 0:
                            champ_win_ratio = str(round(0,2)) # Converted to str() becuase
                        else:
                            
                            # This only hits when the champion does not have 0 wins. i.e: Has at least one win
                            # Calculates the win ratio of the champion
                            champ_win_ratio = ( champion["Wins"] / (champion['Wins'] + champion['Losses']) ) * 100
                            champ_win_ratio = str(round(champ_win_ratio,2))
                    else: 

                        # This made sense when I first made this if loop. I don't know what this does anymore.
                        # Probably a failsafe.
                        champ_win_ratio = str("NULL")

                    message = "*== CHAMPION STATS FOR " + player_name + " ==*" + "\n" + "Champion: " + champ_name + "\n" + "Rank: " + champ_rank + "\n" + "Kills: " + champ_kills + "\n" + "Deaths: " + champ_deaths + "\n" + "Assists: " + champ_assists + "\n" + "Gold Gained: " + champ_gold + "\n" + champ_minutes_str + "Wins: " + champ_wins + "\n" + "Losses: " + champ_losses + "\n" + "Win Ratio: " + champ_win_ratio + "%\n"
                    sendMessage(chat_id, message)

            # So this is where my madness makes sense? I referred to this in line 35
            # Literally check if the provided champion name is in the champion_list.
            # If it doesn't exist, well you can figure out what happens next.    
            if champion_arg not in champion_list:
                message = player_name + " has not played this champion yet."
                sendMessage(chat_id, message)


        # Now because I am an asshole, I won't comment on the ones after this. 
        # Literally does the same thing as above, but does it for each champion.
        # So if you have all the champions unlocked, well, have a good time. 
        else:
            for champion in champions:
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