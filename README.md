# Paladins Telegram Bot

## ALL THE SCRIPTS IN THIS REPO ARE CONFIGURED TO WORK WITH NODE-RED OUT OF THE BOX. IF YOU WANT TO USE THE THINGS STANDALONE, PLEASE GO THROUGH THE CODE AND REFACTOR..

### I WILL BE MAKING NECESSARY CHANGES TO MAKE IT COMPLETELY MODULARIZED WHEN I GET IT WORKING AS GOOD AS I WANT IT TO

This package can be used to get details of the game using the HiRez API.

Only supports **Paladins**. (Since I only play that game)

*Each file is named as what it does. Message construction is also done.*


Right now each file is configured to accept 2-3 parameters.

 - param 1 = chatID of the telegram chat
 - param 2 = name of the player you want to get details of
 - param 3 = name of the champion. (This one only applicable to send_champions_details.py)

  


### Things you need
---

 - You will need your own HiRez Dev ID and Auth Key, which is easily obtainable from their [online form](https://fs12.formsite.com/HiRez/form48/secure_index.html).  
 - You need your own bot on Telegram and it's API keys.
 - Runs on Python 3. Not 2.7.
 - You will need the a Python package called
   '[telepot'](https://pypi.org/project/telepot/)


---
I use Node-RED to make this work. It works for me and my friends extremely well. 
Currently under active development
