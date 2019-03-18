import telepot
import functions as func
import session as ses
import sys
from send_the_message import sendMessage

ses.main()
chat_id = sys.argv[1]

if __name__ == "__main__":
    limits = func.checkApiLimits()
    if limits['ret_msg'] :
        msg = limits['ret_msg']
        message = "*== API USAGE REPORT ==*" + "\n" + "API ERROR \n: " + str(msg) + "\n" 
    else :
        active = str(limits['Active_Sessions'])
        req_today = str(limits['Total_Requests_Today'])
        sessions_today = str(limits['Total_Sessions_Today'])
        message = "*== API USAGE REPORT ==*" + "\n" + "Active Sessions: " + active + "\n" + "Requests Today: " + req_today + "\n" + "Sessions Today: " + sessions_today + "\n"

    sendMessage(chat_id, message)
