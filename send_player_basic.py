import telepot
import functions as func
import session as ses
import sys
from send_the_message import sendMessage

ses.main()
chat_id = sys.argv[1]

if __name__ == "__main__":
    try:
        player_arg = sys.argv[2]
        player = func.getPlayer(player_arg)
        name = str(player['Name'])
        player_level = str(player['Level'])
        hours_played = str(player['HoursPlayed'])
        total_plays = str(player['Wins'] + player['Losses'])
        total_wins = str(player['Wins'])
        total_losses = str(player['Losses'])
        win_ratio = ( (int(total_wins) / int(total_plays) ) * 100)
        win_ration_round = str(round(win_ratio, 2))

        message = "*==" + name + "==*" + "\n" + "Level: " + player_level + "\n" + "Hours played: " + hours_played + "\n" + "Total Plays: " + total_plays + "\n" + "Total Wins: " + total_wins + "\n" + "Total Losses: " + total_losses + "\n" + "Win ratio: " + win_ration_round + "%\n"
        sendMessage(chat_id, message)

    except IndexError as e:
        message = "Enter a player name"
        sendMessage(chat_id, message)
