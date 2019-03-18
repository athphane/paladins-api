import session as ses
import json
import urllib.request
import env

# Returns the amount of sessions and requests that have been made to the API
def checkApiLimits() :
    limit_url = 'http://api.paladins.com/paladinsapi.svc/getdatausedJson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getdataused', file_data['datetime'])
    url = limit_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime']
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents[0]

# This one doesn't seem to work anymore. Will make sure to check up on this.
def getServerStatus() :
    server_stat_url = 'http://api.paladins.com/paladinsapi.svc/gethirezserverstatus'
    file_data = ses.getPreviousSession()
    sig = ses.signature('gethirezserverstatus', file_data['datetime'])
    url = server_stat_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime']
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents[0]

# Gets all the details of a player
def getPlayer(player) :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getplayerJson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getplayer', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + player 
    contents = urllib.request.urlopen(url).read()
    return json.loads(contents.decode('utf-8'))[0]

# Gets the player status. [offline, online, in-game, in game lobby, in lobby]
def getPlayerStatus(player) :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getplayerstatusJson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getplayerstatus', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + str(getPlayer(player)['Id'])
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents[0]

def getMatchHistory(player) :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getmatchhistoryJson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getmatchhistory', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + str(getPlayer(player)['Id'])
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents

def getPlayerAchievements(player) :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getplayerachievementsJson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getplayerachievements', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + str(getPlayer(player)['Id'])
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents

def getChampionRanks(player) :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getchampionranksJson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getchampionranks', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + str(getPlayer(player)['Id'])
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents

def getItems() :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getitemsjson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getitems', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + '1'
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents

def getMatchDetails(match_id) :
    get_player_url = 'http://api.paladins.com/paladinsapi.svc/getmatchdetailsjson'
    file_data = ses.getPreviousSession()
    sig = ses.signature('getmatchdetails', file_data['datetime'])
    url = get_player_url + '/' + env.devID + '/' + sig + '/' + file_data['session_id'] + '/' + file_data['datetime'] + '/' + str(match_id)
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return contents
