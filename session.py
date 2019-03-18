import datetime
from datetime import datetime
import time
import hashlib
import requests
import urllib.request
import json
import sys, os
import telepot
import chardet
import env

# Datetime string formatted to the way the API wants
def getDateTimeStamp() :
    timestamp = int(time.time())
    converted = datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d%H%M%S') 
    return {'datetime':converted, 'computertime':timestamp}

# Generate the signature and hash it using md5
def signature(method = "createsession", dtstring = getDateTimeStamp()['datetime']) :
    signature = env.devID + method + env.authKey + str(dtstring)
    hashed_signature = hashlib.md5(signature.encode('utf-8')).hexdigest()
    return hashed_signature

# Get session ID reuqired for every single other request.
def getSessionID() :
    session_endpoint = "http://api.paladins.com/paladinsapi.svc/createsessionJson/"
    final_session_endpoint = session_endpoint + env.devID + "/" + signature() + "/" + getDateTimeStamp()['datetime']
    contents = urllib.request.urlopen(final_session_endpoint).read()
    json_document =  contents
    python_obj = json.loads(json_document.decode('utf-8'))
    writeString = json.dumps({'session_id': python_obj["session_id"], 'datetime': getDateTimeStamp()['datetime'], 'computertime' : getDateTimeStamp()['computertime']})
    f = open("session.json", "w")
    f.write(writeString)
    return writeString

# Get the last used session details. These details will be used for the next request.
# This is done to not hit the API rate limits. 
def getPreviousSession() :
    f = open("session.json" , "r")
    file_json = f.read()
    contents = json.loads(file_json)
    
    if contents :
        return contents
    else :
        getSessionID()

# This gets the currently stored session details and checks if 5 minutes has passed
# since the last session request. Sessoins expire every 15 minutes. 
def getValidSession() :
    previous_session = getPreviousSession()
    passed = getDateTimeStamp()['computertime'] - previous_session['computertime']
    if passed >= 400 : 
        new_session = getSessionID()
        return new_session
    else :
        return previous_session

# Check if file where the sessions details are accessible
def fileIsAccessible() :
    if os.path.exists('session.json') == 0 :
        return getSessionID()
    else :
        return getValidSession()

# The main function
def main() :
    fileIsAccessible()

if __name__ == "__main__":
    main()